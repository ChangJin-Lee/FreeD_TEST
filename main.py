import streamlit as st
import sys

from App.app import allocate_inventory, convert_str_to_dict, check_order, check_warehouse_inventory

def main_page():
    st.write("# Welcome to FreeD Assginment! ๐")

    st.markdown(
        """
        ์ฃผ์ด์ง ๋ฌธ์ ๋ฅผ ํด๊ฒฐํ๊ณ  python์ ๋จ์ ํ์คํธ ํ๋ ์์ํฌ์ธ unittest๋ฅผ ์ฌ์ฉํ์ฌ ํ์คํธํ๋ ๊ณผ์ ์๋๋ค.
        
        [https://github.com/Jotter-Vortex/FreeD_TEST](https://github.com/Jotter-Vortex/FreeD_TEST)**๐ Enter a Github page via browser** to see infomation

        ## The Problem is...
        compute the best way an order can be shipped (called shipments) given
        inventory across a set of warehouses
    """
    )

    st.markdown(
        """        
        ### custom test
        - ์ํ๋ ํ์คํธ ์ผ์ด์ค๋ฅผ ๋ฐ์ ๋ฃ์ด๋ณด์ธ์. ๊ฒฐ๊ณผ๋ฅผ ๋ณผ ์ ์์ต๋๋ค.
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
        ####  ๋ ๋ง์ ์ผ์ด์ค๋ฅผ ๋ฃ์ผ๋ ค๋ฉด ๋ฐ์ ํ์์ ์ฐธ๊ณ ํด txt ํ์ผ์ ๋ณ๊ฒฝ
        #### sample_input.txt
        - ์ ์ผ ์ฒซ ๋ฒ์งธ ์ค์ ํ์คํธ ์ผ์ด์ค์ ๊ฐ์๊ฐ ์ฃผ์ด์ง๋๋ค.
        - ๋ ๋ฒ์งธ ์ค๋ถํฐ ํ ์ค์ฉ order, shipment, output์ด ์ฃผ์ด์ง๋๋ค.
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
