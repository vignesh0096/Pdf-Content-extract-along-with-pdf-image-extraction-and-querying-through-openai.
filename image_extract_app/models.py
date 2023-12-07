from django.db import models


class Pdfs(models.Model):
    pdf = models.FileField(null=True,blank=True)