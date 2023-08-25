from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html
from django.templatetags.static import static

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display =['title', 'description', 'price', 'created_date', 'updated_date', 'category', 'author', 'location', 'auction', 'photo_preview']
    list_filter = ['price', 'created_at', 'updated_at', 'category']
    actions = ['forbid_the_auction', 'permit_the_auction']
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description', 'category', 'user', 'location', 'photo')
        }),
        ('Финансы', {
            'fields' : ('price', 'auction'),
            'classes' : ['collapse']
        })
    )

    @admin.display(description='Photo Preview')
    def photo_preview(self, object):
        if object.photo: 
            return format_html('<img src="{}" width="100" height="auto" />', object.photo.url)
        else:
            default_image = static('img/adv.png')  
            return format_html('<img src="{}" width="100" height="auto" />', default_image)

    @admin.action(description="Убрать возможность торга.")
    def forbid_the_auction(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга.")
    def permit_the_auction(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)