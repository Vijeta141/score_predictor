import scrapy
import csv
global matchNumber
global h
global links
h = {}
matchNumber=1
links = set()

class QuotesSpider(scrapy.Spider):
    global h
    name = "scorecards_second"
    start_urls=[]
    for current_year in (1985,2018):
       with open("ListofMatches/List"+str(current_year)+".csv",'r') as f:
           reader = csv.reader(f, delimiter=',')
           rows = list(reader)
       for row in rows:
           h[row[6].split("/")[-1]]=row[7]
           start_urls.append(row[6])


    def parse(self, response):

        f=open("ListofCricketers/cricketer_links.csv","w+")
        for batsman in response.css('div.scorecard-section.batsmen'):
            for didbat in batsman.css('div.flex-row div.wrap.batsmen'):                     #For batsmen who did bat
                links.add(didbat.css('div.cell.batsmen a::attr(href)')[0].extract())
            for dnb in batsman.css('div.flex-row div.wrap.dnb div.cell a'):                 #For batsmen who did not bat
                links.add(dnb.css('a::attr(href)')[0].extract())                                 # Already seperated by comma, so no tab used.

        for bowlers in response.css('div.scorecard-section.bowling'):
            for team_bowler in bowlers.css('td a[data-reactid]'):
                links.add(team_bowler.css('a::attr(href)')[0].extract())

        for l in links :
            f.write(l + "\n")