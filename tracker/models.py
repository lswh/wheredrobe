from django.db import models

# Create your models here.
class Clothingplain(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

# class Clothingeotagged(models.Model):

# class LaundryShop

# class AlterShop 