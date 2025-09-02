from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from decimal import Decimal


# Note: This model design uses a single User with role and small profile tables. 
# You can extend later.

class User(AbstractUser):
    STUDENT = 'student'
    EDUCATOR = 'educator'
    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (EDUCATOR, 'Educator'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)

    def is_student(self):
        return self.role == self.STUDENT

    def is_educator(self):
        return self.role == self.EDUCATOR

class EducatorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"EducatorProfile({self.user.username})"

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    study_level = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"StudentProfile({self.user.username})"

class LearningCircle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    educator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hosted_circles')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='joined_circles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (by {self.educator.username})"

class ChatMessage(models.Model):
    circle = models.ForeignKey(LearningCircle, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    is_from_ai = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Msg({self.sender.username}): {self.content[:40]}"

class Payment(models.Model):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    STATUS_CHOICES = [(PENDING, 'Pending'), (COMPLETED, 'Completed'), (FAILED, 'Failed')]

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    educator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_ref = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Payment({self.student.username} -> {self.educator.username}) {self.amount} [{self.status}]"
