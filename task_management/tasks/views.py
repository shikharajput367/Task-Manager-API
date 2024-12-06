from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .models import Task, GoogleOAuth, Invitation
from .forms import TaskForm, GoogleOAuthForm, InvitationForm
from .utils import send_invite_email, validate_registration_token

# Logout view
def logout_view(request):
    logout(request)
    return redirect('/')

# Home view for logged-in users
@login_required
def home(request):
    return render(request, 'home.html')

# View to list tasks assigned to the current user
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

# View to display task details
@login_required
def task_detail(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    return render(request, 'task_detail.html', {'task': task})

# View to add a new task
@login_required
def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully.')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

# View to edit an existing task
@login_required
def task_edit(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

# View to delete a task
@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})

# Admin panel for managing Google OAuth keys and sending invitations
@login_required
def admin_panel(request):
    if request.user.is_staff:  # Ensure the user is an admin
        google_oauth_keys = GoogleOAuth.objects.all()
        invitation_form = InvitationForm()
        google_oauth_key_form = GoogleOAuthForm()

        if request.method == 'POST':
            if 'add_oauth_key' in request.POST:
                google_oauth_key_form = GoogleOAuthForm(request.POST)
                if google_oauth_key_form.is_valid():
                    google_oauth_key_form.save()
                    messages.success(request, 'Google OAuth key added successfully.')
                else:
                    messages.error(request, 'There was an error adding the Google OAuth key.')

            elif 'send_invite' in request.POST:
                invitation_form = InvitationForm(request.POST)
                if invitation_form.is_valid():
                    send_invite_email(request, invitation_form.cleaned_data['email'])
                    messages.success(request, f'Invitation email sent to {invitation_form.cleaned_data["email"]}')
                else:
                    messages.error(request, 'Please provide a valid email address.')

        return render(request, 'admin_panel.html', {
            'google_oauth_keys': google_oauth_keys,
            'invitation_form': invitation_form,
            'google_oauth_key_form': google_oauth_key_form,
        })
    else:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('home')

# Registration view using a token (to validate invitation)
def register(request, token):
    user = validate_registration_token(token)
    if not user:
        messages.error(request, 'Invalid or expired registration link.')
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account successfully created!')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
