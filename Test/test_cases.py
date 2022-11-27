import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from App.app import convert_str_to_dict, allocate_inventory, check_order, check_warehouse_inventory

#
#   app test
#

def print_dicts(order, warehouse, output, expect_output):
    print('Input  :',order,',',warehouse, sep="  ")
    print('Output  :',output, sep="  ")
    print('ExpectOutput  :',expect_output, sep="  ")

def result_output(order, warehouse):
    order = convert_str_to_dict(list(order))
    warehouse = convert_str_to_dict(list(warehouse))
    if check_order(order) and check_warehouse_inventory(warehouse):
        return allocate_inventory(order, warehouse)
    else:
        return []

class TestApp(unittest.TestCase):
    def test_inventory_match(self):
        self.assertEqual(result_output("{ apple: 1 }", "[{ name: owd, inventory: { apple: 1 } }]"), 
                             [{ "owd": { "apple": 1 } }])

    def test_not_enough_inventory(self):
        self.assertEqual(result_output("{ apple: 1 }", "[{ name: owd, inventory: { apple: 0 } }]"), 
                             [])
        self.assertEqual(result_output("{ apple: 5 }", "[{ name: owd, inventory: { apple: 2 } }]"), 
                             [])
        self.assertEqual(result_output("{ apple: 15 }", "[{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]"), 
                             [])

    def test_inventory_split(self):
        self.assertEqual(result_output("{ apple: 10 }", "[{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]"),
                             [{ "dm": { "apple": 5 }}, { "owd": { "apple": 5 } }])
        self.assertEqual(result_output("{ apple: 7 }", "[{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]"),
                             [{ "dm": { "apple": 2 }}, { "owd": { "apple": 5 } }])                     
        self.assertEqual(result_output("{ apple: 5, banana: 5, orange: 5 }", "[{ name: owd, inventory: { apple: 5, orange: 10 } }, { name: dm, inventory: { banana: 5, orange: 10 }}]"),
                             [{'dm': {'banana': 5}}, {'owd': {'apple': 5, 'orange': 5}}])

    def test_order_is_minus(self):
        self.assertEqual(result_output("{ apple: -10 }", "[{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]"),
                             [])

    def test_inventory_is_minus(self):
        self.assertEqual(result_output("{ apple: 10 }", "[{ name: owd, inventory: { apple: -5 } }, { name: dm, inventory: { apple: 5 }}]"),
                             [])
    
    def test_inventory_and_order_both_minus(self):
        self.assertEqual(result_output("{ apple: -10 }", "[{ name: owd, inventory: { apple: -5 } }, { name: dm, inventory: { apple: 5 }}]"),
                             [])

    def test_inventory_empty(self):
        self.assertEqual(result_output("{ apple: 10 }", "[{ name: owd, inventory: {} }, { name: dm, inventory: {}}]"),
                             [])

    def test_order_empty(self):
        self.assertEqual(result_output("{}", "[{ name: owd, inventory: {} }, { name: dm, inventory: {}}]"),
                             [])

if __name__ == '__main__':
    unittest.main()