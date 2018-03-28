import scrapy
current_year=2015
class QuotesSpider(scrapy.Spider):
    name = "matches"
    start_urls=[]
    
    for i in range(2000, 2019):
       start_urls.append('http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id='+str(i)+';type=year')
       

    def parse(self, response):
        current_year=response.url.split("=")[-2]
        f= open("ListofMatches/List"+current_year[:4]+".txt","w+")
        for match in response.css('tr.data1'):
                if match.css('td.left::text')[0].extract()!='no result' and match.css('td.left::text')[0].extract()!='tied':
                        f.write(
                        "Team1:"  + match.css('td.left a.data-link::text')[0].extract()+","
                        "Team2:"  + match.css('td.left a.data-link::text')[1].extract()+","
                        "Winner:" + match.css('td.left a.data-link::text')[2].extract()+","
                        "Margin:" + match.css('td.left::text')[0].extract()+","
                        "Ground:" + match.css('td.left a.data-link::text')[3].extract()+","
                        "Match Date:" + match.css('td::text')[1].extract()+","
                        "Scorecard Link:" + match.css('a::attr(href)')[4].extract()+"\n")
                    
                else:
                        f.write(
                        "Team1:"  + match.css('td.left a.data-link::text')[0].extract()+","
                        "Team2:"  + match.css('td.left a.data-link::text')[1].extract()+","
                        "Winner:" + match.css('td.left::text')[0].extract()+","
                        "Margin:" +" ,"
                        "Ground:" + match.css('td.left a.data-link::text')[2].extract()+","
                        "Match Date:" + match.css('td::text')[1].extract()+","
                        "Scorecard Link:" + match.css('a::attr(href)')[3].extract()+"\n")
