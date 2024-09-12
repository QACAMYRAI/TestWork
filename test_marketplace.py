import pytest
from playwright.sync_api import sync_playwright, expect
import locators


def test_buy_something():
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto(locators.URL)
        page.get_by_placeholder(locators.INPUT_USERNAME).fill(locators.login)
        page.get_by_placeholder(locators.INPUT_PASSWORD).fill(locators.password)
        page.locator(locators.LOGIN).click()
        page.locator(locators.PRODUCT_FOR_TEST).click()
        page.locator(locators.ADD_TO_CART).click()
        page.locator(locators.SHOPING_CART).click()
        page.locator(locators.CHECKOUT).click()
        page.get_by_placeholder(locators.FIRST_NAME).fill(locators.first_name)
        page.get_by_placeholder(locators.LAST_NAME).fill(locators.last_name)
        page.get_by_placeholder(locators.POSTAL_CODE).fill(locators.postal_code)
        page.locator(locators.CONTINUE).click()
        page.locator(locators.FINISH).click()

        expect(page.locator(locators.COMPLETE_HEADER)).to_have_text("Thank you for your order!")


        context.close()
        browser.close()

