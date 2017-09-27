from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox =self.get_item_inpt_box()
        self.browser.get(self.server_url)
        self.get_item_inpt_box().send_keys('\n')
        self.assertEqual(
        self.get_item_inpt_box().get_attribute('placeholder'),
        'Enter a to-do item')
        self.get_item_inpt_box().send_keys('Buy peacock feathers')
        self.get_item_inpt_box().send_keys(Keys.ENTER)

