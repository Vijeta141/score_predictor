import scrapy
import csv
class QuotesSpider(scrapy.Spider):
    name = "scorecards"
    start_urls=[]
    for current_year in (2000,2003):
        with open("ListofMatches/List"+str(current_year)+".csv",'r') as f:
            reader = csv.reader(f, delimiter=',')
            rows = list(reader)
        for row in rows:
            start_urls.append('row[6]')
       
    def parse(self, response):
        #f= open("Scorecard/List"+".csv","w+")
        
