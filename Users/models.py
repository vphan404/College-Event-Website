from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
def defaultUser():
    default = User.objects.first()

    if default is None:
        default = User.objects.create_user('defaultUser', password='djangoproject')

    return default


# def defaultProfile():
#   default = Profile.objects.first()

#   if default is None:
#     default = Profile.objects.create_profile()
  
#   return default


class User(AbstractUser):
  is_admin = models.BooleanField(default=False) 
  is_super_admin = models.BooleanField(default=False) 
  # profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default=defaultProfile())


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.png', upload_to='profile_pics')

  def __str__(self):
    return f'{self.user.username} Profile'

  def save(self, **kwargs):
    super().save()

    image = Image.open(self.image.path) 

    if image.width > 300 or image.height > 300:
      output_size = (300, 300) 
      image.thumbnail(output_size)
      image.save(self.image.path)



