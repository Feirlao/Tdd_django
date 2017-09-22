from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_new_item')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
        any(row.text == '1: Buy peacock feathers' for row in rows) )
