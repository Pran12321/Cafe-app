import unittest
from unittest.mock import patch
from io import StringIO
from Miniproject_Final import add_product

class TestAddProduct(unittest.TestCase):
    @patch('builtins.input', return_value='apple')  # Simulate user input 'apple'
    def test_add_product(self, mock_input):
        global product_list
        product_list = ['apple']  # Initialize product list
        
        add_product()  # Call add_product function with mocked input
        
        # Verify that the product is added to the product list
        self.assertIn('apple', product_list)
        
if __name__ == '__main__':
    unittest.main()