#MapPlot.py
#Name:Nomaan Ahmed
#Date:4/20/2025
#Assignment:Lab 10 

import coffee
import pandas
import matplotlib.pyplot as plt

coffee = coffee.get_coffee()
years = []
scores = []
#print(coffee[0]["Data"]["Scores"]["Total"])

for bean in coffee:
    year = bean["Year"]
    score = bean["Data"]["Scores"]["Total"]
    years.append(year)
    scores.append(score)
    #print(year, score)

df = pandas.DataFrame([{"Year": years,
                        "Score": scores}])

print(df)
df.plot(kind = 'scatter', x = 'Year', y = 'Score')
plt.plot(years, scores)
plt.savefig("output")
