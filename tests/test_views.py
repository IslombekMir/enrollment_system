import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from courses.models import Course, Enrollment

User = get_user_model()


@pytest.mark.django_db
def test_course_list_view(client):
    response = client.get(reverse("courses:course_list"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_enroll_course_view(client):
    instructor = User.objects.create_user(username="inst4", password="pass", role="instructor")
    student = User.objects.create_user(username="stud4", password="pass")

    course = Course.objects.create(
        title="Algorithms",
        description="Algo course",
        instructor=instructor
    )

    client.login(username="stud4", password="pass")

    response = client.get(reverse("courses:enroll_course", args=[course.id]))

    assert response.status_code == 302
    assert Enrollment.objects.filter(student=student, course=course).exists()
