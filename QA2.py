import unittest
from selenium import webdriver
from configparser import ConfigParser
import csv

class SampleTest2(unittest.TestCase):

    def setUp(self):
        print('Testing Task2 start')
        config = ConfigParser()
        config.read('config.ini')
        location = config.get('Chrome', 'location')
        self.driver = webdriver.Chrome(location)
        self.driver.maximize_window()

    def get_credentials(self):
        with open('login_users.csv') as datafile:
            csv_reader = csv.reader(datafile)
            return next(csv_reader)

    def test2_main(self):
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
        self.driver.set_page_load_timeout(20)
        username, password = self.get_credentials()
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys(username)
        self.driver.find_element_by_id("passwd").send_keys(password)
        self.driver.find_element_by_id("SubmitLogin").click()
        self.driver.implicitly_wait(10)
        element = self.driver.find_element_by_class_name("account")
        self.assertEqual(element.text, 'qa qa', 'Login failed')

    def tearDown(self):
        self.driver.quit()
        print('Testing Task2 stop')


if __name__ == "__main__":
    unittest.main()
