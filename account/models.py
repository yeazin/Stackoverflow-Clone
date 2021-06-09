from django.db import models
from django.contrib.auth.models import User
import uuid

# Question user
class Quser(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(unique=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_naem = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


    



