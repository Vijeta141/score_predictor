import scrapy
from ListofCricketers import cricket
import csv
global matchNumber
global h,player_set,player_number,rows
player_number=1
h = {}               #Stores key value pair of Url of scorecard and Odi Number       
player_set={}        #Stores key value pair of all playersid and Row number in Players.csv
matchNumber=1
global x
x=0

# execfile('cricket.py')
"""f1=open("ListofCricketers/cricketer_links.csv","r")
f2=open("ListofCricketers/players.csv","w+")
f2.write("player_id" + "," + "matches" + "," + "innings" + "," + "NO" +","+ "runs" + "," + "BF" + "," + "Ave" + "," + "SR" + "," + "50s" + "," + "100s" + "," + "Ct" + "," + "St" + "," + "Bowl_innings" + "," + "balls" + "," + "runs_given" + "," + "wkts" + ","+ "Ave" + "," + "Eco"+  "," + "SR")
f2.write("\n")
reader = csv.reader(f1, delimiter=',')
rows = list(reader)
for row in rows:
    x = row[0]
    y = x.split(".")[2]
    z = y.split("/")[-1]
    f2.write(z +","+ "0" + ","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0")
    f2.write("\n")"""

class QuotesSpider(scrapy.Spider):
    global matchNumber,h,player_set,player_number,rows,x
    name = "scorecards"
    start_urls=[]

    for current_year in range(2000,2001):
        with open("ListofMatches/List"+str(current_year)+".csv",'r') as f:
            reader2 = csv.reader(f, delimiter=',')
            rows2 = list(reader2)
        for row2 in rows2:
            h[row2[6].split("/")[-1]]=row2[7]
            start_urls.append(row2[6])
            break
            
    with open("ListofCricketers/players.csv","r") as players_file:              #players.csv contains records of player at a particular instant
        reader = csv.reader(players_file, delimiter=',')
        rows=list(reader)
    j=0
    for row in rows:
        player_set[row[0]]=j            #Map playerid to row number i.e j
        j=j+1
    players_file.close()

    def parse(self, response):

        global matchNumber,h,player_set,player_number,rows,x
        
        f= open("ListofScorecards/"+h[response.url.split("/")[-3]+'.html']+".csv","w+")
        #f= open("ListofScorecards/"+'65705'+'.html'+".csv","w+")
        matchNumber=matchNumber+1
        for batsman in response.css('div.scorecard-section.batsmen'):
            for didbat in batsman.css('div.flex-row div.wrap.batsmen'):                     #For batsmen who did bat
                f.write(didbat.css('div.cell.batsmen a::text')[0].extract()+"\t")
                player_linkid=didbat.css('div.cell.batsmen a::attr(href)')[0].extract().split("/")[-1][:-5]           #id of the player, [:-5] used to remove .html 
                rn=player_set[player_linkid]                                                     #rn gives the row number of player in csv
                rows[rn][1]=str(int(rows[rn][1])+1)
                if len(didbat.css('div.cell.commentary a'))==0:
                    if didbat.css('div.cell.commentary::text')[0].extract()== 'absent hurt':
                        continue
                rows[rn][2]=str(int(rows[rn][2])+1)
                runs=didbat.css('div.cell.runs::text')[0].extract()
                balls=didbat.css('div.cell.runs::text')[-4].extract()                                  #-4 because not all matches contains minutes information
                if len(didbat.css('div.cell.commentary a'))==0:
                    if didbat.css('div.cell.commentary::text')[0].extract()== 'not out':
                        rows[rn][3]=str(int(rows[rn][3])+1)
                rows[rn][4]=str(int(rows[rn][4])+int(runs))
                rows[rn][5]=str(int(rows[rn][5])+int(balls))
                if int(rows[rn][2])-int(rows[rn][3])!=0:
                    rows[rn][6]=str(int(rows[rn][4])/(int(rows[rn][2])-int(rows[rn][3])))
                if int(rows[rn][5])!=0:
                    rows[rn][7]=str((int(rows[rn][4])/int(rows[rn][5]))*100)
                if int(runs) >= 100:
                    rows[rn][9]=str(int(rows[rn][9])+1)
                elif int(runs)>=50:
                    rows[rn][8]=str(int(rows[rn][8])+1)
                
            for dnb in batsman.css('div.flex-row div.wrap.dnb div.cell a'):                 #For batsmen who did not bat
                f.write(dnb.css('span::text')[0].extract())                                 # Already seperated by comma, so no tab used.
                player_linkid=dnb.css('::attr(href)')[0].extract().split("/")[-1][:-5]
                rn=player_set[player_linkid]
                rows[rn][1]=str(int(rows[rn][1])+1)
            f.write("\n")

        for bowlers in response.css('div.scorecard-section.bowling'):
            for team_bowler in bowlers.css('tbody tr'):
                f.write(team_bowler.css('td a::text')[0].extract() +"," + "\t" )
                player_linkid=team_bowler.css('td a::attr(href)')[0].extract().split("/")[-1][:-5]
                rn=int(player_set[player_linkid])
                rows[rn][12]=str(int(rows[rn][12])+1)
                #print(team_bowler.css('td::text')[0].extract())
                tot_balls=str(float(team_bowler.css('td::text')[0].extract()))
                balls=int(tot_balls.split(".")[0])*6 + int(tot_balls.split(".")[1])
                runs=int(team_bowler.css('td::text')[2].extract())
                wickets=int(team_bowler.css('td::text')[3].extract())
                rows[rn][13]=str(int(rows[rn][13])+int(balls))
                rows[rn][14]=str(int(rows[rn][14])+int(runs))
                rows[rn][15]=str(int(rows[rn][15])+int(wickets))
                if int(rows[rn][15])!=0:
                    rows[rn][16]=str(int(rows[rn][14])/int(rows[rn][15]))
                    rows[rn][18]=str(int(rows[rn][13])/int(rows[rn][15]))
                if int(rows[rn][13])!=0:
                    rows[rn][17]=str((int(rows[rn][14])/int(rows[rn][13]))*6)
                    
            f.write("\n")
        
       
        my_new_list = open('ListofCricketers/players.csv', 'w', newline = '')
        csv_writer = csv.writer(my_new_list)
        csv_writer.writerows(rows)
        my_new_list.close()    

