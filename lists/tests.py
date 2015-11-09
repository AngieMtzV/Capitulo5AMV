from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'Nuevo Alumno')
		
		self.assertIn('Nuevo Alumno', response.content.decode())
		expected_html = render_to_string('home.html',{'new_item_text':'Nuevo Alumno'})

		self.assertEqual(response.content.decode(), expected_html)
		#self.assertTrue(response.content.startswith(b'<html>'))
		#self.assertIn(b'<title>Lista de Alumnos</title>', response.content)
		self.assertTrue(response.content.strip().endswith(b'</html>'))

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'Nuevo Alumno'
		response = home_page(request)
		
		self.assertIn('Nuevo Alumno', response.content.decode())
 		



