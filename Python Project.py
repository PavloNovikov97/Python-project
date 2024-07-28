#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd 
import math 
import numpy as np #importing pandas, math and numpy
df = pd.read_csv('survey_results_public.csv') #importing dataframe
schema = pd.read_csv('survey_results_schema.csv') #importing schema


# In[3]:


df.head()


# In[5]:


df.ResponseId.nunique() #show number of unique values in ResponseID


# In[6]:


df.ResponseId.max() #show the max value from ResponseID. It should work since values are not repeating and are in order


# <h1>TASK 1 RESULT -> Showing how many respondents answered the survey</h1>

# In[8]:


questions_from_survey = df.columns #show questions from survey
questions_from_schema = schema.qname #show questions from schema
print(questions_from_survey)
print(questions_from_schema)


# In[9]:


both = set(questions_from_schema) & set(questions_from_survey) #turning questions_from_schema and questions_from_survey into sets. 'both' shows which questions are in both sets


# In[10]:


print(both)


# In[11]:


df.dropna(subset = both).shape[0] #Remove all rows with NULL values from the subset 'both' and counts number of rows with 'shape'


# In[ ]:


#how many people answered questions


# In[12]:


survey_only = set(questions_from_survey).difference(set(questions_from_schema)) #selecting questions that are NOT in 'schema'


# In[13]:


print(survey_only)


# In[14]:


print(sorted(survey_only))# print the questions and sort them


# In[17]:


df.loc[:, df.columns.str.contains('AIDev')].head(10) #show answers in the questions that contain 'AIDev'


# In[19]:


df['AIDevHaveWorkedWith'] = df['AIDevHaveWorkedWith'].astype('string') #turning value into a string
df['AIDevWantToWorkWith'] = df['AIDevWantToWorkWith'].astype('string') #turning value into a string


# In[20]:


df['AIDev'] = df['AIDevHaveWorkedWith'] + df['AIDevWantToWorkWith'] #combining the 2 columns with answers into a new column 'AIDev' 


# In[23]:


df.AIDev


# In[24]:


#must do this for all different questions and then run 'both' and 'dropna' from [11]


# In[25]:


df.loc[:, df.columns.str.contains('AINext')].head(10)


# In[26]:


df['AINextVery different'] = df['AINextVery different'].astype('string') #turning value into a string
df['AINextNeither different nor similar'] = df['AINextNeither different nor similar'].astype('string') #turning value into a string
df['AINextSomewhat similar'] = df['AINextSomewhat similar'].astype('string') #turning value into a string
df['AINextVery similar'] = df['AINextVery similar'].astype('string') #turning value into a string
df['AINextSomewhat different'] = df['AINextSomewhat different'].astype('string') #turning value into a string


# In[28]:


df['AINext'] = df['AINextVery different'] + df['AINextNeither different nor similar'] + df['AINextSomewhat similar'] + df['AINextVery similar'] + df['AINextSomewhat different'] 
#combining the 5 columns with answers into a new column 'AINext' 


# In[36]:


df.dropna(subset=['AINext']) #chcking to see if there are any non NULL values in 'AINext' column


# In[38]:


df['AISearchHaveWorkedWith'] = df['AISearchHaveWorkedWith'].astype('string') #turning value into a string
df['AISearchWantToWorkWith'] = df['AISearchWantToWorkWith'].astype('string') #turning value into a string


# In[44]:


