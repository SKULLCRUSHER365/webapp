from django.contrib import admin

from .models import compounds, itemlist, vendor,selection,currency
# Register your models here.
admin.site.register(selection)
admin.site.register(vendor)
admin.site.register(compounds)
admin.site.register(currency)
admin.site.register(itemlist)