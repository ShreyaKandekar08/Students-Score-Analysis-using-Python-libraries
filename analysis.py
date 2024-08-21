import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_scores.csv")
#print(df.head)

#print(df.describe())

#print(df.info())

#print(df.isnull().sum())

#Drop unnamed column
df = df.drop("Unnamed: 0", axis=1)

#gender distribution
plt.figure(figsize= (5,5))
ax = sns.countplot(data = df, x = "Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()

#from above chart we have analysed that:
#the number of females in the data is more that the number of males

#groupby parent education
gb = df.groupby("ParentEduc").agg({"MathScore":'mean', "ReadingScore":'mean', "WritingScore":'mean'})
print(gb)

#heat map
plt.figure(figsize=(5,5))
sns.heatmap(gb, annot=True)
plt.title("Relationship between Parents Education and Student's Scores")
plt.show()

#from the above chart we have concluded that education of parents 
#have a good impact on students scores

#groupby parent marital status
gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean', "ReadingScore":'mean', "WritingScore":'mean'})
print(gb1)

#heat map
plt.figure(figsize=(5,5))
sns.heatmap(gb1, annot=True)
plt.title("Relationship between Parents Marital Status and Student's Scores")
plt.show()

#from the above chart we have concluded that marital status of parents 
#have a negligible/no impact on students scores

#Box plot to detect extream values
sns.boxplot(data = df, x = "MathScore")
plt.show()

sns.boxplot(data = df, x = "ReadingScore")
plt.show()

#Distribution of Ethnic Group
print(df["EthnicGroup"].unique())
groupA = df.loc[(df["EthnicGroup"] == "group A")].count()
groupB = df.loc[(df["EthnicGroup"] == "group B")].count()
groupC = df.loc[(df["EthnicGroup"] == "group C")].count()
groupD = df.loc[(df["EthnicGroup"] == "group D")].count()
groupE = df.loc[(df["EthnicGroup"] == "group E")].count()

l = ["group A","group B","group C","group D","group E"]
mlist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]
plt.pie(mlist, labels = l, autopct= "%1.2f%%" )
plt.title("Distribution of Ethnic Groups")
plt.show()
