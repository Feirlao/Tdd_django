
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from superlist.lists.views import home_page
from django.template.loader import render_to_string
import re
class HomePageTest(TestCase):
     def test_root_url_resolves_to_home_page_view(self):
         found = resolve('/') # ➋
         self.assertEqual(found.func, home_page) # ➌
     def test_home_page_returns_corrent_html(self):
         request=HttpRequest()
         response=home_page(request)
         expected_html = render_to_string('home.html',request=request)
         print('response.content.decode()\n', response.content.decode())
         print('expected_html\n', expected_html)
         csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
         observed_html = re.sub(csrf_regex, '', response.content.decode())
         expected_html = re.sub(csrf_regex, '', expected_html)
         self.assertEqual(observed_html, expected_html)

     def test_home_page_can_save_post_request(self):
         request=HttpRequest()
         request.method='POST'
         request.POST['item_text']='A new list item'

         response=home_page(request)
         self.assertIn('A new list item',response.content.decode())
         excected_html=render_to_string('home.html',
            {'new_item_text':'A new list item'})
         csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
         observed_html = re.sub(csrf_regex, '', response.content.decode())
         self.assertEqual(observed_html,excected_html)


