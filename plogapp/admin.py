from django.contrib import admin
from .models import post
# Register your models here.

class postadmin(admin.ModelAdmin):
    list_display =(
        "title",
        "author",
        "body",
    )

admin.site.register(post,postadmin)



 