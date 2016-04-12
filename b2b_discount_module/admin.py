from django.contrib import admin
from b2b_discount_module.models import Agreement, Company, Country

class AgreementAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'end_date', 'negotiator', 'export_value', 'import_value']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'country']

class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_name']

admin.site.register(Agreement, AgreementAdmin)

admin.site.register(Company, CompanyAdmin)

admin.site.register(Country, CountryAdmin)
