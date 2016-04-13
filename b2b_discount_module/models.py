from django.db import models
from django.contrib.auth.models import User
import json

'''
import json
import bs4
import requests
with open('data.txt', 'w') as outfile:
    #json.dump(data, outfile)

    json.dump(
     [   {
            ['name', 'alpha_2', 'alpha_3', 'numeric'][no]:
            td.find_all()[-1].text
            for no, td in enumerate(row.find_all('td')[:-1])
        }
        for row in bs4.BeautifulSoup(
            requests.get('http://en.wikipedia.org/wiki/ISO_3166-1').text
        ).find('table', {'class': 'wikitable sortable'}).find_all('tr')[1:]
    ],
    outfile,
    indent=2,
    encoding="utf-8"
    
    )
'''

class Country(models.Model):

    fp_json = json.load(open('b2b_discount_module/data.json'))

    country_id = models.PositiveIntegerField(
                                   max_length=255,
                                   choices=[
                                           (ident, country['name'])
                                           for ident, country in enumerate(fp_json)
                                        ]
                                   )

    country_iso = models.CharField(max_length=3, help_text="This field fill automatically!", blank=True, null=True)

    country_disp = models.CharField("Country Name", max_length=255, help_text="This field fill automatically!", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.country_iso = self.fp_json[self.country_id]['alpha_3']
        self.country_disp = self.fp_json[self.country_id]['name']
        super(Country, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return '%s' % self.fp_json[int(self.country_id)]['name']

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



    

