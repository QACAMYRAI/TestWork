from playwright.sync_api import sync_playwright, expect
import locators 

def test_buy_something():
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()

        try:
            # Переход на страницу
            page.goto(locators.URL)

            # Ввод логина и пароля
            page.get_by_placeholder(locators.INPUT_USERNAME).fill(locators.login)
            page.get_by_placeholder(locators.INPUT_PASSWORD).fill(locators.password)
            page.locator(locators.LOGIN).click()

            # Выбор продукта и добавление в корзину
            page.locator(locators.PRODUCT_FOR_TEST).click()
            page.locator(locators.ADD_TO_CART).click()
            page.locator(locators.SHOPING_CART).click()
            page.locator(locators.CHECKOUT).click()

            # Ввод данных для оформления заказа
            page.get_by_placeholder(locators.FIRST_NAME).fill(locators.first_name)
            page.get_by_placeholder(locators.LAST_NAME).fill(locators.last_name)
            page.get_by_placeholder(locators.POSTAL_CODE).fill(locators.postal_code)
            page.locator(locators.CONTINUE).click()
            page.locator(locators.FINISH).click()

            # Проверка успешного завершения заказа
            expect(page.locator(locators.COMPLETE_HEADER)).to_have_text("Thank you for your order!")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Закрытие контекста и браузера
            context.close()
            browser.close()

