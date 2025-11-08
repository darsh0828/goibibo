import pytest

from Pages.HomeScreen import HomeScreen
from Test_cases.BaseTest import BaseTest
from Utilitis import dataProvider


class Test_SearchHotel(BaseTest):

    @pytest.mark.parametrize("city", dataProvider.get_data("SearchTest", 1))
    def test_searchHotel(self,city):
        home = HomeScreen(self.driver)
        home.goto_hotels().search_hotels(city)

