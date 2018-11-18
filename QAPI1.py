import unittest
import requests

"""
The endpoints were not reachable. I tested using postman to verify. Anyway I have included my test scripts.
"""

class SampleTest(unittest.TestCase):

    def test_main(self):
        url = 'http://passwordutility.net:80/api/password/generate'
        data = {"password": "123456", "user_id": "70f3fc6beac4412b82db266b4796b"}
        r = requests.post(url, data=data)
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()
