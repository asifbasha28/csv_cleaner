# CSV Cleaner

A small Python tool that cleans messy CSV files.

## What it fixes

- Extra spaces around text
- Inconsistent capitalization (`KIRAN` → `Kiran`)
- Short city names (`Hyd` → `Hyderabad`)
- Duplicate rows

## How to run

1. Install pandas: `pip install pandas`
2. Put your file in the same folder and name it `messy.csv`
3. Open a terminal **inside this folder** and run: `python cleaner.py`
4. Your cleaned file is saved as `clean.csv`

## Before

```
name,city,age,joined
Ravi , Hyd,21,12/03/2025
priya,hyderabad,,2025-03-15
Ravi , Hyd,21,12/03/2025
KIRAN,Vizag,23,March 20 2025
sneha,VIZAG ,22,
```

## After

```
name,city,age,joined
Ravi,Hyderabad,21.0,12/03/2025
Priya,Hyderabad,,2025-03-15
Kiran,Vizag,23.0,March 20 2025
Sneha,Vizag,22.0,

```

## Coming next

- Fix age numbers (`21.0` → `21`)
- Fix mixed date formats