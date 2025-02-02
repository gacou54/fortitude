from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils import generate_random_8char


class Collection(models.Model):
    identifier = models.CharField(unique=True, max_length=8, default=generate_random_8char)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, blank=True, null=True)

    created_at = models.DateTimeField(verbose_name=_('Creation date'), auto_now_add=True)
    last_update = models.DateTimeField(verbose_name=_('Last update date'), auto_now=True)


class Study(models.Model):
    patient_name = models.CharField(max_length=128, blank=True, null=True)
    patient_id = models.CharField(max_length=128, blank=True, null=True)
    patient_birth_date = models.CharField(max_length=12, blank=True, null=True)
    patient_sex = models.CharField(max_length=32, blank=True, null=True)

    study_uid = models.CharField(unique=True, max_length=128)
    study_id = models.CharField(max_length=32, blank=True, null=True)
    study_date = models.CharField(max_length=16, blank=True, null=True)
    study_time = models.CharField(max_length=52, blank=True, null=True)
    study_description = models.CharField(max_length=128, blank=True, null=True)
    accession_number = models.CharField(max_length=32, blank=True, null=True)
    referring_physician_name = models.CharField(max_length=128, blank=True, null=True)

    created_at = models.DateTimeField(verbose_name=_('Creation date'), auto_now_add=True)
    last_update = models.DateTimeField(verbose_name=_('Last update date'), auto_now=True)


class Series(models.Model):
    modality = models.CharField(max_length=32, blank=True, null=True)
    series_description = models.CharField(max_length=128, blank=True, null=True)

    series_uid = models.CharField(unique=True, max_length=128)
    series_number = models.IntegerField(blank=True, null=True)
    body_part_examined = models.CharField(max_length=32, blank=True, null=True)

    study = models.ForeignKey(Study, on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name=_('Creation date'), auto_now_add=True)
    last_update = models.DateTimeField(verbose_name=_('Last update date'), auto_now=True)
