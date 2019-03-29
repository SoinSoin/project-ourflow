from django.db import models

class Type(models.Model):
    name_type = models.CharField(max_length=30, db_index=True, null=True)

    def __str__(self):
        return self.name_type
    