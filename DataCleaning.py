#importing relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

#importing the data 
resume_data = pd.read_csv('Documents/ResumeScanner/ResumeDataset.csv', encoding='utf-8')
resume_data.head()

#printing the unique profiles
print(resume_data['Category'].unique())

print('Count of different profiles:-')
print(resume_data['Category'].value_counts())


#plotting the count of different job profiles
import seaborn as sns
plt.figure(figsize=(15,15))
plt.xticks()
sns.countplot(y = 'Category', data = resume_data)

#creating a pie chart to visualize the distribution of job profiles
labels = resume_data.Category.unique()
data = resume_data.Category.value_counts()
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=labels, autopct='%1.1f%%')

#cleaning the data 
import re
def CleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', '', resumeText)  #removing URLs 
    resumeText = re.sub('RT|cc', '', resumeText)    #removing RT|cc
    resumeText = re.sub('[^\w\s]', '', resumeText)  #removing punctuation
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText)  #removing non-ASCII characters
    return resumeText

resume_data['cleaned_resume'] = resume_data.Resume.apply(lambda x: CleanResume(x))
resume_data.drop('Resume', axis=1, inplace=True)

resume_data.to_csv('Documents/ResumeScanner/CleanedData.csv', encoding='utf-8')
