from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from .forms import LoginForm
from .models import Profile

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        user, is_new = User.objects.get_or_create(username=username)
        if is_new:
            Profile.objects.create(user=user) # automatically creating profile instance
            user.set_unusable_password() # marks the user as having no password set
            user.email = form.cleaned_data.get('mail')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()

        login(self.request, user)
        return redirect('index') # TODO: should be replaced, when home view is ready


class LogoutView(LogoutView):
    next_page = 'login'

# TODO: should be replaced, when home view is ready
@login_required
def index(request):
    return render(request, 'index.html')
