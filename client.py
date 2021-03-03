import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    browser1 = await playwright.chromium.connect("ws://127.0.0.1:44445/c8a08576f945965f2e45d8f567479b31")
    page1 = await browser1.new_page()
    await page1.goto("https://example.com")
    await browser1.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
