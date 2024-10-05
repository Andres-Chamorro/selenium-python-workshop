from behave import given, when, then
from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.inventory_page_delete import InventoryPageDelete

@given('the user has added a product to the Inventory Page')
def step_user_is_on_inventory_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/v1/inventory.html')  # URL de la página de inventario
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.click_first_item_button()

@when('the user navigates to the cart page')
def step_user_navigates_to_cart_page(context):
    context.driver.get('https://www.saucedemo.com/v1/cart.html')  # Asegúrate de que esta es la URL del carrito
    context.inventory_page_delete = InventoryPageDelete(context.driver)

@when('the user clicks on the delete product button')
def step_user_clicks_on_delete_product(context):
    context.inventory_page_delete.delete_product()

@then('the product should be removed from the inventory list')
def step_product_removed_from_inventory_list(context):
    assert context.inventory_page_delete.is_product_removed()
    context.driver.quit()