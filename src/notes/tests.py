from django.test import TestCase
from django.urls import resolve, reverse

from notes import views


class NoteTests(TestCase):
    def test_notes_home_url_is_correct(self):
        url = reverse("notes:home")
        self.assertEqual(url, "/")

    def test_notes_home_view_function_is_correct(self):
        view = resolve(reverse("notes:home"))
        self.assertIs(view.func.view_class, views.HomeView)

    def test_notes_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("notes:home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("notes:home"))
        self.assertTemplateUsed(response, "notes/home.html")
