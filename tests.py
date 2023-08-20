import unittest
from main import validate_password

class TestPasswordValidation(unittest.TestCase):
    def teste_senha_certa(self):
        self.assertTrue(validate_password("ValidPasword123!@"))

    def caso_1(self):
        self.assertFalse(validate_password(""))

    def case_2(self):
        self.assertFalse(validate_password("aa"))

    def case_3(self):
        self.assertFalse(validate_password("AAABBBCcC"))

    def case_4(self):
        self.assertFalse(validate_password("AbTP9!foo"))

    def case_5(self):
        self.assertTrue(validate_password("Abpt9Fok!"))


if __name__ == '__main__':
    unittest.main()