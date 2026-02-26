from playwright.sync_api import sync_playwright

seeds = range(70,80)
total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/playwright-qa/index.html?seed={seed}"
        page.goto(url)
        cells = page.query_selector_all("td")

        for c in cells:
            try:
                total += float(c.inner_text())
            except:
                pass

    browser.close()

print("TOTAL_SUM =", total)
