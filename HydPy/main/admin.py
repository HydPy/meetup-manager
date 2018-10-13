from django.contrib import admin

# Register your models here.
from .models import (
    User,
    Speaker,
    Venue,
    RegisteredUser
)

admin.site.register(User)
admin.site.register(Speaker)
admin.site.register(Venue)
admin.site.register(RegisteredUser)
