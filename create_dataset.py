import nltk
import pandas as pd
from nltk.corpus import names

nltk.download('names')

data = []

for name in names.words('male.txt'):
    data.append([name, 'Male'])

for name in names.words('female.txt'):
    data.append([name, 'Female'])

df = pd.DataFrame(data, columns=['Name', 'Gender'])

df.to_csv('gender_dataset.csv', index=False)

print(df.shape)