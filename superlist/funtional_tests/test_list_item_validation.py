from unittest import skip
from .base import FunctionalTest
from lists.forms import (
       DUPLICATE_ITEM_ERROR, EMPTY_LIST_ERROR,
       ExistingListItemForm, ItemForm
)

from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.get_item_inpt_box().send_keys('\n')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text,EMPTY_LIST_ERROR)
        self.get_item_inpt_box().send_keys('buy milk\n')
        self.check_for_row_in_list_table('1:buy milk')
        self.get_item_inpt_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, EMPTY_LIST_ERROR)

        self.get_item_inpt_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        self.browser.get(self.server_url)
        self.get_item_inpt_box().send_keys('buy wellies\n')
        self.get_item_inpt_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:buy wellies')

        self.get_item_inpt_box().send_keys('buy wellies\n')
        self.get_item_inpt_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:buy wellies')

        error = self.browser.find_element_by_css_selector('.has-error2')
        self.assertEqual(error.text,DUPLICATE_ITEM_ERROR)