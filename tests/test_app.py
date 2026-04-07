from django.test import TestCase
from django.urls import reverse


class IgsAppCoreTests(TestCase):
    def test_hello_view(self):
        url = reverse("igs_app_core_hello")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hola desde la app reusable igs_app_core")
