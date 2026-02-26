from playwright.sync_api import sync_playwright
import time

seeds = range(70,80)
total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/playwright-qa/index.html?seed={seed}"
        page.goto(url)

        page.wait_for_selector("table")   # wait for table
        time.sleep(2)                     # wait for numbers to load

        cells = page.query_selector_all("td")

        for c in cells:
            try:
                total += float(c.inner_text())
            except:
                pass

    browser.close()

print("TOTAL_SUM =", total)
