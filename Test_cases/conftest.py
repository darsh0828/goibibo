import allure
import pytest
import os
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options


# @pytest.fixture(params=['device1', 'device2'], scope='function')
# def appium_driver(request):
#     if request.param == 'device1':
#         desired_caps = dict(
#             deviceName='Android',
#             platformName= 'Android',
#             appPackage='com.goibibo',
#             appActivity= 'com.goibibo.common.HomeActivity',
#             udid= 'sdfaef'
#         )
#         capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
#         driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
#     if request.param == 'device2':
#         desired_caps = dict(
#             deviceName='Android',
#             platformName='Android',
#             appPackage='com.goibibo',
#             appActivity='com.goibibo.common.HomeActivity',
#             udid='sdfaef'
#         )
#         capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
#         driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

# this is main fixture
@pytest.fixture(scope='function')
def appium_driver(request):
    # username = os.getenv("BROWSERSTACK_USERNAME")
    # access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
    #
    # if not username or not access_key:
    #     raise Exception("Please set BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY as environment variables")

    desired_caps = dict(
        deviceName='Android',
        platformName='Android',
        appPackage='com.goibibo',
        appActivity='.common.HomeActivityAliasDiwali',
        automationName='UiAutomator2',
        noReset=True,
        fullReset=False

    )

    # hub_url = f"https://{username}:{access_key}@hub.browserstack.com"

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver

    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    print("entering log_on_failure")
    yield
    item = request.node
    driver = appium_driver
    print("waiting for log_on_failure")
    if item.rep_call.failed:
        print("executing log_on_failure")
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
