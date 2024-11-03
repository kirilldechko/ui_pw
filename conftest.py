import pytest

from playwright.sync_api import BrowserContext
from my_pages.create_account import CreateAccount
from my_pages.eco_friendly_page import EcoFriendly
from my_pages.home_page import HomePage
from my_pages.sale_page import SalePage
from my_pages.user_account_page import NewUserPage
from my_pages.commodity_page import CommodityPage
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture()  # Фикстура для открытия браузера
def page(context: BrowserContext):  # context - это запущеный браузер
    page = context.new_page()
    return page


@pytest.fixture()  # инициализируем создание аккаунта и возвращаем этот объект доступным для тестов
def create_account_page(page):
    return CreateAccount(page)


@pytest.fixture()  # инициализируем страницу товаров
def eco_friendly_page(page):
    return EcoFriendly(page)


@pytest.fixture()  # инициализируем страницу распродажи
def sale_page(page):
    return SalePage(page)


@pytest.fixture()  # инициализируем страницу распродажи
def new_user_page(page):
    return NewUserPage(page)


@pytest.fixture()  # инициализируем страницу товара
def commodity_page(page):
    return CommodityPage(page)


@pytest.fixture()  # инициализируем домашнюю страницу
def home_page(page):
    return HomePage(page)
