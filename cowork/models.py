from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import smart_unicode


class Address(models.Model):
    street = models.CharField(max_length=100)
    street_numer = models.CharField(max_length=10)
    city = models.CharField(max_length=200)
    post_numer = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.street, self.street_numer)


class Vat(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    vat = models.FloatField()

    def __str__(self):
        return '%s' % (self.vat)


class Company(models.Model):
    user = models.ForeignKey('accounts.User',
                             related_name='companies')
    name = models.CharField(max_length=100)
    website = models.URLField()
    logo = models.ImageField()
    vat_id = models.ForeignKey(Vat)

    def __unicode__(self):
        return smart_unicode(" ".join([self.name, str(self.logo)]))


class Location(models.Model):
    company = models.ForeignKey('Company',
        related_name='locations')
    address = models.ForeignKey(Address)
    city = models.CharField(max_length=200)
    total_desks = models.IntegerField(verbose_name='Total desks')
    reserved_desks = models.IntegerField(verbose_name='Reserved desks')
    price = models.DecimalField(verbose_name='Price per desk $',
        max_digits=12, decimal_places=2)

    def __unicode__(self):
        return '%s' % self.city

    @property
    def free_desks(self):
        return self.total_desks - self.reserved_desks


class Desk(models.Model):
    owner = models.OneToOneField('accounts.User', related_name='desks',
        null=True)
    location = models.OneToOneField(Location, related_name='desks')
    rent_start_date = models.DateTimeField(null=True)
    rent_end_date = models.DateTimeField(null=True)

    def __unicode__(self):
        return '%s' % self.location
