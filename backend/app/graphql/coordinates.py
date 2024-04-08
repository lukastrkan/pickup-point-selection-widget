import graphene


class Coordinates(graphene.ObjectType):
    latitude = graphene.Float(required=True)
    longitude = graphene.Float(required=True)

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


class CoordinatesInput(graphene.InputObjectType):
    latitude = graphene.Float(required=True)
    longitude = graphene.Float(required=True)
