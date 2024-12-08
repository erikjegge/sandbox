import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.goto("https://www.ebay.com/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_test_id("userid").click()
    page.get_by_test_id("userid").fill("erikjegge@gmail.com")
    page.get_by_role("button", name="Continue", exact=True).click()
    page.get_by_test_id("pass").click()
    page.get_by_test_id("pass").fill("8GiWzkGIlnlBZ0C7J0fM")
    page.get_by_role("button", name="Sign in").click()
    page.goto("https://accounts.ebay.com/acctsec/trust-a-device?id=k3sYpl42Nf4tyzUvfmTX1-26&ru=https%3A%2F%2Faccounts.ebay.com%2Facctsec%2Fauthn-register%3Fru%3Dhttps%253A%252F%252Freg.ebay.com%252Freg%252FChangeSecretQuestion%253Fflow%253DSIGN_IN%2526ru%253Dhttps%25253A%25252F%25252Fwww.ebay.com%25252F%26srt%3DAQAJAAABAP46q9XIOPYRAKRN17PhSGeUB7JWaMNzLS5JcjznCpExNQCuiPGfUrDO0uGWU7GIHAD7qhFqeGwWc9LSUNMQyr8hDjakc-_BNYeAAeN9ftStRDKoYljfNtmUGnlazY8oBSpRJ6gbFBtEud_XP5GpuiSuiFDziV-GPjDyISO2s2C8KZirZfMSyUtl-oRvZGlPuYflR9l6TRuQzVASFhoW7ZlB4utubc0LwCnOnRHXouopxQD9dsindT9e1GBH3ejYpN3_8uYgRjuro4_LuHTUkPZOTaKNqJKc9fuDyERR8dc70LtQAw8e3RRA65671QuYDND5szdtoVCMWfk6OwcwJ1U")
    page.get_by_label("Trust", exact=True).click()
    page.get_by_label("Cancel").click()
    page.get_by_label("Account").get_by_role("link", name="Sell").click()
    page.get_by_role("button", name="Create listing").click()
    page.get_by_role("button", name="Multiple listing").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)