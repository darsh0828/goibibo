from Pages.BasePage import BasePage


class FlightScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_flight(self):
        self.click("search_flight_RESOURCEID")
        self.click("dismiss_RESOURCEID")