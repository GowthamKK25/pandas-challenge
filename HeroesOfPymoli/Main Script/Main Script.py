#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[3]:


# Connected path directly in file because resources folder did not work for me

pyheros_path = "purchase_data.csv"

pyheros_df = pd.read_csv(pyheros_path)
pyheros_df.head()


# In[4]:


#Player Count 

PlayerCount = len(pyheros_df["SN"].unique()) 

TotalPlayerframe = pd.DataFrame({"Total Players":[PlayerCount]})
TotalPlayerframe


# In[5]:


#Purchasing Analysis (Total) 

UniqueItems = len(pyheros_df["Item Name"].unique()) 
Totalpurchases = len(pyheros_df["Purchase ID"])
AveragePurPrice = round(pyheros_df["Price"].sum() / Totalpurchases,2) 
TotalRev = pyheros_df["Price"].sum()


TotalFrame = pd.DataFrame(
    {"Number of Unique Items": [UniqueItems],
     "Average Price": [AveragePurPrice],
     "Total Revenue": [TotalRev], 
     "Number of Purchases":[Totalpurchases]
     }
)


TotalFrame['Average Price'] = TotalFrame['Average Price'].map("${:.2f}".format) 
TotalFrame[ "Total Revenue"] = TotalFrame[ "Total Revenue"].map("${:.2f}".format) 



TotalFrame


# In[6]:


#Gender Demographics
gender = pyheros_df.groupby("Gender")
totalgender = gender.nunique()["SN"]
percentofplayers = round((totalgender / PlayerCount) * 100,2) 

GenderdemFrame = pd.DataFrame({ "Gender Count" : totalgender, "Percentage": percentofplayers })

GenderdemFrame.index.name = None

GenderdemFrame["Percentage"] = GenderdemFrame["Percentage"].map("{:.2f}%".format)



GenderdemFrame


# In[7]:


#Purchasing Analysis (Gender)  
Purchasecount = gender["Purchase ID"].nunique()
totalspending = gender["Price"].sum()
averagespendinggen = round(totalspending / totalgender,2) 
averagespending = round(totalspending / Purchasecount,2) 

GenderAnalysisFrame = pd.DataFrame({ "Purchase Count" : Purchasecount, "Total Spending": totalspending, "Average Purchase Price": averagespending, "Average Spending per Person": averagespendinggen})


GenderAnalysisFrame["Total Spending"] = GenderAnalysisFrame["Total Spending"].map("${:.2f}".format)
GenderAnalysisFrame["Average Purchase Price"] = GenderAnalysisFrame["Average Purchase Price"].map("${:.2f}".format)
GenderAnalysisFrame["Average Spending per Person"] =GenderAnalysisFrame["Average Spending per Person"].map("${:.2f}".format)


GenderAnalysisFrame


# In[8]:


#Age Demographics 
bins = [0,9,14,19,24,29,34,39,100]
age = ['<10','10-14','15-19','20-24',"25-29","30-34","35-39","40+"]
pyheros_df["age"] = pd.cut(pyheros_df["Age"],bins,labels = age)
demographic = pyheros_df.groupby(pyheros_df["age"])
totalcount = demographic.nunique()["SN"] 
percent = round((totalcount/ PlayerCount) * 100,2)  

AgeFrame = pd.DataFrame({ "Total Count" : totalcount, "Percent of players":percent })
AgeFrame.index.name = None


AgeFrame["Percent of players"] = AgeFrame["Percent of players"].map("{:.2f}%".format)

AgeFrame


# In[9]:


#Purchasing Analysis (Age) 
Purchasecountbin = demographic["Purchase ID"].nunique()
totalspendingbin  = demographic["Price"].sum()
averagebin = round(totalspendingbin / totalcount, 2)
avgpurpricebin = round(totalspendingbin / Purchasecountbin, 2) 

AgeAnalysisFrame = pd.DataFrame({ "Purchase Count" : Purchasecountbin, "total Purchase Value":totalspendingbin,"Average Purchase Value": avgpurpricebin, "Average Purchase Value per Person": averagebin})
AgeFrame.index.name = None


