from django.db import models
from api.models import Type

class Paragraph(models.Model):
    title_section = models.CharField(max_length=30, db_index=True, null=True, blank=True)
    order_para = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ('order_para',)