from behave import given,when,then

from lib.pages.TestPage import TestPage
from lib.pages.loginPage import LoginPage


@given(u'user login in the page')
def step_impl(context):
    login = LoginPage(context)
    login.openUrl()
    login.fillLoginPage()


@when(u'the robot do the 10 cicles')
def step_impl(context):
    test = TestPage(context)
    test.automation_test()
    context.actions.waitSecond(2000)


@then(u'get the hast code')
def step_impl(context):
    context.actions.waitSecond(5000)
