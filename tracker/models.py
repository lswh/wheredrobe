from django.db import models

# Create your models here.
class Clothingplain(models.Model):
	name = models.CharField(max_length=200)
	#Choice Field for Status of Clothing Item
	CABINET = 'CB'
	REPAIRSHOP = 'RS'
	HAMPER = 'H'
	LAUNDRYSHOP = 'LS'
	MISSING = 'M'
	status_choices = (
		(CABINET,'In the Cabinet'),
		(REPAIRSHOP,'Under Alterations'),
		(HAMPER,'In the Hamper'),
		(LAUNDRYSHOP,'At the Laundry Shop'),
		(MISSING,'Missing'),
		)
	itemstatus = models.CharField(max_length=2, choices=status_choices, default=CABINET)
	picture = models.ImageField()

	def __str__(self):
		return self.name

# class Clothingeotagged(models.Model):

# class LaundryShop

# class AlterShop 