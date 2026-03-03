from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.shortcuts import render, redirect

from courses.models import Course, Enrollment

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

@login_required
def profile_view(request):
    user = request.user

    enrolled_courses = None
    created_courses = None

    if user.role == "student":
        enrolled_courses = Enrollment.objects.filter(
            student=user,
            is_active=True,
        ).select_related('course')

    elif user.role == "instructor":
        created_courses = Course.objects.filter(instructor=user)

    context = {
        "user": user,
        "enrolled_courses": enrolled_courses,
        "created_courses": created_courses,
    }

    return render(request, "core/profile.html", context)
