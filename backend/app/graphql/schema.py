import graphene
from .branches import BranchesQuery
from .branch_types import BranchTypeQuery
from .branch import BranchQuery
from .clusters import ClustersQuery


class Query(BranchesQuery, BranchTypeQuery, BranchQuery, ClustersQuery):
    pass


schema = graphene.Schema(query=Query)
