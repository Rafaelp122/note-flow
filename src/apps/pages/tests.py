from django.test import TestCase
from django.urls import reverse


class PagesViewsTests(TestCase):
    def test_pages_about_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("pages:about"))
        self.assertEqual(response.status_code, 200)

    def test_pages_about_view_loads_correct_template(self):
        response = self.client.get(reverse("pages:about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_pages_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)

    def test_pages_home_view_loads_correct_template(self):
        response = self.client.get(reverse("pages:home"))
        self.assertTemplateUsed(response, "pages/home.html")
