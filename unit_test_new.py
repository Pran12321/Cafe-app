import unittest
from unittest.mock import patch
from io import StringIO
from Miniproject_Final import add_product  # My function imported from my product

class TestAddProduct(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['New Product', '10.99'])  # Mocking user input, # Builtin makes it into string. #
    @patch('sys.stdout', new_callable=StringIO)  # Redirecting stdout to capture printed output
    def test_add_product(self, mock_stdout, mock_input):
        add_product()  # Call the function
        
        # Get the output value
        output = mock_stdout.getvalue()
        
        # Assert statements to check if the expected output is printed
        assert 'Record inserted successfully!' in output
        assert 'Name: New Product, Price: 10.99' in output

if __name__ == '__main__':
    unittest.main()
    
    
# Patch() and unittest.mock provides a powerful way to mokck objects. patch looks up an object in a module, replacing it with a mock!
#you can use this to mock an object for the entire duration of the function, just provide the scope

