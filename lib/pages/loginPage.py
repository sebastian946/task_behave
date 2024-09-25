from lib.webelements.loginWebElements import LoginWebElements


class LoginPage:
    def __init__(self,context):
        self.context = context
        self.web_elements = LoginWebElements

    def openUrl(self):
        self.context.actions.openUrl(self.context.url)

    def fillLoginPage(self):
        self.context.actions.sendKeys(self.web_elements.input_user,self.context.user)
        self.context.actions.sendKeys(self.web_elements.input_password,self.context.password)
        self.context.actions.clickElement(self.web_elements.button_enviar)


