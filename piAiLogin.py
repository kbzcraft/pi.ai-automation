
import asyncio
from playwright.async_api import Playwright, async_playwright

async def login(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=True,args=["--headless=new",])
    context = await browser.new_context()
    page = await context.new_page()
    print("logging in")
    await page.goto("https://pi.ai/talk")
    await page.locator('xpath=//html/body/div/main/div/div/div[3]/button').click()
    await page.locator('xpath=//html/body/div/main/div/div/div[3]/div[2]/button[1]').click()
    await page.locator('xpath=//html/body/div/main/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/button').click()
    await page.locator('xpath=//html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input').type("gmail/uname/pn") #fb id here
    await page.locator('xpath=//html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input').type("password") #password here
    await page.locator('xpath=//html/body/div[1]/div[2]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button').click()
    print("login sucessfull")
    
    # save the login state
    print("saving")
    await context.storage_state(path=".auth/pi.json")
    print("sucessfully saved to .auth/pi.json")
    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await login(playwright)


# asyncio.run(main())
