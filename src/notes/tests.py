from django.test import TestCase
from django.urls import reverse


class NotesViewsTests(TestCase):
    def test_notes_about_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("notes:about"))
        self.assertEqual(response.status_code, 200)

    def test_notes_about_view_loads_correct_template(self):
        response = self.client.get(reverse("notes:about"))
        self.assertTemplateUsed(response, "notes/about.html")

    def test_notes_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("notes:home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("notes:home"))
        self.assertTemplateUsed(response, "notes/home.html")
