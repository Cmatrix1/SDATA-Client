
from playwright.async_api import async_playwright
from requests import get
from bs4 import BeautifulSoup


class SDataClient:

    async def get_data_playwright(self, question):
        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=False)
            page = await browser.new_page()
            await page.goto(f"https://sdata.ir/chatgpt/?q={question}&on=chatgpt")

            element_exists = await page.query_selector(selector=".martor-preview")
            text_content = await element_exists.text_content()
            await browser.close()
            return text_content.strip()

    def get_data_requests(self, question):
        response = get(f"https://sdata.ir/chatgpt/?q={question}&on=chatgpt").content
        soup = BeautifulSoup(response, "html.parser")
        return soup.find("div", class_="martor-preview").text.strip()
