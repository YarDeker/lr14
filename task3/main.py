import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

with open('average-marks.json', 'r', encoding='utf-8') as f:
    lab12_data = json.load(f)

average_scores = [entry['Середня оцінка'] for entry in lab12_data]
scores_count = pd.Series(average_scores).value_counts().sort_index()
labels = scores_count.index.tolist()
values = scores_count.values

plt.figure(figsize=(10, 7))
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=plt.cm.Set3(np.linspace(0, 1, len(labels))))
plt.title("Percentage of Average students marks")
plt.show()
