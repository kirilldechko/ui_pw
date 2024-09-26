import allure

from my_pages.base_page import BasePage
from my_pages.locators import eco_friendly_locators as loc


class EcoFriendly(BasePage):
    """Класс для работы со страницей экологически чистых товаров"""
    page_url = "/collections/eco-friendly.html"

    @allure.step("Переход на страницу товара")
    def go_to_commodity_page(self, commodity_name):
        search_commodity = self.find_elem(loc.commodity_path(commodity_name))
        self.check_elem_by_text(search_commodity.text, commodity_name)
        search_commodity.click()

    @allure.step("Проверка выбранного размера")
    def checking_the_selected_size(self, size, commodity_name):
        selected_size = self.find_elem(loc.selected_size(size, commodity_name))
        self.check_elem_by_text(size, selected_size.text)

    @allure.step("Выбрать размер товара")
    def select_commodity_size(self, size, commodity_name):
        size_button = self.find_elem(loc.size_button(size, commodity_name))
        size_button.click()
        selected_size = self.find_elem(loc.selected_size(size, commodity_name))
        self.check_elem_by_text(size, selected_size.text)
        return selected_size.text

    @allure.step("Выбрать цвет товара")
    def change_commodity_color(self, color, commodity_name):
        color_button = self.find_elem(loc.color_button(color, commodity_name))
        color_button.click()
        selected_color_elem = self.find_elem(loc.selected_color(color, commodity_name))
        return selected_color_elem.get_attribute('aria-label')

    @allure.step("Проверка выбранного цвета")
    def checking_the_selected_color(self, selected_color, commodity_name):
        color = self.find_elem(loc.selected_color(selected_color, commodity_name))
        assert color.get_attribute('aria-label') == selected_color

    # @allure.step("Добавить товар в корзину")
    # def add_to_cart(self, commodity_name):
    #     search_commodity = self.find_elem(loc.commodity_path(commodity_name))
    #     actions = ActionChains(self.page)  # для наведения мыши на элемент инициализируем ActionChains
    #     actions.move_to_element(search_commodity).perform()  # наводим мышь на элемент
    #     find_add_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located
    #                                                            (loc.add_button))
    #     find_add_button.click()
    #
    # @allure.step("Проверка сообщения о добавлении товара в корзину")
    # def check_success_text(self, commodity_name):
    #     success_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located
    #                                                         (loc.success_text(commodity_name)))
    #     assert commodity_name in success_text.text
