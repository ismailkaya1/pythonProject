from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LCW:
    CATEGORY_PAGE = (By.CSS_SELECTOR, ".menu.sf-arrows>li")
    SUB_CATEGORY_PAGE = (By.CLASS_NAME, "image_Box.visible-lg")
    SUB_CATEGORY_IMG_BOX = (By.CLASS_NAME, "image_Box.visible-lg")
    PRODUCT_PAGE = (By.CLASS_NAME, "product-card")
    CHOOSE_SIZE = (By.CLASS_NAME, "option-size > a")
    ADD_TO_CART = (By.ID, "pd_add_to_cart")
    CART_PAGE = (By.CLASS_NAME, "header-cart")
    MAIN_PAGE = (By.CLASS_NAME, "header-logo")
    MAIN_LOGO = (By.CLASS_NAME, "main-header-logo")
    PAYMENT_BUTTON = (By.CLASS_NAME, "mt-15")
    website = "https://www.lcwaikiki.com/tr-TR/TR"

    def __init__(self):
        self.driver = webdriver.Chrome("/home/ismailkaya/PycharmProjects/pythonProject/chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.website)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        assert self.wait.until(ec.element_to_be_clickable(self.MAIN_LOGO)).is_displayed(), 'This page is not main page!'
        self.wait.until(ec.presence_of_all_elements_located(self.CATEGORY_PAGE))[0].click()
        assert self.wait.until(ec.element_to_be_clickable(self.SUB_CATEGORY_IMG_BOX)).is_displayed(), \
            'This page is not category page'
        self.wait.until(ec.presence_of_all_elements_located(self.SUB_CATEGORY_PAGE))[1].click()
        assert self.wait.until(ec.element_to_be_clickable(self.PRODUCT_PAGE)).is_displayed(),\
            'This page is not product page'
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[1].click()
        assert self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).is_displayed(),\
            'Add to cart button is not displayed! This page is not product page.'
        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[0].click()
        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()
        self.wait.until(ec.element_to_be_clickable(self.CART_PAGE)).click()
        assert self.wait.until(ec.element_to_be_clickable(self.PAYMENT_BUTTON)).is_displayed(), \
                                  'Payment button is mot displayed! this pa is not cart page.'
        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()
        self.driver.quit()


LCW().test_navigate()