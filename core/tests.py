from django.test import TestCase


class UnitTestCase(TestCase):
    def test_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "core/index.html")
