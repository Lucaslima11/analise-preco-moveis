import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(
            headless=False
        )

        page = await browser.new_page()
        await page.goto('https://www.madeiramadeira.com.br/moveis/moveis-para-quarto-infantil/cama-montessoriana')
        await page.wait_for_timeout(5000)

        all_products = await page.locator('//*[@id="control-box-content"]/div[3]/div[1]/div[2]/div/div/div/div[2]/div')\
        .filter(has_text='Cama')\
        .locator('h2').all_inner_texts()
        print(all_products)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())