from django.db import models

class License(models.Model):
	user = models.CharField(max_length=50)
	company_name = models.CharField(max_length=250)
	serial = models.CharField(max_length=50)
	valid_date = models.DateField()