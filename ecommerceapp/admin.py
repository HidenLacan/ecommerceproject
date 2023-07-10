from django.contrib import admin
from .models import products,order
# Register your models here.
admin.site.site_header= "E-commerce Site"
admin.site.site_title ="ABC Shopping"
admin.site.index_title ="Manage ABC Shoppin"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','discount_price','category','price','description')
    search_fields = ('category',)
    list_editable = ('price',)
class orderAdmin(admin.ModelAdmin):
    list_display = ('name','email','dire','city','state','items','total')
    list_editable = ('items',)


admin.site.register(products,ProductAdmin)
admin.site.register(order,orderAdmin)