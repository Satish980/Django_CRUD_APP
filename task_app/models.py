from django.db import models

# Create your models here.

class UserDetails(models.Model):
	#"id" serial NOT NULL PRIMARY KEY,
	username = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 100,unique = True)
	password = models.CharField(max_length = 20)
	address = models.CharField(max_length = 200)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.username +" "+ self.email + " "+self.password+ " " + self.address