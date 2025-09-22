from django.test import TestCase
from django.urls import reverse


class UsersViewsTests(TestCase):
    def test_users_sign_up_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("users:sign-up"))
        self.assertEqual(response.status_code, 200)

    def test_users_sign_in_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("users:sign-up"))
        self.assertEqual(response.status_code, 200)

    def test_users_sign_up_view_loads_correct_template(self):
        response = self.client.get(reverse("users:sign-up"))
        self.assertTemplateUsed(response, "users/sign-up.html")

    def test_users_sign_in_view_loads_correct_template(self):
        response = self.client.get(reverse("users:sign-in"))
        self.assertTemplateUsed(response, "users/sign-in.html")
