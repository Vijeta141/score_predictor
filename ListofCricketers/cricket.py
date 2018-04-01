import scrapy
import csv


def main():
    f1=open("cricketer_links.csv","r")
    f2=open("players.csv","w+")
    f2.write("player_id" + "," + "matches" + "," + "innings" + "," + "runs" + "," + "BF" + "," + "Ave" + "," + "SR" + "," + "50s" + "," + "100s" + "," + "Ct" + "," + "St" + "," + "NO" + "," + "Bowl_innings" + "," + "balls" + "," + "runs_given" + "," + "wkts" + ","+ "Ave" + "," + "Eco"+  "," + "SR")
    f2.write("\n")
    reader = csv.reader(f1, delimiter=',')
    rows = list(reader)
    for row in rows:
        x = row[0]
        y = x.split(".")[2]
        z = y.split("/")[-1]
        f2.write(z +","+ "0" + ","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0"+","+"0")
        f2.write("\n")




if __name__ == "__main__":
    main()