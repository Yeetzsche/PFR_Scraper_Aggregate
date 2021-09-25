# Pro Football Reference Game Data Webscraper
Copyright Yeetzsche

### This is a simple Pro Football Reference Webscraper that can either collect all game data per week of a given year, or collect all that data and then aggregate it into a single .csv file per week.

### Example usage:
```Bash
import PFR_Scrape_Aggregate as pfr

year = 2021
week = 2
multiple_weeks = True

#Call the tools
pfr.readData(year=year,week=week,multiple_weeks=multiple_weeks)

for i in range(1,week+1):
    
    pfr.buildAggregate(year,i)

```
