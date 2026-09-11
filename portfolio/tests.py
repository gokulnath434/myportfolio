from django.test import TestCase
from django.urls import reverse


class PortfolioHomePageTests(TestCase):
    def test_home_page_renders_portfolio_content_without_raw_python_source(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf-8')

        self.assertIn('Gokulnath S', html)
        self.assertIn('Python Django Developer', html)
        self.assertIn('Available for Python Developer Opportunities', html)

        self.assertNotIn('portfolio/developer.py', html)
        self.assertNotIn('class DeveloperProfile', html)
        self.assertNotIn('get_core_stack', html)
        self.assertNotIn('Python 3.13', html)
