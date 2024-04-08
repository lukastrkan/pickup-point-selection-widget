import requests
from django.db.models import Q

from app.graphql.coordinates import Coordinates, CoordinatesInput

from branchData.models import Branch

import graphene


class Cluster(graphene.ObjectType):
    coordinates = graphene.Field(Coordinates)
    id = graphene.Int()
    cluster = graphene.Boolean()
    point_count = graphene.Int()
    cluster_zoom = graphene.Int()

    def __init__(self, latitude=None, longitude=None, id=None, cluster=None, point_count=None, cluster_zoom=None):
        self.latitude = latitude
        self.longitude = longitude
        self.id = id
        self.cluster = cluster
        self.point_count = point_count
        self.cluster_zoom = cluster_zoom

    def resolve_coordinates(self, info):
        return Coordinates(latitude=self.latitude, longitude=self.longitude)


def convert_to_geojson(branches):
    features = []
    for branch in branches:
        feature = {
            "type": "Feature",
            "properties": {
                "branchId": str(branch['id'])
            },
            "geometry": {
                "type": "Point",
                "coordinates": [float(branch['longitude']), float(branch['latitude'])]
            }
        }
        features.append(feature)
    return features


class ClustersQuery(graphene.ObjectType):
    clusters = graphene.List(Cluster, zoom=graphene.Int(required=True),
                             coordinatesA=graphene.Argument(CoordinatesInput, required=False),
                             coordinatesB=graphene.Argument(CoordinatesInput, required=False),
                             branch_type=graphene.Int(required=False))

    def resolve_clusters(self, info, zoom, branch_type=None, coordinatesA=None, coordinatesB=None):
        q = Q()
        if branch_type:
            q &= Q(branch_type_id=branch_type)
        if coordinatesA and coordinatesB:
            q &= Q(latitude__lte=round(coordinatesA.latitude, 6),
                   latitude__gte=round(coordinatesB.latitude, 6),
                   longitude__gte=round(coordinatesA.longitude, 6),
                   longitude__lte=round(coordinatesB.longitude, 6))
        branches = Branch.objects.filter(q)
        vals = branches.values('id', 'latitude', 'longitude', 'branch_type_id')
        points = convert_to_geojson(vals)

        r = requests.post('http://supercluster:5000/cluster', json={'points': points, 'zoom': zoom})

        for data in r.json():
            branch_id = None
            cluster = False
            point_count = 1
            cluster_zoom = None
            if 'branchId' in data['properties']:
                branch_id = data['properties']['branchId']
            if 'cluster' in data['properties']:
                cluster = data['properties']['cluster']
            if 'point_count' in data['properties']:
                point_count = data['properties']['point_count']
            if 'zoom' in data['properties']:
                cluster_zoom = data['properties']['zoom']

            yield Cluster(latitude=data['geometry']['coordinates'][1], longitude=data['geometry']['coordinates'][0],
                          id=branch_id,
                          cluster=cluster, point_count=point_count, cluster_zoom=cluster_zoom)
