
from selenium.webdriver.common.by import By

class LoginWebElements:
    input_user = (By.XPATH,"//input[@placeholder='Usuario ']")
    input_password = (By.XPATH,"//input[@placeholder='Contraseña ']")
    button_enviar = (By.XPATH,"//button[@type='submit']")