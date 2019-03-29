from django.db import models
from api.assets import file_cleanup_delete, file_cleanup_upload, definer_root

class Item(models.Model):
    title_item = models.CharField(max_length=30, db_index=True, null=True, blank=True,)
    descritpion_item = models.TextField(null=True, blank=True,)
    media_item = models.FileField(upload_to=definer_root, null=True, blank=True)
    link_item = models.CharField(max_length=200, db_index=True, null=True, blank=True,)
    alt_item =  models.CharField(max_length=500, db_index=True, null=True, blank=True,)
    order_item = models.PositiveIntegerField(null=True, blank=True, db_index=True,)

    def __str__(self):
        return self.title_item
    
    class Meta:
        ordering = ('order_item',)


models.signals.pre_save.connect(file_cleanup_upload, sender=Item, dispatch_uid="my_unique")
models.signals.post_delete.connect(file_cleanup_delete, sender=Item, dispatch_uid="my_unique_identifier")
