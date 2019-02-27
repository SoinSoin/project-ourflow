from django.db import models
from api.models import Item
from api.models import Paragraph

class ParaItem(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    item =  models.ForeignKey(Item, on_delete=models.CASCADE)