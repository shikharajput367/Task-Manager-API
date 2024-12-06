import uuid
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta
from .models import Invitation

def generate_invite_token():
    """Generate a unique token for the invitation."""
    return str(uuid.uuid4())

def send_invite_email(request, email):
    """Send an invitation email with a registration link."""
    # Generate token and store it in the database
    token = generate_invite_token()
    expiration_time = now() + timedelta(hours=24)
    
    Invitation.objects.create(email=email, token=token, expiration_time=expiration_time)

    registration_link = f"{request.scheme}://{request.get_host()}/register/{token}/"
    subject = 'Invitation to Join Task Manager'
    message = f"Click the following link to complete your registration: {registration_link}"

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return True
    except BadHeaderError:
        return False
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

def validate_registration_token(token):
    """Validate if the registration token exists and is not expired."""
    try:
        invitation = Invitation.objects.get(token=token)
        if invitation.is_expired():
            return None
        return invitation
    except Invitation.DoesNotExist:
        return None
