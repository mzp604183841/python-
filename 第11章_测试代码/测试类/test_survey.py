import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self) -> None:
        question = 'what language did you first learn to speak ?'
        self.my_survey = AnonymousSurvey(question)

    def test_store_single_response(self):
        question = 'what language did you first learn to speak ?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.response)

    def test_store_3_response(self):
        question = 'what language did you first learn to speak ?'
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'French', 'chinese']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.response)


if __name__ == '__main__':
    unittest.main()

