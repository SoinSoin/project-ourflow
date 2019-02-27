from django.db import models

class Type(models.Model):
    name_para = models.CharField(max_length=30, db_index=True, null=True)