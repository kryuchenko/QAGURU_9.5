import pytest
from selene import browser
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    # Настройка конфигурации Selene
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1440

    # Настройка опций WebDriver
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield

    # Закрытие браузера с обработкой исключений
    try:
        browser.quit()
    except WebDriverException as e:
        print(f"Ошибка при закрытии браузера: {e}")
