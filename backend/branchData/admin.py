from django.contrib import admin
from django.utils.safestring import mark_safe

from branchData.models import BranchType, Branch
from branchData.utils.ceskaPostaUtil import CeskaPostaUtil, BalikovnaUtil
from branchData.utils.balikobotPPLUtil import BalikobotPPLUtil
from branchData.utils.zasilkovnaUtil import ZasilkovnaUtil
from branchData.utils.dpdUtil import DpdUtil


# Register your models here.

@admin.register(BranchType)
class BranchTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    actions = ['loadBalikovna', 'loadCeskaPosta', 'loadZasilkovna', 'loadDpd', 'loadPPL']

    @admin.action(description='Aktualizovat pobočky Balíkovny')
    def loadBalikovna(self, request, queryset):
        util = BalikovnaUtil()
        util.load_data()

    @admin.action(description='Aktualizovat pobočky České pošty')
    def loadCeskaPosta(self, request, queryset):
        util = CeskaPostaUtil()
        util.load_data()

    @admin.action(description='Aktualizovat pobočky Zásilkovny')
    def loadZasilkovna(self, request, queryset):
        util = ZasilkovnaUtil()
        util.load_data()

    @admin.action(description='Aktualizovat pobočky DPD')
    def loadDpd(self, request, queryset):
        util = DpdUtil()
        util.load_data()

    @admin.action(description='Aktualizovat pobočky PPL')
    def loadPPL(self, request, queryset):
        util = BalikobotPPLUtil()
        util.load_data()


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch_type', 'address', 'city', 'zip', 'country', 'latitude', 'longitude',
                    'opening_hours_render')
    search_fields = ('name', 'address', 'city', 'zip')

    list_filter = ['branch_type']

    @admin.display(description='Opening hours')
    def opening_hours_render(self, obj):
        txt = ''
        opening_hours = obj.openning_hours
        for day in opening_hours:
            txt += f'{day}: '
            tmp = []
            if opening_hours[day] == []:
                tmp.append('closed')
            else:
                for hour in opening_hours[day]:
                    tmp.append(f"{hour['open']}-{hour['close']}")
            txt += ', '.join(tmp)
            txt += '<br>'

        return mark_safe(txt)
