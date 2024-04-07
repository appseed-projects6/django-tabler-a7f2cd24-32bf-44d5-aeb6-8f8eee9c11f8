# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Dimcompany(models.Model):

    #__Dimcompany_FIELDS__
    company = models.CharField(max_length=255, null=True, blank=True)
    company desc = models.CharField(max_length=255, null=True, blank=True)
    program = models.CharField(max_length=255, null=True, blank=True)
    mbu = models.CharField(max_length=255, null=True, blank=True)
    capability = models.CharField(max_length=255, null=True, blank=True)

    #__Dimcompany_FIELDS__END

    class Meta:
        verbose_name        = _("Dimcompany")
        verbose_name_plural = _("Dimcompany")


class Dimitem(models.Model):

    #__Dimitem_FIELDS__
    company = models.CharField(max_length=255, null=True, blank=True)
    item = models.CharField(max_length=255, null=True, blank=True)
    item desc = models.CharField(max_length=255, null=True, blank=True)

    #__Dimitem_FIELDS__END

    class Meta:
        verbose_name        = _("Dimitem")
        verbose_name_plural = _("Dimitem")


class Sales(models.Model):

    #__Sales_FIELDS__
    company = models.CharField(max_length=255, null=True, blank=True)
    order number = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    sold to bp = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    sequence = models.CharField(max_length=255, null=True, blank=True)

    #__Sales_FIELDS__END

    class Meta:
        verbose_name        = _("Sales")
        verbose_name_plural = _("Sales")



#__MODELS__END
