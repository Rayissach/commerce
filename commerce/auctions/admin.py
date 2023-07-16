from django.contrib import admin
from django .contrib.auth.admin import UserAdmin
from .models import User, Listing, Bids, Comments

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Listing)
admin.site.register(Bids)
admin.site.register(Comments)

