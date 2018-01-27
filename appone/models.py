# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#
#
# class Publisher(models.Model):
#     name = models.CharField(max_length=300)
#     num_awards = models.IntegerField()
#
# class Book(models.Model):
#     name = models.CharField(max_length=300)
#     pages = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     rating = models.FloatField()
#     authors = models.ManyToManyField(Author)
#     publisher = models.ForeignKey(Publisher)
#     pubdate = models.DateField()
#
# class Store(models.Model):
#     name = models.CharField(max_length=300)
#     books = models.ManyToManyField(Book)
#     registered_users = models.PositiveIntegerField()


# class Publication(models.Model):
#     title = models.CharField(max_length=30)
#
#     # On Python 3: def __str__(self):
#     def __unicode__(self):
#         return self.title
#
#     class Meta:
#         ordering = ('title',)
#
#
# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)
#
#     # On Python 3: def __str__(self):
#     def __unicode__(self):
#         return self.headline
#
#     class Meta:
#         ordering = ('headline',)




class Assets(models.Model):
    assets_type_choices = (
        ('server', u'服务器'),
        ('vmser', u'虚拟机')
    )

    assets_type = models.CharField(choices=assets_type_choices, max_length=100, default='server', verbose_name='资产类型')