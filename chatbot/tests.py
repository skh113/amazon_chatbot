from django.test import TestCase


class UnitTestCase(TestCase):
    def test_use_chatbot_template(self):
        response = self.client.get("/chatbot/")
        self.assertTemplateUsed(response, "chatbot/chatbot.html")

    def test_accept_user_input(self):
        pass

    def test_returns_answer(self):
        pass

    def test_handel_invalid_input(self):
        pass
