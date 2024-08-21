# Databricks notebook source
import unittest
from datasvc import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_read_data(self):
        response = self.app.get('/data/read')
        self.assertEqual(response.status_code, 200)
        self.assertIn('col1', response.json[0])

if __name__ == "__main__":
    unittest.main()
