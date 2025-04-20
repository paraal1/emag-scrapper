
from playwright.sync_api import sync_playwright

url = "https://altex.ro/laptopuri/cpl/filtru/chipset-video-dedicat-10911/rtx-5090_rtx-5080_rtx-5070-ti_rtx-4090_rtx-4080_rtx-4070/"



def open_browser(url):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    return p, browser, page


def getFilterOptions(page):
    ul = page.query_selector("div.Filters > ul")

    list_items = ul.query_selector_all("li")

    for item in list_items:
        div = item.query_selector("div")
        if div:
            text = div.inner_text().strip()
            if text != "":
                print(div.inner_text())



def main():
    p, browser, page = open_browser(url)

    getFilterOptions(page)


    browser.close()

    p.stop()
