from django.db import models
from .Types import Type

class Paragraph(models.Model):
    title_para = models.CharField(max_length=30, db_index=True, null=True, blank=True)
    order_para = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE,related_name='para_type')

    def __str__(self):
        return self.title_para
    
    class Meta:
        ordering = ('order_para',)