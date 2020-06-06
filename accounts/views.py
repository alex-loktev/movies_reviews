from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'accounts/registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
        return render(request, 'accounts/registration.html', {'form': form})
