from django.db import models
from auth_app.models import User


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_time = models.DateTimeField(auto_now_add=True)
