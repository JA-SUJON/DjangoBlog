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

class articleModel(admin.ModelAdmin):
    list_display  = ["__str__","posted_on"]
    search_fields = ["__str__","details"]
    list_filter   = ["posted_on","category"]
    list_per_page = 10
    class Meta:
        Model = Article

admin.site.register(Article,articleModel)