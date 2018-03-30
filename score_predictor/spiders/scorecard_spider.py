import scrapy
import csv
global matchNumber
global h
h = {}
matchNumber=1 

class QuotesSpider(scrapy.Spider):
    global h
    name = "scorecards"
    start_urls=[]
    for current_year in (2014,2015):
        with open("ListofMatches/List"+str(current_year)+".csv",'r') as f:
            reader = csv.reader(f, delimiter=',')
            rows = list(reader)
        for row in rows:
            h[row[6].split("/")[-1]]=row[7]
            start_urls.append(row[6])

       
    def parse(self, response):
        global matchNumber,h
        print ("urlurl="+response.url.split("/")[-3])
        f= open("ListofScorecards/"+h[response.url.split("/")[-3]+'.html']+".csv","w+")
        matchNumber=matchNumber+1
        for batsman in response.css('div.scorecard-section.batsmen'):
            for didbat in batsman.css('div.flex-row div.wrap.batsmen'):                     #For batsmen who did bat
                f.write(didbat.css('div.cell.batsmen a::text')[0].extract()+"\t")
            for dnb in batsman.css('div.flex-row div.wrap.dnb div.cell a'):                 #For batsmen who did not bat
                f.write(dnb.css('span::text')[0].extract())                                 # Already seperated by comma, so no tab used.
            f.write("\n")
