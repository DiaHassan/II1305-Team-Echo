from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://se.indeed.com/jobs?q=java&l=&vjk=76d3e26b11dc418a&advn=8529806170522296")
    data = page.content()
    data = data.encode('ascii', 'replace').decode('ascii')
    f = open("text.txt", "a")
    f.write(data)
    f.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)