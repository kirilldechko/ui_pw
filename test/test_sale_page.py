import allure
from my_pages.data_tests import sale_page_data as sale_data


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Go to sale page")
def test_sale_tab_name(sale_page):
    """Проверка названия вкладки распродажи"""
    sale_page.open_page()
    sale_page.check_sale_tab(sale_data.page_name)


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Check home button")
def test_check_home_page_button(sale_page):
    """Проверка наличия кнопки Home"""
    sale_page.open_page()
    sale_page.find_home_button(sale_data.home_button)


@allure.feature("Sale page")
@allure.story("Sale page")
@allure.title("Go to home page")
def test_go_to_home_page(sale_page, home_page):
    """Переход на домашнюю страницу"""
    sale_page.open_page()
    sale_page.check_home_page(sale_data.home_button)
    home_page.check_home_page_title(sale_data.page_title)


