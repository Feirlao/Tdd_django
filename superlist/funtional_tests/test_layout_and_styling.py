from .base import FunctionalTest
class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        inputbox=self.get_item_inpt_box()
        self.browser.get(self.server_url)
        self.get_item_inpt_box().send_keys('testing\n')

        self.assertAlmostEqual(
            self.get_item_inpt_box().location['x'] + self.get_item_inpt_box().size['width'] / 2,
            self.browser.get_window_size().get("width") / 2,
            delta=5
        )