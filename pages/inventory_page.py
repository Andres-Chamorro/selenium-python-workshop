from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[3]/button')
    TITLE2 = (By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[3]/button')

    def click_first_item_button(self):
        self.click(self.TITLE)

    def click_second_item_button(self):
        self.click(self.TITLE2)

    def is_inventory_page_displayed(self):
        self.click(self.TITLE)
        self.click(self.TITLE2)
        return self.find_element(self.TITLE).is_displayed() and self.find_element(self.TITLE2).is_displayed()
