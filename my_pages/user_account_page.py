import allure

from playwright.sync_api import expect
from my_pages.base_page import BasePage
from my_pages.locators import user_account_locators as ual


class NewUserPage(BasePage):  # этот класс наследуется из BasePage
    """Класс для работы со страницей регистрации нового пользователя"""
    page_url = "/customer/account/"

    @allure.step("Проверить сообщение о создании нового пользователя")
    def check_success_report(self, report_text):
        success_report = (self.page.locator(ual.success_report_elem_path))
        expect(success_report.get_by_text(report_text))
