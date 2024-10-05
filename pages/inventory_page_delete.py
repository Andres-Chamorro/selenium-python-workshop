from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPageDelete(BasePage):
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, '[data-action="REMOVE"]')  # Usa el selector correcto para el botón de eliminar
    FIRST_ITEM_DELETE_BUTTON = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/button')  # XPath correcto

    def delete_product(self):
        self.click(self.DELETE_PRODUCT_BUTTON)

    def delete_first_product(self):
        self.click(self.FIRST_ITEM_DELETE_BUTTON)


    def is_product_removed(self):
        product_elements = self.driver.find_elements(*self.PRODUCT_CONTAINER)
        return len(product_elements) == 0  # Verifica que no queden productos