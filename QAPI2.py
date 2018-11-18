import unittest
import requests

"""
The endpoints were not reachable. I tested using postman to verify. Anyway I have included my test scripts.
"""

class SampleTest2(unittest.TestCase):

    def test_main(self):
        url = 'https://od-api-demo.oxforddictionaries.com:443/api/v1/domains/es/es'
        headers = {"app_id": "!no1me2digas!", "app_key": "0clave42"}
        r = requests.post(url, headers=headers)
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()
