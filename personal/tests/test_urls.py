from django.test import SimpleTestCase
from django.urls import reverse, resolve
from personal.views import home_screen_view

class TestUrls(SimpleTestCase):

	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'personal/home.html')

	# def test_come_url_is_resolved(self):
	# 	url = reverse('')
	# 	self.assertEquals(resolve(url).func, home_screen_view)