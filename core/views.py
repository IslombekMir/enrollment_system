from django.contrib.auth import login
from .forms import SignUpForm
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'core/index.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect("core:index")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {"form": form})
