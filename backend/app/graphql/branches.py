import graphene
from django.db.models import Q

import app.graphql.branch
from branchData.models import Branch
from .coordinates import CoordinatesInput


def get_queried_fields(info):
    field_names = []
    for field in info.field_nodes:
        for selection in field.selection_set.selections:
            if hasattr(selection, 'name'):
                if selection.name.value != '__typename':
                    field_names.append(selection.name.value)
            elif hasattr(selection, 'selection_set'):
                for sub_selection in selection.selection_set.selections:
                    if hasattr(sub_selection, 'name'):
                        if sub_selection.name.value != '__typename':
                            field_names.append(sub_selection.name.value)
    return field_names


class BranchesQuery(graphene.ObjectType):
    branches = graphene.List(app.graphql.branch.Branch,
                             coordinatesA=graphene.Argument(CoordinatesInput, required=False),
                             coordinatesB=graphene.Argument(CoordinatesInput, required=False),
                             country=graphene.Argument(graphene.String, required=False),
                             search=graphene.Argument(graphene.String, required=False),
                             branchType=graphene.Argument(graphene.Int, required=False))

    def resolve_branches(self, info, coordinatesA=None, coordinatesB=None, country=None, search=None, branchType=None):
        q = Q()
        qb = Branch.objects
        if coordinatesA and coordinatesB:
            q &= Q(latitude__lte=round(coordinatesA.latitude, 6),
                   latitude__gte=round(coordinatesB.latitude, 6),
                   longitude__gte=round(coordinatesA.longitude, 6),
                   longitude__lte=round(coordinatesB.longitude, 6))
        if country:
            q &= Q(country=country)
        if search:
            q &= Q(name__icontains=search) | Q(address__icontains=search) | Q(city__icontains=search) | Q(
                zip__icontains=search)
        if branchType:
            q &= Q(branch_type_id=branchType)

        to_query = []
        for field in get_queried_fields(info):
            if field == 'coordinates':
                to_query.append('latitude')
                to_query.append('longitude')
            elif field == 'openningHours':
                to_query.append('openning_hours')
            elif field == 'branchType':
                to_query.append('branch_type')
                qb = qb.select_related('branch_type')
            else:
                to_query.append(field)
        if len(to_query) > 0:
            qb = qb.only(*to_query)
        return qb.filter(q)
