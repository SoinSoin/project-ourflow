from django.db import models
from .Pages import Page
from .Paragraphs import Paragraph

class PagePara(models.Model):
        page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name= 'page_para_page' )
        paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE,related_name='page_para_para')

        def __str__(self):
            return "{} : {} ".format(self.page, self.paragraph)
        class Meta:
            ordering = ('page',)
        