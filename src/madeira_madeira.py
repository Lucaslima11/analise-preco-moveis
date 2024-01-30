import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as pw:
        browser = await pw.firefox.launch(
            headless=False
        )

        page = await browser.new_page()
        await page.goto('https://www.globo.com')
        await print(page.content())

if __name__ == '__main__':
    asyncio.run(main())