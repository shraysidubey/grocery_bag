from django.contrib import admin

from gro_app.models import UserProfile, GroceryItem

admin.site.register(UserProfile)

admin.site.register(GroceryItem)