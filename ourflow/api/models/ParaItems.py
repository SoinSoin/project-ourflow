from django.db import models
from .Items import Item
from .Paragraphs import Paragraph

class ParaItem(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='para_item_para')
    item =  models.ForeignKey(Item, on_delete=models.CASCADE, related_name='para_item_item')
    def __str__(self):
        return "{} : {} ".format(self.paragraph, self.item)
    class Meta:
        ordering = ('paragraph',)