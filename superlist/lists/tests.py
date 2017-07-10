
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from superlist.lists.views import home_page
from django.template.loader import render_to_string
from lists.models import Item
import re
class HomePageTest(TestCase):
     def test_root_url_resolves_to_home_page_view(self):
         found = resolve('/') # ➋
         self.assertEqual(found.func, home_page) # ➌
     def test_home_page_returns_corrent_html(self):
         request=HttpRequest()
         response=home_page(request)
         print(response)
         expected_html = render_to_string('home.html',request=request)
     #    print('response.content.decode()\n', response.content.decode())
     #    print('expected_html\n', expected_html)
         csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
         observed_html = re.sub(csrf_regex, '', response.content.decode())
         expected_html = re.sub(csrf_regex, '', expected_html)
         self.assertEqual(observed_html, expected_html)

     def test_home_page_can_save_post_request(self):
         request=HttpRequest()
         request.method='POST'
         request.POST['item_text']=('A new list item')
         response=home_page(request)
<<<<<<< HEAD
         self.assertEqual(Item.objects.count(),1)
         new_item=Item.objects.first()
         self.assertEqual(new_item.text,'A new list item')
         self.assertIn('A new list item',response.content.decode())
         excected_html=render_to_string('home.html',
            {'new_item_text':'A new list item'})
         csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
         observed_html = re.sub(csrf_regex, '', response.content.decode())
         self.assertEqual(observed_html,excected_html)
     def test_home_page_only_saves_when_necessary(self):
         request=HttpRequest()
         home_page(request)
         self.assertEqual(Item.objects.count(),0)

=======
         print(response)
         self.assertEqual(Item.objects.count(), 1)
         new_item = Item.objects.first()
         self.assertEqual(new_item.text, 'A new list item')
         self.assertEqual(response.status_code,302)
         self.assertEqual(response['location'],'/')
         #self.assertIn(new_item.text,response.content.decode())
         #excected_html=render_to_string('home.html',
           # {'new_item_text':'A new list item'})
         #csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
         #observed_html = re.sub(csrf_regex, '', response.content.decode())
         #self.assertEqual(observed_html,excected_html)

     def test_home_page_only_saves_items_when_necessary(self):
         request=HttpRequest()
         home_page(request)
         self.assertEqual(Item.objects.count(),0)
>>>>>>> 826a76537cd9d84f25e92ce18a36a4ac1e6d8ff4

class ItemModelTest(TestCase):
     def test_saving_and_retrieving_items(self):
         first_item = Item()
         first_item.text = ('The first (ever) list item')
         first_item.save()
         second_item = Item()
         second_item.text = ('Item the second')
         second_item.save()
         saved_items = Item.objects.all()
         self.assertEqual(saved_items.count(), 2)
         first_saved_item = saved_items[0]
         second_saved_item = saved_items[1]
         self.assertEqual(first_saved_item.text, 'The first (ever) list item')
         self.assertEqual(second_saved_item.text, 'Item the second')

