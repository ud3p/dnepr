from django.contrib import admin
from b2b_discount_module.models import Agreement, Company, Country

class AgreementAdmin(admin.ModelAdmin):
    list_settings_agreement = ['company', 'start_date', 'end_date', 'negotiator', 'export_value', 'import_value']
    list_display = list_settings_agreement
    list_filter = list_settings_agreement
    search_fields = list_settings_agreement

class CompanyAdmin(admin.ModelAdmin):
    list_settings_company = ['company_name', 'country']
    list_display = list_settings_company
    list_filter = list_settings_company
    search_fields = list_settings_company

class CountryAdmin(admin.ModelAdmin):
    list_settings_country = ['country_disp', 'country_iso']
    list_display = list_settings_country
    readonly_fields = list_settings_country
    list_filter = list_settings_country
    search_fields = list_settings_country


admin.site.register(Agreement, AgreementAdmin)

admin.site.register(Company, CompanyAdmin)

admin.site.register(Country, CountryAdmin)
