import graphene
from graphene_django.types import DjangoObjectType

from branchData.models import BranchType


class BranchTypes(DjangoObjectType):
    id = graphene.ID(source='pk', required=True)
    name = graphene.String(required=True)

    class Meta:
        interfaces = (graphene.relay.Node,)
        model = BranchType
        fields = ('id', 'name', 'icon')


class BranchTypeQuery(graphene.ObjectType):
    branch_types = graphene.List(BranchTypes)

    def resolve_branch_types(self, info):
        return BranchType.objects.all()
