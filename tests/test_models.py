import pytest
from django.contrib.auth import get_user_model
from courses.models import Course, Enrollment

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username="student1", password="pass")
    assert user.username == "student1"


@pytest.mark.django_db
def test_create_course():
    instructor = User.objects.create_user(username="inst1", password="pass", role="instructor")

    course = Course.objects.create(
        title="Python Course",
        description="Learn Python",
        instructor=instructor
    )

    assert course.title == "Python Course"
    assert course.instructor.username == "inst1"


@pytest.mark.django_db
def test_enrollment_creation():
    instructor = User.objects.create_user(username="inst2", password="pass", role="instructor")
    student = User.objects.create_user(username="stud2", password="pass")

    course = Course.objects.create(
        title="Django Course",
        description="Learn Django",
        instructor=instructor
    )

    enrollment = Enrollment.objects.create(
        student=student,
        course=course
    )

    assert enrollment.student.username == "stud2"
    assert enrollment.course.title == "Django Course"
    assert enrollment.is_active is True


@pytest.mark.django_db
def test_unique_enrollment_constraint():
    instructor = User.objects.create_user(username="inst3", password="pass", role="instructor")
    student = User.objects.create_user(username="stud3", password="pass")

    course = Course.objects.create(
        title="DevOps",
        description="Learn DevOps",
        instructor=instructor
    )

    Enrollment.objects.create(student=student, course=course)

    with pytest.raises(Exception):
        Enrollment.objects.create(student=student, course=course)