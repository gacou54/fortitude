from django.contrib.auth.models import Group, User
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.collections.models import Collection
from .utils import generate_token


class UserCollection(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name=_('Creation date'), auto_now_add=True)


class GroupCollection(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name=_('Creation date'), auto_now_add=True)


class Token(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    secret = models.CharField(max_length=36, default=generate_token)

    read_permission = models.BooleanField(default=False)
    write_permission = models.BooleanField(default=False)
    download_permission = models.BooleanField(default=False)

    expiration_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=_('Creation date'), auto_now_add=True)

    last_used = models.DateTimeField(blank=True, null=True)
    revoked_time = models.DateTimeField(blank=True, null=True)

    revoked_by_user_fk = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
