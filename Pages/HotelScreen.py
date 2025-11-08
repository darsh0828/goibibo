import time

from Pages.BasePage import BasePage


class HotelScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def search_hotels(self, city):
        print("Step 0")
        self.click("destination_search_XPATH")
        print("Step 1")
        self.type("search_text_XPATH", city)
        print("Step 2")
        self.click("select_city_XPATH")
        print("Step 3")
        self.click("search_XPATH")
        print("Step 4")




