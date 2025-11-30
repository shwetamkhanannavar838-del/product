import pytest
from product import get_product_details

def test_get_employee_details():
    #sample data
    prd_id = "P101"
    name = "Wireless Mouse"
    quantity = 2
    price = 550
    #Expected result
    expected_output=(
        "Product ID: P101\n"
        "Product name: Wireless Mouse\n"
        "Quantity: 2\n"
        "Price: 550"
    )
    #Assertion
    assert get_product_details(prd_id,name,quantity,price) == expected_output