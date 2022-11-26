import sys

from App.app import allocate_inventory, convert_str_to_dict, check_order, check_warehouse_inventory


def main():
    # order and warehouses are both should dict format
    with open('sample_input.txt') as file_data:
        sys.stdin = file_data
        T = int(input())
        for test_input in range(1, T+1):
            input_order = input()
            input_warehouse = input()
            output = input()

            input_order = convert_str_to_dict(list(input_order))
            input_warehouse = convert_str_to_dict(list(input_warehouse))

            if check_order(input_order) and check_warehouse_inventory(input_warehouse):
                print(allocate_inventory(input_order, input_warehouse))
            else:
                print("Please check order and inventory")



if __name__ == "__main__":
    main()
