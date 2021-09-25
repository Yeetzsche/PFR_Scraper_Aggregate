import PFR_Scrape_Aggregate as pfr

year = 2020
week = 17
multiple_weeks = True

#Call the tools

pfr.readData(year=year,week=week,multiple_weeks=multiple_weeks)
pfr.buildAggregate(year=year,week=week,multiple_weeks=multiple_weeks)
