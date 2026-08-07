import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Listen for console events
        page.on("console", lambda msg: print(f"Console: {msg.type} - {msg.text}"))
        
        print("Navigating to the calculator...")
        await page.goto("http://localhost:5173/calculadora-simples-nacional.html")
        await page.wait_for_timeout(3000)
        
        await browser.close()

asyncio.run(main())
