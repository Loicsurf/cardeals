from email.mime import image
from django.db import models
from django.utils import timezone

class Cars(models.Model):
	cars_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	extra1 = models.CharField(max_length=50, null = True, blank=True)
	extra2 = models.CharField(max_length=50, null = True, blank=True)
	extra3 = models.CharField(max_length=50, null = True, blank=True)
	extra4 = models.CharField(max_length=50, null = True, blank=True)
	extra5 = models.CharField(max_length=50, null = True, blank=True)
	extra6 = models.CharField(max_length=50, null = True, blank=True)
	extra7 = models.CharField(max_length=50, null = True, blank=True)
	extra8 = models.CharField(max_length=50, null = True, blank=True)
	extra9 = models.CharField(max_length=50, null = True, blank=True)
	extra10 = models.CharField(max_length=50, null = True, blank=True)
	type = models.CharField(max_length=20)
	price = models.IntegerField()
	initial_price = models.IntegerField()
	down_payment = models.IntegerField()
	stock = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	image1 = models.FileField(null = True, blank=True)
	image2 = models.FileField(null = True, blank=True)
	image3 = models.FileField(null = True, blank=True)

	def __str__(self):
		return str(self.name)
