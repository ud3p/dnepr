from django.db import models
from django.contrib.auth.models import User
import pycountry
import csv

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
    indent=4,
    ensure_ascii=False
    
    )


class Country(models.Model):
    with open('b2b_discount_module/country.csv') as county:
        fp_csv = csv.reader(county)
        fp_csv.next()
        #for i in fp_csv:
            #print i[0],i[3]

    country_iso = models.CharField(max_length=3, choices=[(i, k) for i,k in enumerate(range(5))])
    country_name = models.CharField(max_length=255)
    #for i in pycountry.countries:
        #print i
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



    

