from django.contrib import admin
from .models import Product
from .models import Orders
# Register your models here.

admin.site.site_header = "Shopping"
admin.site.site_title="E-commerce"
admin.site.index_title="Shopping Managment"

class Productadmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category='device')

    change_category_to_default.short_description='Default Category'
    list_display=('title','category','price','description',)
    search_fields=('title','category',)
    actions =('change_category_to_default',)
    fields=('title','price')
    list_editable=('description','price')

admin.site.register(Product,Productadmin)
admin.site.register(Orders)
