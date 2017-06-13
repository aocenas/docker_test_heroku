import unittest
import requests
SERVER_URL = 'http://localhost:5000'


class MainTestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(True, True)


class APITestCase(unittest.TestCase):
    def test_test(self):
        campaign_id = '23842563749550662'
        res = requests.get(f'{SERVER_URL}/test')
        self.assertIn(res.status_code, [200])
