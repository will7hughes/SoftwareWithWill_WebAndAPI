import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from urllib.parse import urlencode

from account.models import User
from account.api.serializer import RegistrationSerializer

class RegisterUserTestCase(APITestCase):
	def setUp(self):
		#Authentication
		self.user = User.objects.create(user_id=1, username="user", email="user@gmail.com", password="password", is_staff=True, is_inspector=True)
		self.token = Token.objects.get(user=self.user)
		self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

	def test_register_user_valid(self):
		data = {
			"username": "jdoe",
			"email": "jdoe@gmail.com",
			"password": "pass2Word",
			"confirm_password": "pass2Word"
		}
		response = self.client.post("/api/account/register", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(User.objects.count(), 2)
		self.assertTrue(response.data['token'])

	def test_register_user_invalid(self):
		data = {
			"username": "jdoe",
			"email": "jdoe@gmail.com",
			"password": "pass2Word",
			"confirm_password": "pass2" #Passwords must match
		}
		response = self.client.post("/api/account/register", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(User.objects.count(), 1)

	def test_register_user_username_already_exists(self):
		data = {
			"username": "jdoe",
			"email": "jdoe@gmail.com",
			"password": "pass2Word",
			"confirm_password": "pass2Word"
		}
		response = self.client.post("/api/account/register", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(User.objects.count(), 2)
		data["email"] = "other_email@gmail.com"
		response = self.client.post("/api/account/register", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(User.objects.count(), 2)
		response_data = {
			"username": ["user with this username already exists."]
		}
		self.assertEqual(response.data, response_data)

	def test_register_user_email_already_exists(self):
		data = {
			"username": "jdoe",
			"email": "jdoe@gmail.com",
			"password": "pass2Word",
			"confirm_password": "pass2Word"
		}
		response = self.client.post("/api/account/register", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(User.objects.count(), 2)
		data["username"] = "otheruser"
		response = self.client.post("/api/account/register", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(User.objects.count(), 2)
		response_data = {
			"email": ["user with this email already exists."]
		}
		self.assertEqual(response.data, response_data)

	def test_register_user_email_and_username_already_exists(self):
		data = {
			"username": "jdoe",
			"email": "jdoe@gmail.com",
			"password": "pass2Word",
			"confirm_password": "pass2Word"
		}
		response = self.client.post("/api/account/register", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(User.objects.count(), 2)
		response = self.client.post("/api/account/register", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(User.objects.count(), 2)
		response_data = {
			"username": ["user with this username already exists."],
			"email": ["user with this email already exists."]
		}
		self.assertEqual(response.data, response_data)

		
class LoginUserTestCase(APITestCase):
	def setUp(self):
		#Authentication
		self.user = User.objects.create(user_id=1, username="user", email="user@gmail.com", password="password", is_staff=True, is_inspector=True)
		self.token = Token.objects.get(user=self.user)
		self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

	def test_login(self):
		data = {
			"username": "jdoe",
			"email": "jdoe@gmail.com",
			"password": "pass2Word",
			"confirm_password": "pass2Word"
		}
		response = self.client.post("/api/account/register", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(User.objects.count(), 2)
		data = urlencode({'username': "jdoe",'password': "pass2Word"})
		response = self.client.post('/api/account/login', data, content_type="application/x-www-form-urlencoded")
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(response.data['token'])