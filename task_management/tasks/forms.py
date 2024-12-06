from django import forms
from .models import Task, GoogleOAuth, Invitation
from django.utils import timezone
from datetime import timedelta

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class GoogleOAuthForm(forms.ModelForm):
    class Meta:
        model = GoogleOAuth
        fields = ['client_id', 'client_secret', 'redirect_uri']

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['email', 'token', 'expiration_time']

    def clean_expiration_time(self):
        """Ensure the expiration time is not in the past."""
        expiration_time = self.cleaned_data.get('expiration_time')
        if expiration_time < timezone.now():
            raise forms.ValidationError("Expiration time cannot be in the past.")
        return expiration_time

    def save(self, *args, **kwargs):
        """Override save to set expiration time if not provided."""
        if not self.instance.expiration_time:
            self.instance.expiration_time = timezone.now() + timedelta(hours=24)
        return super().save(*args, **kwargs)
