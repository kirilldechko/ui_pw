import allure
from playwright.sync_api import expect

from my_pages.base_page import BasePage
from my_pages.locators import create_account_locators as loc


class CreateAccount(BasePage):  # этот класс наследуется из BasePage
    """Класс для работы со страницей регистрации нового пользователя"""
    page_url = "/customer/account/create/"

    @allure.step("Проверить название формы регистрации")
    def check_header_title(self, page_title_name):
        search_form_field = self.find_elem(loc.page_form_path)
        expect (search_form_field.text == page_title_name)

    @allure.step("Заполнить поле 'Имя'")
    def fill_in_the_first_name_field(self, name):
        search_first_name_fild = self.find_elem(loc.first_name_x_path)
        search_first_name_fild.fill(name)
        self.check_elem_name_value(name, loc.first_name_x_path)

    @allure.step("Заполнить поле 'Фамилия'")
    def fill_in_the_last_name_field(self, last_name):
        search_last_name_fild = self.find_elem(loc.last_name_x_path)
        search_last_name_fild.fill(last_name)
        self.check_elem_name_value(last_name, loc.last_name_x_path)

    @allure.step("Заполнить поле 'Email'")
    def fill_in_the_email_field(self, test_email):
        search_email_fild = self.find_elem(loc.email_field_path)
        search_email_fild.fill(test_email)
        self.check_elem_name_value(test_email, loc.email_field_path)

    @allure.step("Заполнить поле 'Пароль'")
    def fill_in_the_password_field(self, password):
        search_pass_field = self.find_elem(loc.password_field_path)
        search_pass_field.fill(password)
        self.check_elem_name_value(password, loc.password_field_path)

    @allure.step("Заполнить поле 'Подтвердите пароль'")
    def fill_in_the_confirm_password_field(self, password):
        search_confirm_pass_field = self.find_elem(loc.confirm_password_field_path)
        search_confirm_pass_field.fill(password)
        self.check_elem_name_value(password, loc.confirm_password_field_path)

    @allure.step("Нажать кнопку 'Зарегистрироваться'")
    def click_on_registration_button(self):
        search_registration_button = self.find_elem(loc.registration_button_path)
        search_registration_button.click()

    @allure.step("Проверка признака обязательности у поля формы")
    def check_required_fields(self, requirement_field_path):
        search_name_fild = self.find_elem(requirement_field_path)
        expect(search_name_fild.get_attribute("aria-required") == "true")

    @allure.step("Создание нового пользователя")
    def create_new_user(self, first_name, last_name, email, password):
        self.fill_in_the_first_name_field(first_name)
        self.fill_in_the_last_name_field(last_name)
        self.fill_in_the_email_field(email)
        self.fill_in_the_password_field(password)
        self.fill_in_the_confirm_password_field(password)
        self.click_on_registration_button()
