
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from superlist.lists.views import home_page
from django.template.loader import render_to_string
from lists.models import Item,List
import re
class HomePageTest(TestCase):
     def test_root_url_resolves_to_home_page_view(self):
         found = resolve('/')
         self.assertEqual(found.func, home_page)
     def test_home_page_returns_corrent_html(self):
         request=HttpRequest()
         response=home_page(request)
         expected_html = render_to_string('home.html',request=request)
         csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
         observed_html = re.sub(csrf_regex, '', response.content.decode())
         expected_html = re.sub(csrf_regex, '', expected_html)
         self.assertEqual(observed_html, expected_html)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        list_=List.objects.create()

        response=self.client.get('/lists/%d/' % (list_.id))
        self.assertTemplateUsed(response,'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list=List.objects.create()

        Item.objects.create(text='itemey 1',list=correct_list)
        Item.objects.create(text='itemey 2',list=correct_list)
        print(correct_list)
        other_list=List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')

    def test_displays_all_items(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        Item.objects.create(text='itemey 2', list=list_)

    def test_passes_correct_list_to_template(self):
        other_list=List.objects.create()
        correct_list=List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)


class NewlistTest(TestCase):
    def  test_can_save_post_request(self):
         self.client.post('/lists/new',data={'item_text':'A new list item '})
         self.assertEqual(Item.objects.count(),1)

    def test_redirects_after_POST(self):
        response=self.client.post('/lists/new',data={'item_text':'A new list item '})
        new_list=List.objects.first()
        self.assertRedirects(response,'/lists/%d/' % (new_list.id,))


class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post('/lists/%d/add_item' % (correct_list.id,),
        data={'item_text': 'A new item for an existing list'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)
    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.post(
            '/lists/%d/add_item' % (correct_list.id,),
            data={'item_text': 'A new item for an existing list'}
        )
        self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))