from playwright.sync_api import sync_playwright
import time

seeds = range(70, 80)
total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/playwright-qa/index.html?seed={seed}"
        page.goto(url, wait_until="domcontentloaded")

        time.sleep(3)

        values = page.locator(".value").all()

        for v in values:
            try:
                total += float(v.inner_text())
            except:
                pass

    browser.close()

print("TOTAL_SUM =", total)
