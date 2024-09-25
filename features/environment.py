from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from lib.helper.tools import Tools
from lib.utils.actions import Actions


def before_all(context):
    driver = set_driver()
    driver.set_page_load_timeout(10)
    context.driver = driver

    context.actions = Actions(context.driver)
    context.tools = Tools()

    context.user = "918071"
    context.password = "10df2f32286b7120MS00LTE3MDgxOQ==30e0c83e6c29f1c3"
    context.url = "https://tasks.evalartapp.com/automatization/"


def set_driver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    try:
        service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except WebDriverException as e:
        print(f"Error al instalar o iniciar el ChromeDriver: {e}")
        print("Intentando con una versión específica del driver...")
        try:
            service = Service(ChromeDriverManager(version="127.0.0", chrome_type=ChromeType.GOOGLE).install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
        except WebDriverException as e:
            raise RuntimeError(f"No se pudo iniciar el ChromeDriver: {e}")

    driver.maximize_window()
    return driver
