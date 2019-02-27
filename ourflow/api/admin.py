from django.contrib import admin
from .models import * 

admin.site.register(Page)
admin.site.register(Item)
admin.site.register(Type)
admin.site.register(Paragraph)
admin.site.register(PagePara)
admin.site.register(ParaItem)