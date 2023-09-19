import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    # browser = await playwright.chromium.launch(headless=False)
    browser = await playwright.chromium.launch(headless=True, args=["--headless=new",], ignore_default_args=["--mute-audio"])
    while True:
        try:
            context = await browser.new_context(storage_state=".auth/pi.json")
            break
        except:
            from piAiLogin import login
            async with async_playwright() as playwright:
                    await login(playwright)
            continue
    page = await context.new_page()
    await page.goto("https://pi.ai/talk")
    textAreaXpath="//html/body/div/main/div/div/div[1]/div[4]/div/div[2]/div/div/textarea"
    sendButtonXpath="//html/body/div/main/div/div/div[1]/div[4]/div/div/div/button"
    # micButtonXpath="//html/body/div/main/div/div/div[2]/div/div[2]/button"
    AnswerXpath = "//html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]"
    # voiceXpath="//html/body/div/main/div/div/div[2]/div/div[2]/button[3]"
    mic='off'
    while True:
        q = input('Q: ')
        prevAns = await page.locator(f'xpath={AnswerXpath}').all_text_contents()
        if q == "QUIT":
            break
        # await page.reload()
        txtArea = page.locator(f'xpath={textAreaXpath}')
        await txtArea.type(q)
        sendBtn = page.locator(f'xpath={sendButtonXpath}')
        await sendBtn.click()
        await asyncio.sleep(1.5)
        # micBtn = page.locator(f'xpath={micButtonXpath}')
        if mic == "off":
            button = page.locator('//html/body/div/main/div/div/div[2]/div/div[2]/button')
            await button.click()
            try:
                voice = page.locator('//html/body/div/main/div/div/div[2]/div/div[2]/button[3]')
                await voice.click()
                await button.click()
            except:
                pass
            mic = "on"
        await page.wait_for_selector('//html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]')
        Answer = page.locator(f'xpath={AnswerXpath}')
        reply = await Answer.all_text_contents()
        while prevAns == reply:
            await page.wait_for_selector('//html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div')
            Answer = page.locator(f'xpath={AnswerXpath}')
            reply = await Answer.all_text_contents()
            if prevAns != reply:
                break
        while True:
            Xreply = reply
            await asyncio.sleep(1)
            Answer = page.locator(f'xpath={AnswerXpath}')
            reply = await Answer.all_text_contents()
            if Xreply == reply:
                break
        print('A:',reply)
        
    # ---------------------
    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
