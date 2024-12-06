from django.contrib import admin
from .models import GoogleOAuth, Invitation

class GoogleOAuthAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'redirect_uri')

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'token', 'expiration_time')

admin.site.register(GoogleOAuth, GoogleOAuthAdmin)
admin.site.register(Invitation, InvitationAdmin)
