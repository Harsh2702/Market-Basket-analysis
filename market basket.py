
import pandas as pd
import numpy as np
from apyori import apriori


data = pd.read_csv('D:\datasets\store_data.csv')
# item = data['Item(s)']
# item = item[:40]
#print(data.shape)
# d1 = data.drop(['Item(s)'], axis = 1)
#d1 = data.loc[:39]
#len(d1)

records = []
for i in range(0,len(data)):
        records.append([str(data.values[i,j]) for j in range(0,20)]) #32 for gro.csv
#print(records)
#len(records)

#for gro.csv
# a = records
# b = item
# c = []
# for i in range(0,len(item)):
#     for j in range(0,b[i]):
#         c.append(a[i])
#len(c)

#model building
asrule = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=1.5, min_length=2)
asres = list(asrule)

# asres[0]

antecedent = []
consequent = []
support = []
confidence = []
lift = []
p = 1


for item in asres:                                        

    # first index of the inner list
    # Contains base item and add item
    print(p)
    p = p+1
    pair = item[0] 
    items = [x for x in pair]
     
    print("Rule: " ,items[0] , " -> " , items[1])
    antecedent.append(str(items[0]))
    consequent.append(str(items[1]))
    #second index of the inner list
    print("Support: " + str(item[1]))
    support.append(str(item[1]))
    #third index of the list located at 0th
    #of the third index of the inner list
    confidence.append(str(item[2][0][2]))
    lift.append(str(item[2][0][3]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
  

final_res = pd.DataFrame({'antecedent':antecedent,'conesequent':consequent,'support':support,'confidence':confidence,'lift':lift})


result = final_res.sort_values(by=['confidence'],ascending=False).dropna()
print(result)

