from django.db import models

class Page(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True,)
    title_page = models.CharField(max_length=30, db_index=True, null=True, blank=True,)
    order_page = models.PositiveIntegerField(null=True, blank=True, db_index=True,unique=True)

    def __str__(self):
        return self.title_page
    
    class Meta:
        ordering = ('order_page',)