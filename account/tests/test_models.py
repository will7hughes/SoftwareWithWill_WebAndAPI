from django.test import TestCase
from account.models import User, UserManager

class TestUserModel(TestCase):

	def test_create_user_required_fields(self):
		with self.assertRaises(ValueError):
			User.objects.create_user('', 'jdoe@gmail.com', 'password')
			User.objects.create_user('jdoe', '', 'password')
			User.objects.create_user('jdoe', 'jdoe@gmail.com', '')
	
	def test_create_user_permissions(self):
		user = User.objects.create_user(
			username='jdoe',
			email='jdoe@gmail.com',
			password='jdoepassword'
		)
		self.assertTrue(user.is_active)
		self.assertTrue(user.is_report)
		self.assertFalse(user.is_staff)

	def test_create_super_user_required_fields(self):
		with self.assertRaises(ValueError):
			User.objects.create_superuser('', 'jdoe@gmail.com', 'password')
			User.objects.create_superuser('jdoe', '', 'password')
			User.objects.create_superuser('jdoe', 'jdoe@gmail.com', '')
	
	def test_create_superuser_permissions(self):
		user = User.objects.create_superuser(
			username='jdoe',
			email='jdoe@gmail.com',
			password='jdoepassword'
		)
		self.assertTrue(user.is_active)
		self.assertTrue(user.is_report)
		self.assertTrue(user.is_admin)
		self.assertTrue(user.is_superuser)