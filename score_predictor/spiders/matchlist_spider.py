import scrapy
global match_count
match_count=0
class QuotesSpider(scrapy.Spider):
    name = "matches"
    start_urls=[]
    
    for i in range(1985, 2019):
       start_urls.append('http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id='+str(i)+';type=year')
       

    def parse(self, response):
        global match_count
        current_year=response.url.split("=")[-2]
        f= open("ListofMatches/List"+current_year[:4]+".csv","w+")
        for match in response.css('tr.data1'):            
                if match.css('td::text')[0].extract()!='no result' and match.css('td::text')[0].extract()!='tied':      
                    if match.css('td')[3].extract()=='<td class="left" nowrap></td>' :                              #Matches with a winner but no margin (abandoned)
                        f.write(        
                        match.css('td.left a.data-link::text')[0].extract()+","
                        + match.css('td.left a.data-link::text')[1].extract()+","
                        + match.css('td.left a.data-link::text')[2].extract()+","
                        + " ,"
                        + match.css('td.left a.data-link::text')[3].extract()+","
                        + match.css('td::text')[0].extract().split(",")[0]+"," 
                        + "http://stats.espncricinfo.com"+ match.css('a::attr(href)')[4].extract()+","  
                        + match.css('a.data-link::text')[4].extract()+"\n")
                        match_count+=1
                    else:                                                                                           #Matches with a winner
                        f.write(        
                        match.css('td.left a.data-link::text')[0].extract()+","
                        + match.css('td.left a.data-link::text')[1].extract()+","
                        + match.css('td.left a.data-link::text')[2].extract()+","
                        + match.css('td.left::text')[0].extract()+","
                        + match.css('td.left a.data-link::text')[3].extract()+","
                        + match.css('td::text')[1].extract().split(",")[0]+","
                        +"http://stats.espncricinfo.com"+ match.css('a::attr(href)')[4].extract()+","
                        + match.css('a.data-link::text')[4].extract()+"\n")
                        match_count+=1
                else:                                                                                               #Matches with no winner (tied or no result)
                    f.write(
                    match.css('td.left a.data-link::text')[0].extract()+","
                    + match.css('td.left a.data-link::text')[1].extract()+","
                    + match.css('td.left::text')[0].extract()+","
                    +" ,"
                    + match.css('td.left a.data-link::text')[2].extract()+","
                    + match.css('td::text')[1].extract().split(",")[0]+","
                    +"http://stats.espncricinfo.com"+ match.css('a::attr(href)')[3].extract()+","
                    +match.css('a.data-link::text')[3].extract()+"\n")
                    match_count+=1
