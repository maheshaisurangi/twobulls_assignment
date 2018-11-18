import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser


class SampleTest(unittest.TestCase):

    def setUp(self):
        print('Testing Task1 start')
        config = ConfigParser()
        config.read('config.ini')
        location = config.get('Chrome', 'location')
        self.driver = webdriver.Chrome(location)
        self.driver.maximize_window()

    def test_main(self):
        self.driver.get("https://www.google.com/")
        self.driver.set_page_load_timeout(30)
        search_field = self.driver.find_element_by_name("q")
        search_field.send_keys("QA")
        search_field.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)

        search_links = self.driver.find_elements_by_tag_name("a")
        link_to_click = None
        for link in search_links:
            if link.get_attribute('href') == 'https://en.wikipedia.org/wiki/Software_quality_assurance':
                link_to_click = link

        self.assertIsNotNone(link_to_click, 'Desired search result not found')
        link_to_click.click()
        self.driver.set_page_load_timeout(30)

        link_list = self.driver.find_elements_by_tag_name('a')
        href_list = []
        for link in link_list:
            href_list.append(link.get_attribute('href'))

        self.assertIn("https://en.wikipedia.org/wiki/Quality_assurance", href_list, 'Desired wikipedia link not found')

    def tearDown(self):
        self.driver.quit()
        print('Testing Task1 finished')


if __name__ == "__main__":
    unittest.main()
