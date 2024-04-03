import unittest
from unittest.mock import patch
from io import StringIO
from Miniproject_Final import place_order

class TestPlaceOrder(unittest.TestCase):
    @patch('builtins.input', side_effect=['John Doe', '123 Main St', '9876543210', 'coffee'])
    def test_place_order(self, mock_input):
        global orders
        orders = []  # Initialize orders list
        
        place_order()  # Call place_order function with mocked input
        
        # Verify that the order is added to the orders list with the correct data
        expected_order = {
            'customer_name': 'John Doe',
            'customer_address': '123 Main St',
            'customer_phone': '9876543210',
            'customer_item': 'coffee',
            'status': 'PREPARING'
        }
        self.assertIn(expected_order, orders)
        
    @patch('builtins.input', side_effect=['', '', '', ''])  # Simulate empty user input
    def test_place_order_empty_input(self, mock_input):
        global orders
        orders = []  # Initialize orders list
        
        place_order()  # Call place_order function with mocked input
        
        # Verify that the orders list remains empty
        self.assertEqual(len(orders), 0)
        
if __name__ == '__main__':
    unittest.main()