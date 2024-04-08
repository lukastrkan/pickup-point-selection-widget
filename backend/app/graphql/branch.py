import graphene
from graphene_django.types import DjangoObjectType

import branchData.models
from .coordinates import Coordinates


def load_data(current):
    to_add = []
    for x in current:
        to_add.append(f"{x['open']} - {x['close']}")
    if len(to_add) == 0:
        return None
    return ', '.join(to_add)


class OpeningHours(graphene.ObjectType):
    monday = graphene.String()
    tuesday = graphene.String()
    wednesday = graphene.String()
    thursday = graphene.String()
    friday = graphene.String()
    saturday = graphene.String()
    sunday = graphene.String()

    def resolve_monday(self, info):
        return load_data(self['monday'])

    def resolve_tuesday(self, info):
        return load_data(self['tuesday'])

    def resolve_wednesday(self, info):
        return load_data(self['wednesday'])

    def resolve_thursday(self, info):
        return load_data(self['thursday'])

    def resolve_friday(self, info):
        return load_data(self['friday'])

    def resolve_saturday(self, info):
        return load_data(self['saturday'])

    def resolve_sunday(self, info):
        return load_data(self['sunday'])


class Branch(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    coordinates = graphene.Field(Coordinates)
    openning_hours = graphene.Field(OpeningHours)

    class Meta:
        interfaces = (graphene.relay.Node,)
        model = branchData.models.Branch
        fields = (
            'id', 'name', 'branch_type', 'address', 'city', 'zip', 'country', 'openning_hours', 'branchId', 'box',
            'card', 'wheelchair')

    def resolve_coordinates(self, info):
        return Coordinates(latitude=self.latitude, longitude=self.longitude)


class BranchQuery(graphene.ObjectType):
    branch = graphene.Field(Branch, id=graphene.Int(required=True))

    def resolve_branch(self, info, id):
        return branchData.models.Branch.objects.get(pk=id)
