from playwright.sync_api import sync_playwright
import time

seeds = range(70, 80)
total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/playwright-qa/index.html?seed={seed}"
        page.goto(url, wait_until="networkidle")

        time.sleep(3)   # wait for JS to render numbers

        cells = page.query_selector_all("td")

        for c in cells:
            try:
                total += float(c.inner_text().strip())
            except:
                pass

    browser.close()

print("TOTAL_SUM =", total)
