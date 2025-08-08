import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Sample dataset (you can replace this with your actual dataset)
data = {
    'sleep': [1, 0, 1, 1, 0],
    'appetite': [1, 1, 0, 0, 1],
    'mood': [0, 0, 1, 1, 0],
    'suicidal_thoughts': [0, 1, 0, 1, 0],
    'label': ['general', 'emergency', 'moderate', 'emergency', 'general']
}

df = pd.DataFrame(data)

X = df[['sleep', 'appetite', 'mood', 'suicidal_thoughts']]
y = df['label']

model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
