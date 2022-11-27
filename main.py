import streamlit as st
import sys

from App.app import allocate_inventory, convert_str_to_dict, check_order, check_warehouse_inventory

def main_page():
    st.write("# Welcome to FreeD Assginment! 👋")

    st.markdown(
        """
        주어진 문제를 해결하고 python의 단위 테스트 프레임워크인 unittest를 사용하여 테스트하는 과제입니다.
        
        [https://github.com/Jotter-Vortex/FreeD_TEST](https://github.com/Jotter-Vortex/FreeD_TEST)**👈 Enter a Github page via browser** to see infomation

        ## The Problem is...
        compute the best way an order can be shipped (called shipments) given
        inventory across a set of warehouses
    """
    )

    st.markdown(
        """        
        ### custom test
        - 원하는 테스트 케이스를 밑에 넣어보세요. 결과를 볼 수 있습니다.
    """
    )

    st_order = st.text_input('order info', '{ apple: 1 }')
    st_warehouse = st.text_input('warehouse info', '[{ name: owd, inventory: { apple: 1 } }]')
    try:
        st_order = convert_str_to_dict(list(st_order))
        st_warehouse = convert_str_to_dict(list(st_warehouse))
        if check_order(st_order) and check_warehouse_inventory(st_warehouse):
            st.success(allocate_inventory(st_order, st_warehouse))
        else:
            st.error("Please check order and inventory")
    except:
        st.error("format dosen't match")
    
    st.markdown(
        """
        ####  더 많은 케이스를 넣으려면 밑의 형식을 참고해 txt 파일을 변경
        #### sample_input.txt
        - 제일 첫 번째 줄에 테스트 케이스의 개수가 주어집니다.
        - 두 번째 줄부터 한 줄씩 order, shipment, output이 주어집니다.
    """
    )

    input_writes = []
    with open('sample_input.txt') as file_data:
        st.write(file_data.readlines())


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
    main_page()
