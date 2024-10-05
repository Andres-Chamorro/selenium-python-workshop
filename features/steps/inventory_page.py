from behave import given, when, then
from selenium import webdriver
from pages.inventory_page import InventoryPage

@given('the user is on the Inventory Page with items')
def step_user_is_on_inventory_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/v1/inventory.html')
    context.inventory_page = InventoryPage(context.driver)

@when('the user clicks on both inventory item buttons')
def step_user_clicks_on_both_items(context):
    context.inventory_page.click_first_item_button()
    context.inventory_page.click_second_item_button()


@then('the first inventory item button should be displayed')
def step_inventory_item_button_displayed(context):
    assert context.inventory_page.is_inventory_page_displayed()

