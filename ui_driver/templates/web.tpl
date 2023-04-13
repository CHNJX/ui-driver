from page.base_page import BasePage


class Web(BasePage):

    def teardown(self):
        self.driver.close()
