import scrapy
import csv

class CricketSpider(scrapy.Spider):
    name="cricketers"
    start_urls=[]

    for i in range(1, 10):
       start_urls.append('http://www.espncricinfo.com/ci/content/player/caps.html?country='+str(i)+';class=2')


    def parse(self,response):
        country = response.url.split(";")
        number = country[0].split("=")[-1]
        f=open("ListofCricketers/list"+number+".csv","w+")
        card = response.css('div.ciPlayerbycapstable')[0]

        for player in card.css('li.sep'):
            f.write(
                player.css('li.ciPlayername a::text')[0].extract()+","
                +"http://www.espncricinfo.com"+player.css('li.ciPlayername a::attr(href)')[0].extract()
                +("\n")
            )