AgeAnalysisFrame["total Purchase Value"] = AgeAnalysisFrame["total Purchase Value"].map("${:.2f}".format)
AgeAnalysisFrame["Average Purchase Value"] = AgeAnalysisFrame["Average Purchase Value"].map("${:.2f}".format)
AgeAnalysisFrame["Average Purchase Value per Person"] = AgeAnalysisFrame["Average Purchase Value per Person"].map("${:.2f}".format)


AgeAnalysisFrame 


# In[10]:


#Top Spenders 

Players = pyheros_df.groupby(pyheros_df["SN"]) 
PlayerTotal = Players["Price"].nunique()
TotalPlayerspending = Players["Price"].sum()
AvgPlayerSpending = round(TotalPlayerspending / PlayerTotal, 2)
PurchaseCount = Players["Purchase ID"].nunique()

TopSpenders = pd.DataFrame({"Amount of Purchases": PurchaseCount, "Average Purchase Price" : AvgPlayerSpending, "Total Player Spending":TotalPlayerspending })
TopSpenders.index.name = None
TopSpenders.head()

TopSpenders.nlargest(5,["Amount of Purchases","Total Player Spending"]) 

TopSpenders["Average Purchase Price"] = TopSpenders["Average Purchase Price"].map("${:.2f}".format)
TopSpenders["Total Player Spending"] = TopSpenders["Total Player Spending"].map("${:.2f}".format) 

TopSpenders.nlargest(5,["Amount of Purchases"]) 


# In[81]:


# Most Popular items 
Itemid = pyheros_df.groupby(["Item ID","Item Name"])
Itemname = Itemid["Item Name"].unique()
PurchaseTotal = Itemid["Purchase ID"].nunique()


Totalval = Itemid["Price"].sum() 

Maybe = round(Totalval/ PurchaseTotal,2 )

TopItems = pd.DataFrame({ "Purchase Count" : PurchaseTotal, "Item Price":Maybe, "Total Purchase Value": Totalval })


TopItems = TopItems.sort_values(["Purchase Count"], ascending=False)

TopItems["Item Price"] = TopItems["Item Price"].map("${:.2f}".format) 
TopItems["Total Purchase Value"] = TopItems["Total Purchase Value"].map("${:.2f}".format)  


TopItems.head()


# In[ ]:


# Most Profitable items 


Itemname = Itemid[("Item Name")].unique()
PurchaseTotal = Itemid["Purchase ID"].nunique()


Totalval = Itemid["Price"].sum() 

Maybe = round(Totalval/ PurchaseTotal,2 )

TopItems = pd.DataFrame({"Purchase Count": PurchaseTotal, "Item Price":Maybe, "Total Purchase Value": Totalval })



TopItems = TopItems.sort_values(["Total Purchase Value","Purchase Count"], ascending=False)

TopItems["Item Price"] = TopItems["Item Price"].map("${:.2f}".format) 
TopItems["Total Purchase Value"] = TopItems["Total Purchase Value"].map("${:.2f}".format)  


TopItems.head()


# In[83]:


# Most Profitable items 


Itemname = Itemid[("Item Name")].unique()
PurchaseTotal = Itemid["Purchase ID"].nunique()


Totalval = Itemid["Price"].sum() 

Maybe = round(Totalval/ PurchaseTotal,2 )

TopItems = pd.DataFrame({"Purchase Count": PurchaseTotal, "Item Price":Maybe, "Total Purchase Value": Totalval })



TopItems = TopItems.sort_values(["Total Purchase Value","Purchase Count"], ascending=False)

TopItems["Item Price"] = TopItems["Item Price"].map("${:.2f}".format) 
TopItems["Total Purchase Value"] = TopItems["Total Purchase Value"].map("${:.2f}".format)  


TopItems.head()


# Conclusions: Three trends which I have observed from the data is firstly that Final Critic is both the most popular and profitable item out of all the items, thus implying it is very good in the game both cosemetically and for usage. Secondly, the majority of people (44%) who play this game are in the age group of 20-24 and most players are adults with less than 25% of players being less that 20 years old. Finally, this game is played mainly by males with 84% of the game population being a male based population.
