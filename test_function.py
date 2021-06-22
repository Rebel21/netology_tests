import unittest
import unittest.mock
from app import *


class TestDocumentInfo(unittest.TestCase):

    def test_1_doc_exist_in_dict(self):
        self.assertEqual(check_document_existance("2207 876234"), True)

    def test_2_get_doc_owner_name(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            self.assertEqual(get_doc_owner_name(), "Аристарх Павлов")

    def test_3_add_new_doc(self):
        with unittest.mock.patch('builtins.input', side_effect=['9999', 'passport', 'Denis', 12]):
            add_new_doc()
            self.assertIn({"type": "passport", "number": "9999", "name": "Denis"}, documents)

    def test_4_delete_doc(self):
        with unittest.mock.patch('builtins.input', return_value='10006'):
            delete_doc()
            self.assertNotIn({"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}, documents)
