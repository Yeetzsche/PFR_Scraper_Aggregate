# Pro Football Reference Game Data Webscraper
Code Copyright Yeetzsche

### This is a simple Pro Football Reference Webscraper that can either collect all game data per week of a given year, or collect all that data and then aggregate it into a single .csv file per week.

### When using this tool, please be kind to the folks at Pro Football Reference and try not to grab too much of their data all at once which could inadvertently cause network problems for them. They are kind enough to offer it for free, so play nice.
Please see https://www.sports-reference.com/data_use.html for more details about PFR's data policy.

### Example usage:
```Bash
import PFR_Scrape_Aggregate as pfr

year = 2020
week = 17
multiple_weeks = True

#Call the tools

pfr.readData(year=year,week=week,multiple_weeks=multiple_weeks)
pfr.buildAggregate(year=year,week=week,multiple_weeks=multiple_weeks)

```
