from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    """Model to represent tasks assigned to users."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class GoogleOAuth(models.Model):
    """Model to store Google OAuth credentials."""
    client_id = models.CharField(max_length=255, unique=True)
    client_secret = models.CharField(max_length=255)
    redirect_uri = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OAuth Client: {self.client_id}"

    class Meta:
        verbose_name = "Google OAuth Credential"
        verbose_name_plural = "Google OAuth Credentials"


class Invitation(models.Model):
    """Model to represent an invitation with a token and expiration time."""
    email = models.EmailField()
    token = models.CharField(max_length=255, unique=True)
    expiration_time = models.DateTimeField()

    def is_expired(self):
        """Check if the invitation token has expired."""
        return self.expiration_time < timezone.now()

    def __str__(self):
        return f"Invitation to {self.email}"

    class Meta:
        verbose_name = 'Invitation'
        verbose_name_plural = 'Invitations'
