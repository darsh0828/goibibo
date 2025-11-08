import pytest

from Pages.HomeScreen import HomeScreen
from Pages.FlightScreen import FlightScreen
from Test_cases.BaseTest import BaseTest
from Utilitis import dataProvider


class Test_SearchFlight(BaseTest):


    def test_searchFlight(self):
        home = HomeScreen(self.driver)
        home.goto_flight().search_flight()