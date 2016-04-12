from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    country_iso = models.CharField(max_length=3, choices=(('M', 'Male'), ('F', 'Female')))
    country_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.country_name

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    country = models.OneToOneField(Country, blank=True, null=True)

    def __unicode__(self):
        return self.company_name

class Agreement(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    company = models.OneToOneField(Company, blank=True, null=True)
    negotiator = models.OneToOneField(User, blank=True, null=True)
    export_value = models.PositiveIntegerField()
    import_value = models.PositiveIntegerField()

    def __unicode__(self):
        return 'Agreement %s' % self.company



    

