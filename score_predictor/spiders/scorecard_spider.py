import scrapy
import csv
global matchNumber
matchNumber=1 
class QuotesSpider(scrapy.Spider):
    name = "scorecards"
    start_urls=[]
    for current_year in (2014,2015):
        with open("ListofMatches/List"+str(current_year)+".csv",'r') as f:
            reader = csv.reader(f, delimiter=',')
            rows = list(reader)
        for row in rows:
            start_urls.append(row[6])

       
    def parse(self, response):
        global matchNumber
        f= open("ListofScorecards/Match"+response.css('div.cscore_info-overview::text')[0].extract().split(",")[-1]+".csv","w+")
        matchNumber=matchNumber+1
        for batsman in response.css('div.scorecard-section.batsmen'):
            for didbat in batsman.css('div.flex-row div.wrap.batsmen'):                     #For batsmen who did bat
                f.write(didbat.css('div.cell.batsmen a::text')[0].extract()+"\t")
            for dnb in batsman.css('div.flex-row div.wrap.dnb div.cell a'):                 #For batsmen who did not bat
                f.write(dnb.css('span::text')[0].extract())                                 # Already seperated by comma, so no tab used.
            f.write("\n")
