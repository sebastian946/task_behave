from selenium.webdriver.common.by import By

class TestWebElement:
    text_numberCicle = (By.XPATH,"//p[contains(text(),'ciclo')]")
    text_first_box = (By.XPATH,"//p[contains(text(),'fecha')]")
    input_date = (By.XPATH,"//input[@type='date']")
    input_number = (By.XPATH,"//input[@type='number']")
    text_emoji = (By.XPATH,"//p[contains(text(),'cuantos')]")
    text_content_emoji = (By.XPATH,"(//div[contains(@class,'w-9/12')]//p)[2]")
    button_enviar = (By.XPATH,"//button[@type='submit']")