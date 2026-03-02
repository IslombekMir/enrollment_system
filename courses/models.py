from django.db import models
from users.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="courses"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        db_index=True
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['order']
        constraints = [
	        models.UniqueConstraint(
	            fields=['course', 'order'],
	            name='unique_lesson_order_per_course'
	        )
	    ]

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Enrollment(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments",
        db_index=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'],
                name='unique_enrollment'
            )
        ]

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"