# coding=utf-8
from __future__ import unicode_literals

from authtools.models import AbstractEmailUser
from django.db import models
from django.utils.functional import cached_property
from accounts.const import *


class User(AbstractEmailUser):
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES,
        default=USER_TYPE_COMPANY)

    @cached_property
    def is_company_type(self):
        return self.user_type == USER_TYPE_COMPANY
