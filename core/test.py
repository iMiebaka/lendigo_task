import unittest
import requests

class CheckApp(unittest.TestCase):
    API_URL = "http://localhost:5000/api/v1/"
    
    def test_home(self):
        res = requests.get(self.API_URL)
        self.assertEqual(res.status_code, 200)

    def test_page_search(self):
        params = {"search": "test_data"}
        res = requests.get(url = f"{self.API_URL}get-posts", params=params)
        self.assertEqual(res.status_code, 200)
        
    def test_page_view(self):
        params = {"page":1}
        res = requests.get(url = f"{self.API_URL}get-posts", params=params)
        self.assertEqual(res.status_code, 200)

    def test_view_comment(self):
        params = {"page":1}
        res = requests.get(url = f"{self.API_URL}get-posts", params=params)
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()