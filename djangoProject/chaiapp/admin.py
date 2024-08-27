from django.contrib import admin
from .models import Models, ChaiReview,Stores,ChaiCertificates

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra=2
    
class ModelsAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines = [ChaiReviewInline]
    
class StoresAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal = ('chai_varieties',)
    
class ChaiCertificatesAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')

admin.site.register(Models,ModelsAdmin)
admin.site.register(Stores,StoresAdmin)
admin.site.register(ChaiCertificates,ChaiCertificatesAdmin)
# admin.site.register(ChaiReview,ChaiReviewInline)



