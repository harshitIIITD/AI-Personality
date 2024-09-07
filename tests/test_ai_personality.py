import unittest
from src.ai_personality import AssertiveAIPersonality

class TestAssertiveAIPersonality(unittest.TestCase):
    def setUp(self):
        self.ai = AssertiveAIPersonality()

    def test_make_assertive(self):
        text = "I think this is a good idea."
        expected = "I am sure this is a good idea."
        self.assertEqual(self.ai.make_assertive(text), expected)

    def test_generate_response(self):
        prompt = "What do you think?"
        response = self.ai.generate_response(prompt)
        self.assertIsInstance(response, str)


if __name__ == '__main__':
    unittest.main()
