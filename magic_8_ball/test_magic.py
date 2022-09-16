from unittest import TestCase
import functions_magic

class TestMagic8Ball(TestCase):

    def test_generate_url(self):
        test_url = f'https://8ball.delegator.com/magic/JSON/Will I get my Degree?'
        self.assertEqual(test_url, functions_magic.extract_answer_from_response('Will I get my degree'))

    def test_exact_answer_from_response(self):
        example1 = {'magic':  {'question': 'will it be sunny tomorrow?', 'answer': 'Yes', 'type': 'Affirmative'}}
        self.assertEqual('Yes', functions_magic.extract_answer_from_response(example1))

        example2 = {'magic':  {'question': 'Is the sky blue?', 'answer': 'Yes', 'type': 'Affirmative'}}
        self.assertEqual('Nope', functions_magic.extract_answer_from_response(example2))

    #def test_extract_answer_from_response(self):
        



""" TODO create a test case to test the following functions,

generate_url_for_question
 - check that the expected URL is returned for an example question. 

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""