import csv
s=set()
m2={}

for current_year in range(2000,2019):
    with open("ListofMatches/List"+str(current_year)+".csv",'r') as f:
        reader = csv.reader(f, delimiter=',')
        rows = list(reader)
    print(rows[1])
    for row in rows:
    	s.add(row[1])
    	s.add(row[0])
    
for s1 in s:
	m2[s1]=0

for current_year in range(2000,2019):
    with open("ListofMatches/List"+str(current_year)+".csv",'r') as f:
        reader = csv.reader(f, delimiter=',')
        rows = list(reader)
    for row in rows:
    	j=j+1
    	m2[row[1]]=m2[row[1]]+1
    	m2[row[0]]=m2[row[0]]+1

print(m2)
print(j)
