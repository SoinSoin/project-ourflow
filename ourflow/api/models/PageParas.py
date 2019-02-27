from django.db import models
from api.models import Page
from api.models import Paragraph
class PagePara(models.Model):
        page = models.ForeignKey(Page, on_delete=models.CASCADE)
        paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE,)