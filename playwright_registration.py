from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.locator('//input[@id=":r0:"]')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.locator('//input[@id=":r1:"]')
    username_input.fill("username")

    # Заполняем поле username
    username_input = page.locator('//input[@id=":r2:"]')
    username_input.fill("password")

    # Нажимаем на кнопку Registration
    registration_button = page.locator('//button[@id="registration-page-registration-button"]')
    registration_button.click()

    # Проверяем, что после редиректа на страницу дашбордов отображается заголовок Dashboard
    dashboard_h = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_h).to_be_visible()

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)
