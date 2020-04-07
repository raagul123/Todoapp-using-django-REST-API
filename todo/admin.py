from django.contrib import admin
from todo import models
admin.site.register(models.UserProfile)
admin.site.register(models.TodoItem)
