from .models import Course, Enrollment, User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {
        "courses": courses
    })

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    is_enrolled = Enrollment.objects.filter(student=request.user, course=course, is_active=True).exists()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'is_enrolled': is_enrolled,
    })

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    Enrollment.objects.update_or_create(
        student=request.user,
        course=course,
        defaults={'is_active': True}
    )
    
    return redirect('courses:course_detail', pk=course.id)

@login_required
def unenroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.filter(student=request.user, course=course).update(is_active=False)
    return redirect('core:profile')

@login_required
def course_create(request):
    if request.user.role != "instructor":
        return redirect("core:index")
    
    course = None

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect("courses:course_list")
    else:
        form = CourseForm()

    return render(request, "courses/course_form.html", {"form": form, "course": course})

@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.user != course.instructor:
        return redirect("courses:course_list")

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("courses:course_list")
    else:
        form = CourseForm(instance=course)

    return render(request, "courses/course_form.html", {"form": form})

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.user != course.instructor:
        return redirect("courses:course_list")

    if request.method == "POST":
        course.delete()
        return redirect("courses:course_list")

    return render(request, "courses/course_confirm_delete.html", {"course": course})
