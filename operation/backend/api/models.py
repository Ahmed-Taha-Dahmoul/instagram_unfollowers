from django.db import models
from django.contrib.auth.models import User

class InstagramUser_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to Django User model
    user1_id = models.CharField(max_length=100, unique=True)
    session_id = models.CharField(max_length=255)
    csrftoken = models.CharField(max_length=255)
    x_ig_app_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)  # Return the username as a string representation
