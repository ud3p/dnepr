from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import json
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver

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

    country_id = models.PositiveIntegerField("Country Name", 
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

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Start date cannot precede end date')


    def save(self, *args, **kwargs):
        super(Agreement, self).save(*args, **kwargs)

    def __unicode__(self):
        return 'Agreement to %s' % self.company


class Period(models.Model):
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    choose_period = models.ForeignKey(Agreement)

    def clean(self):
        cleaned_data = super(Period, self).clean()
        cc_myself = cleaned_data.get("period_start_date")
        print cc_myself
        try:
            l = str(Period.objects.last()).split(' / ')
            print l
            temp_date = datetime.datetime.strptime(l[1], "%Y-%m-%d").date()
            print self.period_start_date, Period.objects.count(), Period.objects.values('choose_period_id')[0]
            print 'temp date', temp_date

            dict_id = Period.objects.values('choose_period_id')[0]
            agree = Agreement.objects.get(id=dict_id['choose_period_id'])
            print dict_id, agree, agree.start_date

            if agree.start_date > self.period_start_date:
                raise ValidationError('Period start date cannot precede Agreement start date')

            if self.period_start_date > self.period_end_date:
                raise ValidationError('Period start date cannot precede period end date')
            '''
            if temp_date > self.period_start_date and Period.objects.count() < 100:
                print 'False'
                raise ValidationError('Periods should not overlap')

            if Period.objects.count() >= 1 and self.period_start_date < temp_date:
                print temp_date
                raise ValidationError('Periods should not overlap')
            '''
        except IndexError:
            pass


    def save(self, *args, **kwargs):
        #print self.period_start_date, Period.objects.count(), Period.objects.values()
        super(Period, self).save(*args, **kwargs)


    def __unicode__(self):
        return '%s / %s' % (self.period_start_date, self.period_end_date)

