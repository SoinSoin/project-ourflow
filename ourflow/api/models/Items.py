from django.db import models

class Item(models.Model):
    title_item = models.CharField(max_length=30, db_index=True, null=True, blank=True,)
    descritpion_item = models.TextField(null=True, blank=True,)
    media_item = models.FileField(null=True, blank=True, upload_to='uploads',)
    link_item = models.CharField(max_length=200, db_index=True, null=True, blank=True,)
    alt_item =  models.CharField(max_length=500, db_index=True, null=True, blank=True,)
    order_item = models.PositiveIntegerField(null=True, blank=True, db_index=True,)
    
    class Meta:
        ordering = ('order_item',)

print(Item)