import allure
from my_pages.data_tests import create_account_data as cpd


@allure.feature("Registration page")
@allure.story("Registration page")
@allure.title("Check title on registration page")
def test_registration_page_name(create_account_page):
    """Проверка названия страницы регистрации"""
    create_account_page.open_page()
    create_account_page.check_header_title(cpd.page_form_name)


@allure.feature("Registration page")
@allure.story("Registration page")
@allure.title("Checking mandatory fields on a form")
def test_field_requirement(create_account_page):
    """Проверка обязательности полей регистрации"""
    create_account_page.open_page()
    create_account_page.check_required_fields(cpd.requirement_fields[0])


@allure.feature("Registration page")
@allure.story("Registration page")
@allure.title("Create new customer account.")
def test_create_new_customer(create_account_page, new_user_page):
    """Создание нового пользователя"""
    create_account_page.open_page()
    create_account_page.create_new_user(cpd.first_name, cpd.last_name, cpd.test_email, cpd.password)
    new_user_page.check_success_report(cpd.success_report_text)
