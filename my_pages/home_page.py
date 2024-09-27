import allure
from playwright.sync_api import expect

from my_pages.base_page import BasePage
from my_pages.locators import home_page_locators as hp_loc


class HomePage(BasePage):
    """Класс для работы с домашней страницей"""
    page_url = ""

    @allure.step("Проверка перехода на домашнюю страницу")
    def check_home_page_title(self, home_title):
        home_page = self.find_elem(hp_loc.home_page)
        expect (home_page).to_have_attribute('content', home_title)
