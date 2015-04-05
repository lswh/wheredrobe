from django.db import models

# Create your models here.
class Clothingplain(models.Model):
	name = models.CharField(max_length=200)
	#Choice Fields for Status of Clothing Item
	CABINET = 'CB'
	REPAIRSHOP = 'RS'
	HAMPER = 'H'
	LAUNDRYSHOP = 'LS'
	MISSING = 'M'
	DONATION = 'D'
	status_choices = (
		(CABINET,'In the Cabinet'),
		(REPAIRSHOP,'Under Alterations'),
		(HAMPER,'In the Hamper'),
		(LAUNDRYSHOP,'At the Laundry Shop'),
		(DONATION, 'For Donation or Charity')
		(MISSING,'Missing'),
		)
	itemstatus = models.CharField(max_length=2, choices=status_choices, default=CABINET)
	#Picture upload for clothing
	picture = models.ImageField(default=None)
	#Choice Fields for Clothing Type Listing
	UNDERWEAR = 'UW'
	#Top and bottom basic but needs to be broken down further
	TOP = 'T'
	BOTTOM = 'B'
	DRESS = 'D'
	FOOTWEAR = 'FW'
	MISC = 'MI'

	clothingtype_choices = (
		(TOP,'Shirts or Tops or Polos'),
		(BOTTOM,'Skirts or Shorts or Pants'),
		(FOOTWEAR,'Footwear'),
		(DRESS,'Dresses or Onesies'),
		(MISC,'Miscellaneous'),
		)
	clothing_type = models.CharField(max_length=2, choices=clothingtype_choices, default=TOP)

	def __str__(self):
		return self.name

# class Clothingeotagged(models.Model):

# class LaundryShopPOI:

# class AlterShopPOI: