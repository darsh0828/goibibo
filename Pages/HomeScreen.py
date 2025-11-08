from Pages.BasePage import BasePage
from Pages.FlightScreen import FlightScreen
from Pages.HotelScreen import HotelScreen


class HomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def goto_hotels(self):
        self.click("hotels_XPATH")
        return HotelScreen(self.driver)


    def goto_flight(self):
        self.click("goto_flight_XPATH")
        return FlightScreen(self.driver)
