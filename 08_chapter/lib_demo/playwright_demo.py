# playwright_demo.py
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cn.bing.com/")
    page.get_by_role("searchbox", name="输入搜索词").click()
    page.get_by_role("searchbox", name="输入搜索词").fill("playwright")
    page.get_by_role("searchbox", name="输入搜索词").press("Enter")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Playwright 中文网", exact=True).click()
    page1 = page1_info.value
    page1.get_by_text("Playwright", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
