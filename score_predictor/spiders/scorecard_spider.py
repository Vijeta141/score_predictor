import scrapy
import csv
global matchNumber
global h,player_set,player_number
player_number=1
h = {}               #Stores key value pair of Url of scorecard and Odi Number       
player_set={}        #Stores key value pair of all playersid and Row number in Players.csv
matchNumber=1

class QuotesSpider(scrapy.Spider):
    global h
    name = "scorecards"
    start_urls=[]
    for current_year in range(2014,2015):
        with open("ListofMatches/List"+str(current_year)+".csv",'r') as f:
            reader = csv.reader(f, delimiter=',')
            rows = list(reader)
        for row in rows:
            h[row[6].split("/")[-1]]=row[7]
            start_urls.append(row[6])


    def parse(self, response):
        global matchNumber,h,player_set,player_number
        f= open("ListofScorecards/"+h[response.url.split("/")[-3]+'.html']+".csv","w+")
        with open("PlayersChangingData.csv","w+") as players_file:              #PlayersChangingData.csv contains records of player at a particular instant
            reader = csv.reader(f, delimiter=',')
            rows=list(reader)
        j=0
        for row in rows:
            player_set[row[0]]=j            #Map playerid to row number i.e j
            j=j+1

        matchNumber=matchNumber+1
        for batsman in response.css('div.scorecard-section.batsmen'):
            for didbat in batsman.css('div.flex-row div.wrap.batsmen'):                     #For batsmen who did bat
                f.write(didbat.css('div.cell.batsmen a::text')[0].extract()+"\t")
                player_linkid=didbat.css('div.cell.batsmen a::attr(href)')[0].extract().split("/")[-1][:-5]           #id of the player, [:-5] used to remove .html 
                rn=player_set[player_linkid]                                                      #rn gives the row number of player in csv
                rows[rn][1]+=1
                rows[rn][2]+=1
                runs=didbat.css('div.cell.runs::text')[0].extract()
                balls=didbat.css('div.cell.runs::text')[-4].extract()                                  #-4 because not all matches contains minutes information
                if didbat.css('div.cell.commentary::text')[0].extract()== 'not out':
                    rows[rn][3]+=1
                rows[rn][4]+=runs
                rows[rn][5]+=balls
                rows[rn][6]=rows[rn][4]/(rows[rn][2]-rows[rn][3])
                rows[rn][7]=rows[rn][4]/rows[rn][5]
                if runs >= 100:
                    rows[rn][9]+=1
                elif runs>=50:
                    rows[rn][8]+=1
                
            for dnb in batsman.css('div.flex-row div.wrap.dnb div.cell a'):                 #For batsmen who did not bat
                f.write(dnb.css('span::text')[0].extract())                                 # Already seperated by comma, so no tab used.
                rows[rn][1]+=1
            f.write("\n")

        #f.write(response.css('div.scorecard-section.bowling td a[data-reactid]::text').extract() + "\t")
