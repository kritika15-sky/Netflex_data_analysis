# Netflix Cleaned Dataset (`netflix_cleaned.csv`)

This repository contains the cleaned and standardized Netflix catalog dataset (`netflix_cleaned.csv`), prepared for exploratory data analysis (EDA), content trend visualization, and recommendation modeling.

## Project Structure

```text
netflix_cleaned/
├── README.md/
│   └── README.md
├── REQUIRMENT.TXT/
│   └── REQUIRMENT.TXT
└── netflix_cleaned.csv
```

## Dataset Overview

* **File Name**: `netflix_cleaned.csv`
* **Total Records**: 8,807 titles (6,131 Movies and 2,676 TV Shows)
* **Total Columns**: 10
* **Release Year Range**: 1925 – 2021

### Column Schema

| Column | Data Type | Description |
| :--- | :--- | :--- |
| `content_type` | `string` | Category of the title (`Movie` or `TV Show`) |
| `title` | `string` | Name of the movie or TV show |
| `director` | `string` | Director(s) of the title (`Unknown` where unavailable) |
| `cast_members` | `string` | Main cast members (`Unknown` where unavailable) |
| `country` | `string` | Country or countries of production (`Unknown` where unavailable) |
| `date_added_to_netflix` | `date (YYYY-MM-DD)` | Date the title was added to Netflix (`98` missing entries) |
| `release_year` | `integer` | Original theatrical or broadcast release year |
| `rating` | `string` | Maturity rating (e.g., `TV-MA`, `PG-13`, `TV-14`) |
| `duration` | `string` | Runtime in minutes for Movies (`90 min`) or seasons for TV Shows (`2 Seasons`) |
| `genres` | `string` | Comma-separated Netflix catalog genres/categories |

## Data Cleaning & Standardization Applied

* Standardized column names (`type` → `content_type`, `cast` → `cast_members`, `date_added` → `date_added_to_netflix`, `listed_in` → `genres`).
* Imputed missing values in `director`, `cast_members`, and `country` with `'Unknown'`.
* Standardized `date_added_to_netflix` into ISO date format (`YYYY-MM-DD`).
* Dropped raw identifier (`show_id`) and free-text synopsis (`description`) fields for streamlined tabular analysis.

## Setup & Usage

1. Install the required Python dependencies:
   ```bash
   pip install -r REQUIRMENT.TXT/REQUIRMENT.TXT
   ```
2. Load the dataset in Python:
   ```python
   import pandas as pd

   df = pd.read_csv("netflix_cleaned.csv")
   print(df.info())
   ```
