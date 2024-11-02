from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Bids, Contact, Financials

admin.site.register(Contact) 

@admin.register(Bids)
class BidsAdmin(ImportExportModelAdmin):
    pass

"""
admin.site.register(Menu)

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    pass
"""

@admin.register(Financials)
class ItemAdmin(ImportExportModelAdmin):
    pass