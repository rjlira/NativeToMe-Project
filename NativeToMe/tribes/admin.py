from django.contrib import admin
from .models import Tribe, Posts, JoinRequest, House
# Register your models here.

admin.site.register(Tribe)
admin.site.register(Posts)
admin.site.register(JoinRequest)
admin.site.register(House)