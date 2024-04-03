from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Bids, Contact, Menu, Item

admin.site.register(Contact) 

@admin.register(Bids)
class BidsAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Menu)

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    pass