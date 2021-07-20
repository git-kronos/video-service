from django.contrib import admin

# Register your models here.
from memberships.models import Membership, UserMembership, Subscription

admin.site.register(Membership)
admin.site.register(UserMembership)
admin.site.register(Subscription)
