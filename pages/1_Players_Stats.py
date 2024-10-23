import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Top Scorer')


df=pd.read_csv('./euros_2024_shot_map.csv')

Scorer = df[df['shot_outcome'] == 'Goal']

topScorer = Scorer['player'].value_counts().to_dict()


topGoalCount = max(topScorer.values())



L=[]
for key, value in topScorer.items() :
    if value == topGoalCount :
        L.append(key)


ds = pd.DataFrame(L, columns=['Name'])
st.write(ds)



Sl = Scorer['location'].apply(json.loads)

L=[]
for i in Sl : 
    L.append('outside the box' if float(i[0]) < 102 else 'inside the box' )


ld = pd.DataFrame(L)

Goal_dis = ld.value_counts()



labels = ['Inside the Box', 'Outside the Box']
counts = [108, 18]


plt.figure(figsize=(8, 5))
plt.bar(labels, counts, color=['blue', 'orange'])


plt.title('Goals Scored Inside vs. Outside the Box', fontsize=16)
plt.xlabel('Goal Location', fontsize=14)
plt.ylabel('Number of Goals', fontsize=14)


for i, count in enumerate(counts):
    plt.text(i, count + 2, str(count), ha='center', fontsize=12)


plt.ylim(0, max(counts) + 20)  
plt.grid(axis='y', linestyle='--', alpha=0.7)


st.title('Inside the box vs Outside the box')

st.pyplot(plt)