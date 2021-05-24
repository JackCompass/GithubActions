from django.test import TestCase
from django.urls import reverse
from .models import RegisteredUsers

class Tests(TestCase):

	def setUp(self):
		RegisteredUsers.objects.create(username = 'harry', age = 45, country = 'Washington')
		RegisteredUsers.objects.create(username = 'hermoine', age = 25, country = 'New York')
		RegisteredUsers.objects.create(username = 'ron', age = 35, country = 'Huston')

	def test_checking_total_entries(self):
		entries = RegisteredUsers.objects.count()
		self.assertEqual(entries, 3)

	def test_index_function(self):
		person = RegisteredUsers.objects.get(username = 'harry')
		self.assertEqual(person.age, 45)

	def test_correct_template(self):
		response = self.client.get('')
		self.assertEqual(response.status_code, 200)

	def test_template(self):
		'''Testing weather the template used in the index function is correct'''
		response = self.client.get(reverse('index'))
		self.assertTemplateUsed(response, 'pipeline/index.html')