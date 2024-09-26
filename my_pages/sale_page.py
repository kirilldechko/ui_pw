import allure

from my_pages.base_page import BasePage
from my_pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    """Класс для работы со страницей распродажи"""
    page_url = "/sale.html"

    @allure.step("Проверить название вкладки Sale")
    def check_sale_tab(self, page_name):
        tab_name = self.find_elem(loc.sale_tab_xpath)
        self.check_elem_by_text(page_name, tab_name.text)

    @allure.step("Проверка наличия вкадки 'Домашняя старница'")
    def find_home_button(self, home_button):
        search_home_button = self.find_elem(loc.home_button_xpath)
        self.check_elem_by_text(home_button, search_home_button.text)

    @allure.step("Переход на домашнюю страницу")
    def check_home_page(self, home_button):
        search_home_button = self.find_elem(loc.home_button_xpath)
        self.check_elem_by_text(home_button, search_home_button.text)
        search_home_button.click()
