import allure

from my_pages.base_page import BasePage
from my_pages.data_tests.commodity_data import commodity_page_url
from my_pages.locators import commodity_page_locators as loc


class CommodityPage(BasePage):
    page_url = commodity_page_url

    @allure.step("Проверка наименования товара на странице товара")
    def check_commodity_name(self, commodity_name):
        search_commodity_name = self.find_elem(loc.commodity_name_loc)
        self.check_elem_by_text(commodity_name, search_commodity_name.text)

