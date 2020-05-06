from django.contrib import admin
from . models import Author,Category,Article
# Register your models here.

class authorModel(admin.ModelAdmin):
    list_display  = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        Model = Author
admin.site.register(Author , authorModel)
admin.site.register(Category)
admin.site.register(Article)
