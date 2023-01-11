from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.apartments_property.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    list_editable = ('new_building',)
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
    )
    raw_id_fields = ('likes',)

    inlines = [
        OwnerInline,
    ]


class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'flat',
        'text',
    )
    raw_id_fields = ('user', 'flat',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('apartment_owner',)
    raw_id_fields = ('apartments_property',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
