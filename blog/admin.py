from django.contrib import admin
from .models import Blog, Document, Hashtag
# Register your models here.

admin.site.register(Blog)
admin.site.register(Document)
admin.site.register(Hashtag)
