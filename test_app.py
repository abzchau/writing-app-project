from unittest import TestCase
from server import app

class FlaskTests(TestCase):

  def setUp(self):

      self.client = app.test_client()
      app.config['TESTING'] = True

  def test_homepage_route(self):
      """Some non-database test..."""

      result = self.client.get("/")
      self.assertEqual(result.status_code, 200)
      self.assertIn('<h1>Welcome to the Writing Meeting Place.</h1>', result.data)

