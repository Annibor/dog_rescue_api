from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
  """
  Extends the base User model to store additional personal information about users.

  Attributes:
    user (OneToOneField): A one-to-one link to Django's built-in User model, ensuring
        that each user has one associated profile.
    first_name (CharField): The user's first name.
    last_name (CharField): The user's last name.
    email (EmailField): The user's email address, must be unique across all users.
    phone_number (CharField): An optional field for the user's phone number, can be blank.
    liked_dogs (ManyToManyField): Represents a many-to-many relationship allowing
        users to 'like' multiple dogs. Each dog can likewise be liked by multiple users.

  Methods:
    __str__: Returns a string representation of the UserProfile, which includes the
        associated user's username.
  """
  user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=60)
  email = models.EmailField(unique=True, blank=False)
  phone_number = models.CharField(max_length=20, blank=True, null=True)
  liked_dogs = models.ManyToManyField('Dog', related_name='liked_by_users')
  
  def __str__(self):
        return f"{self.user}'s profile"

