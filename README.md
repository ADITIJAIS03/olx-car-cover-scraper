
# OLX Car Cover Scraper

This Python script scrapes search results from [OLX India](https://www.olx.in/items/q-car-cover) for the query **"Car Cover"** and stores the listing data in a CSV file.

## Features

- Scrapes titles, prices, locations, and links of listings.
- Saves data in a structured `CSV` file.
- Easy to run and modify for similar OLX search terms.

## Requirements

Install the required libraries before running:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone or download the script.
2. Run the script:

```bash
python olx_car_cover_scraper.py
```

3. The results will be saved in `olx_car_cover_results.csv`.

## Output Format

The CSV file will contain:

- Title
- Price
- Location
- Link

## Notes

- The script scrapes data from the first page of OLX results.
- If OLX updates its site structure or adds bot protection, the script may need adjustments.

---

Created by [Aditi Jaiswal](https://github.com/ADITIJAIS03)