df['AISearch'] = df['AISearchHaveWorkedWith'] + df['AISearchWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'AISearch' 


# In[42]:


df['AIToolCurrently Using'] = df['AIToolCurrently Using'].astype('string') #turning value into a string
df['AIToolInterested in Using'] = df['AIToolInterested in Using'].astype('string') #turning value into a string
df['AIToolNot interested in Using'] = df['AIToolNot interested in Using'].astype('string') #turning value into a string


# In[43]:


df['AITool'] = df['AIToolCurrently Using'] + df['AIToolInterested in Using'] + df['AIToolNot interested in Using'] 
#combining the 3 columns with answers into a new column 'AITool' 


# In[45]:


df['ConvertedCompYearly'] = df['ConvertedCompYearly'].astype('string') #turning value into a string


# In[46]:


df['Converted'] = df['ConvertedCompYearly']
#turning the column with answers into a new column 'Converted', just for the sake of keeping th process straight, even if its extra work. 


# In[47]:


df['DatabaseHaveWorkedWith'] = df['DatabaseHaveWorkedWith'].astype('string') #turning value into a string
df['DatabaseWantToWorkWith'] = df['DatabaseWantToWorkWith'].astype('string') #turning value into a string


# In[63]:


df['Database'] = df['DatabaseHaveWorkedWith'] + df['DatabaseWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'Database' 


# In[49]:


df['LanguageHaveWorkedWith'] = df['LanguageHaveWorkedWith'].astype('string') #turning value into a string
df['LanguageWantToWorkWith'] = df['LanguageWantToWorkWith'].astype('string') #turning value into a string


# In[62]:


df['Language'] = df['LanguageHaveWorkedWith'] + df['LanguageWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'Language'


# In[51]:


df['MiscTechHaveWorkedWith'] = df['MiscTechHaveWorkedWith'].astype('string') #turning value into a string
df['MiscTechWantToWorkWith'] = df['MiscTechWantToWorkWith'].astype('string') #turning value into a string


# In[52]:


df['MiscTech'] = df['MiscTechHaveWorkedWith'] + df['MiscTechWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'MiscTech'


# In[53]:


df['NEWCollabToolsHaveWorkedWith'] = df['NEWCollabToolsHaveWorkedWith'].astype('string') #turning value into a string
df['NEWCollabToolsWantToWorkWith'] = df['NEWCollabToolsWantToWorkWith'].astype('string') #turning value into a string


# In[54]:


df['NEWCollabTools'] = df['NEWCollabToolsHaveWorkedWith'] + df['NEWCollabToolsWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'NEWCollabTools'


# In[57]:


df['OfficeStackAsyncHaveWorkedWith'] = df['OfficeStackAsyncHaveWorkedWith'].astype('string') #turning value into a string
df['OfficeStackAsyncWantToWorkWith'] = df['OfficeStackAsyncWantToWorkWith'].astype('string') #turning value into a string


# In[56]:


df['OfficeStackAsync'] = df['OfficeStackAsyncHaveWorkedWith'] + df['OfficeStackAsyncWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'OfficeStackAsync'


# In[58]:


df['OfficeStackSyncHaveWorkedWith'] = df['OfficeStackSyncHaveWorkedWith'].astype('string') #turning value into a string
df['OfficeStackSyncWantToWorkWith'] = df['OfficeStackSyncWantToWorkWith'].astype('string') #turning value into a string


# In[59]:


df['OfficeStackSync'] = df['OfficeStackSyncHaveWorkedWith'] + df['OfficeStackSyncWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'OfficeStackSync'


# In[60]:


df['OpSysPersonal use'] = df['OpSysPersonal use'].astype('string') #turning value into a string
df['OpSysProfessional use'] = df['OpSysProfessional use'].astype('string') #turning value into a string


# In[61]:


df['OpSys'] = df['OpSysPersonal use'] + df['OpSysProfessional use'] 
#combining the 2 columns with answers into a new column 'OpSys'


# In[64]:


df['PlatformHaveWorkedWith'] = df['PlatformHaveWorkedWith'].astype('string') #turning value into a string
df['PlatformWantToWorkWith'] = df['PlatformWantToWorkWith'].astype('string') #turning value into a string


# In[65]:


df['Platform'] = df['PlatformHaveWorkedWith'] + df['PlatformWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'Platform'


# In[66]:


df['ResponseId'] = df['ResponseId'].astype('string') #turning value into a string


# In[67]:


df['ToolsTechHaveWorkedWith'] = df['ToolsTechHaveWorkedWith'].astype('string') #turning value into a string
df['ToolsTechWantToWorkWith'] = df['ToolsTechWantToWorkWith'].astype('string') #turning value into a string


# In[68]:


df['ToolsTech'] = df['ToolsTechHaveWorkedWith'] + df['ToolsTechWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'ToolsTech'


# In[69]:


df['WebframeHaveWorkedWith'] = df['WebframeHaveWorkedWith'].astype('string') #turning value into a string
df['WebframeWantToWorkWith'] = df['WebframeWantToWorkWith'].astype('string') #turning value into a string


# In[70]:


df['Webframe'] = df['WebframeHaveWorkedWith'] + df['WebframeWantToWorkWith'] 
#combining the 2 columns with answers into a new column 'Webframe'


# In[80]:


answers_from_survey = df.AIDev + df.AINext + df.AISearch + df.AITool + df.Converted + df.Database + df.Language + df.MiscTech + df.NEWCollabTools + df.OfficeStackAsync + df.OfficeStackSync + df.OpSys + df.Platform + df.ResponseId + df.ToolsTech + df.Webframe 
#show answers from survey from new rows


# In[84]:


answers_from_survey_set = set(answers_from_survey) #put answers from new columns in a set


# In[251]:


df.dropna(subset = answers_from_survey_set).shape[0] 
#show number of rows with no NULL values in a new set 'answers_from_survey_set'. Not sure what the issue is


# In[93]:


df.dropna(subset= ['AIDev', 'AINext', 'AISearch', 'AITool', 'Converted', 'Database', 'Language', 'MiscTech', 'NEWCollabTools', 'OfficeStackAsync', 'OfficeStackSync', 'OpSys',  'ResponseId', 'ToolsTech', 'Webframe']).shape[0]
#tried making the same action but without a substet, by inputing all columns names manually
# the result is only 1 row -> meaning only 1 person answered ALL questions


# <h1>TASK 2 Result -> How many people answred ALL questions -> 1 </h1>

# In[105]:


df.dropna(axis = 0) #there are 0 rows with no NULL values if we check all columns


# In[123]:


Workexp_mean = df.WorkExp.mean() #calculate mean


# In[252]:


Workexp_mode = float(df.WorkExp.mode()) #calculate Mode


# In[124]:


Workexp_median = df.WorkExp.median() # calculate Median


# In[253]:


print (f"The Mean for WorkExp is {Workexp_mean}, Mode is {Workexp_mode}, and Median is {Workexp_median}.")


# <h1>TASK 3 RESULTS -> The Mean for WorkExp is 11.4, Mode is 5 and Median is 9. </h1>

# In[133]:


Num_of_people_working_remotely = df[df.RemoteWork=='Remote'].shape[0] #check how many people have 'Remote' value in the RemoteWork column


# In[247]:


print (f"The number of respondents who work Remotely is {Num_of_people_working_remotely}")


# <h1>TASK 4 RESULTS -> The number of respondents who work Remotely is 30566</h1>

# In[196]:


mask = df.LanguageHaveWorkedWith.str.lower().str.contains('python', na = False)
df.loc[mask].shape[0]/len(df.ResponseId.unique())


# In[195]:


mask_worked_with_python = df.LanguageHaveWorkedWith.str.lower().str.contains('python', na = False) 
#create a mask checking how many people worked with python


# In[206]:


Percentage_worked_with_python = float((df.loc[mask_worked_with_python].shape[0]/df.ResponseId.nunique())*100) 
#calculated the % from total number of responders


# In[248]:


print (f"The percentage of respondents who work with Python is {Percentage_worked_with_python} % ")


# <h1>TASK 5 RESULTS -> The percentage of respondents who work with Python is 48.4 % </h1>

# In[144]:


mask_studied_online = df.LearnCode.str.lower().str.contains('online', na = False) #create a mask checking how many people studied online


# In[151]:


number_studied_online = int((df.loc[mask_studied_online].shape[0])) #calculate number of people who studied onilne as integer


# In[249]:


print (f"The number of respondents who studied online is {number_studied_online} ")


# <h1>TASK 6 RESULTS -> The number of respondents who studied online is 77027</h1>

# In[236]:


filtered_df = df[mask_worked_with_python] #new filtered values to use later, based on a mask we created earlier


# In[200]:


df['ConvertedCompYearly'] = pd.to_numeric(df['ConvertedCompYearly'], errors='coerce')
#code was not working because 'ConvertedCompYearly' was a string and I had to convert it to numeric


# In[237]:


filtered_df.groupby(by='Country').agg({'ConvertedCompYearly': ['mean', 'median']}) 
#the values we filtered earlier, now we group by 'Country'and calculate median and mean for each country


# <h1>TASK 7 RESULTS-> Mean and Median for Converted Yearly Compensation for people who worked with Python, by country </h1>

# In[238]:


selected_df = df[['ConvertedCompYearly', 'EdLevel']] #selecting 2 columns


# In[239]:


sorted_df = selected_df.sort_values(by='ConvertedCompYearly', ascending=False) #sorting the cilumns by 'ConvertedCompYearly'


# In[240]:


sorted_df.head(5) #showing top 5 results


# <h1>TASK 8 RESULTS -> Top 5 Educational Levels ordered by the Converted Yearly Compensation </h1>

# In[241]:


df['worked_with_python'] = mask_worked_with_python #creating new column based on a mask


# In[242]:


df.worked_with_python #checking new column


# In[243]:


temp_table = df.groupby('Age').agg({'ResponseId' : 'count', 'worked_with_python' : 'sum'}) 
#making a new table, groupped  by 'Age' and in it we count 'ResponseId' and sum up how many of them worked with Python


# In[244]:


temp_table.worked_with_python/ temp_table.ResponseId #dividing one value by another to get the percentage 


# <h1>EXTRA TASK 1 RESULTS -> Percentage of people who worked with python, grouped by age. </h1>

# In[245]:


df[(df.ConvertedCompYearly > df.ConvertedCompYearly.quantile(0.75)) & (df.RemoteWork == 'Remote')].Industry.value_counts()
#selecting people in .75 quantile of Converted Yearly Compensation and who worked Remotely. Then we count how many people like this are in each Industry


# <h1>EXTRA TASK 2 RESULTS -> Top Industries in .75 quantile of Converted Yearly Compensation and who work Remotely</h1>

# In[ ]:




