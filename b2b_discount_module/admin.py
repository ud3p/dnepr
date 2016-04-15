from django.contrib import admin
from b2b_discount_module.models import Agreement, Company, Country, Period

class PeriodInline(admin.TabularInline):
    model = Period
    extra = 1


class AgreementAdmin(admin.ModelAdmin):
    list_settings_agreement = ['company', 'start_date', 'end_date', 'negotiator', 'export_value', 'import_value']
    list_display = list_settings_agreement
    list_filter = list_settings_agreement
    search_fields = list_settings_agreement
    inlines = [PeriodInline]

class CompanyAdmin(admin.ModelAdmin):
    list_settings_company = ['company_name', 'country']
    list_display = list_settings_company
    list_filter = list_settings_company
    search_fields = list_settings_company

class CountryAdmin(admin.ModelAdmin):
    list_settings_country = ['country_disp', 'country_iso']
    list_display = list_settings_country
    readonly_fields = ['country_iso']
    list_filter = list_settings_country
    search_fields = list_settings_country
    exclude = ['country_disp']

class PeriodAdmin(admin.ModelAdmin):
    list_settings_period = ['period_start_date', 'period_end_date', 'is_active']
    list_display = list_settings_period
    list_filter = list_settings_period
    search_fields = list_settings_period

admin.site.register(Agreement, AgreementAdmin)

admin.site.register(Company, CompanyAdmin)

admin.site.register(Country, CountryAdmin)

admin.site.register(Period, PeriodAdmin)
