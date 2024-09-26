import allure

from my_pages.data_tests import eco_freandly_data as ef_data


@allure.feature("Eco friendly page")
@allure.story("Eco friendly page")
@allure.title("Open commodity page")
def test_go_to_commodity_page(eco_friendly_page, commodity_page):
    """Открыть страницу товара"""
    eco_friendly_page.open_page()
    eco_friendly_page.go_to_commodity_page(ef_data.commodity_name)
    commodity_page.check_commodity_name(ef_data.commodity_name)


@allure.feature("Eco friendly page")
@allure.story("Eco friendly page")
@allure.title("Select commodity size")
def test_select_size(eco_friendly_page):
    """Выбрать размер товара"""
    eco_friendly_page.open_page()
    selected_size = eco_friendly_page.select_commodity_size(ef_data.commodity_size, ef_data.commodity_name)
    eco_friendly_page.checking_the_selected_size(selected_size, ef_data.commodity_name)


@allure.feature("Eco friendly page")
@allure.story("Eco friendly page")
@allure.title("Change commodity colore and check it")
def test_select_color(eco_friendly_page):
    """Изменить цвет товара и проверить его"""
    eco_friendly_page.open_page()
    selected_color = eco_friendly_page.change_commodity_color(ef_data.commodity_color, ef_data.commodity_name)
    eco_friendly_page.checking_the_selected_color(selected_color, ef_data.commodity_name)


@allure.feature("Eco friendly page")
@allure.story("Eco friendly page")
@allure.title("Check success_text")
def test_success_text(eco_friendly_page):
    """Проверить сообщение о добавлении товара в корзину"""
    eco_friendly_page.open_page()
    eco_friendly_page.select_commodity_size(ef_data.commodity_size, ef_data.commodity_name)
    eco_friendly_page.change_commodity_color(ef_data.commodity_color, ef_data.commodity_name)
    eco_friendly_page.add_to_cart(ef_data.commodity_name)
    eco_friendly_page.check_success_text(ef_data.commodity_name)
