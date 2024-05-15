from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Dog(models.Model):
  """
  Represents a dog available for adoption.
  
  Attributes:
    name (CharField): The dog's name.
    breed (CharField): The dog's breed.
    age (IntegerField): The dog's age in years.
    featured_image (CloudinaryField): An image of the dog, stored externally via Cloudinary.
    description (TextField): A detailed description of the dog.
    gender (CharField): The gender of the dog.
    good_with_children (BooleanField): True if the dog is known to be good with children, False otherwise.
    adoption_status (CharField): The current adoption status of the dog, with choices of 'available', 'pending', or 'adopted'.
    """
  name = models.CharField(max_length=80)
  breed = models.CharField(max_length=80)
  age = models.IntegerField()
  featured_image = CloudinaryField('image', default='placeholder')
  description = models.TextField()
  gender = models.CharField(max_length=10)
  good_with_children = models.BooleanField(default=True)
  adoption_status = models.CharField(max_length=20, choices=[('available', 'Available'), ('pending', 'Pending'), ('adopted', 'Adopted')], default='available')


  class Meta:
    """
    Metadata for the Dog model.
    
    Attributes:
      verbose_name: A human-readable name for the model used in the Django admin.
      verbose_name_plural: A human-readable name for the model in plural form.
      ordering: The default sorting order for queries, based on the dog's name.
    
    """
    verbose_name = "Dog"
    verbose_name_plural = "Dogs"
    ordering = ["name"]

  def __str__(self):
     return self.name