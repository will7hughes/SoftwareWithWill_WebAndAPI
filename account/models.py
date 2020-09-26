from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionsMixin
from personal.models import BaseModel
from django.contrib.auth.models import Group

class UserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if not username:
			raise ValueError("Users must have an username")
		if not email:
			raise ValueError("Users must have an email address")

		user = self.model(
			username = username,
			email = self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, password):

		user = self.create_user(
			username = username,
			email = self.normalize_email(email),
			password = password
		)
		user.is_staff = True
		user.is_admin = True
		user.is_superuser = True

		user.save(using=self._db)
		return user

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
	username = models.CharField(max_length=45, unique=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(unique=True, verbose_name="email", max_length=60)
	date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

	is_active = models.BooleanField(default=True, verbose_name="active")
	is_staff = models.BooleanField(default=True, verbose_name="staff")
	is_admin = models.BooleanField(default=False, verbose_name="admin")
	is_superuser = models.BooleanField(default=False, verbose_name="superuser")

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email',]

	objects = UserManager()

	def __str__(self):
		return self.username

	def has_module_perms(self, app_label):
		return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)
