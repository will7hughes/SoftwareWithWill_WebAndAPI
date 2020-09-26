from django.db import models

# updated_date is required by the Kotlin app
# It is used to determine if the local Room database 
# needs to update any of it's existing items
class BaseModel(models.Model):
	# auto_now will set when initially created
	# and everytime the save method is called
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True