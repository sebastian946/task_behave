import re
from lib.webelements.TestWebElement import TestWebElement
from datetime import datetime  # Importa datetime

class TestPage:
    def __init__(self, context):
        self.context = context
        self.web_elements = TestWebElement

    def automation_test(self):
        ciclo_actual = 0
        while int(ciclo_actual) < 10:
            text = self.context.actions.getContextText(self.web_elements.text_numberCicle)
            valores = re.findall(r'\d+', text)
            ciclo_actual = valores[0]

            # Realiza la resta de las fechas
            textDate = self.context.actions.getContextText(self.web_elements.text_first_box)
            dias = self.context.tools.getValueDias(textDate)
            date = self.context.tools.getValueDates(textDate)
            restaDate = self.context.tools.restarValues(dias, date)

            # Convierte `restaDate` a string en el formato que deseas
            fecha_str = restaDate.strftime('%d/%m/%Y')
            self.context.actions.sendKeys(self.web_elements.input_date, fecha_str)

            # Busca el emoji y cuenta
            #pull
            emoji_title = self.context.actions.getContextText(self.web_elements.text_emoji)
            emoji_to_count = self.context.tools.searchEmoji(emoji_title)
            emoji_text = self.context.actions.getContextText(self.web_elements.text_content_emoji)
            count = self.context.tools.countEmoji(emoji_text, emoji_to_count)
            self.context.actions.sendKeys(self.web_elements.input_number, count)
            self.context.actions.waitSecond(50000)
            if ciclo_actual == 4:
                print(count)
                print(fecha_str)

            self.context.actions.clickElement(self.web_elements.button_enviar)



