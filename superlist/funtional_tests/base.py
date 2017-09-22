from selenium import webdriver
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time
import unittest
import sys
from unittest import skip

class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url='http//'+arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url=cls.live_server_url
    @classmethod
    def tearDownClass(cls):
        if cls.server_url==cls.live_server_url:
           super().tearDownClass()
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.implicitly_wait(5)
        self.browser.implicitly_wait(5)
        self.browser.quit()

