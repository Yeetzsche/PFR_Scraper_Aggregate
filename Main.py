import PFR_Scrape_Aggregate as pfr

year = 2021
week = 2
multiple_weeks = True

#Call the tools
pfr.readData(year=year,week=week,multiple_weeks=multiple_weeks)

for i in range(1,week+1):
    
    pfr.buildAggregate(year,i)

