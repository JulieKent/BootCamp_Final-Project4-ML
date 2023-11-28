## Project 4

### Contact Centre Productivity and Performance Improvement

"Outline what we are planning to do"

#### *Data and data delivery*

We have drawn data from a live Australia Contact Centre which operates utilising the Genesys PureCloud Contact Centre Platform.

As this is a live commerical business, an initial notebook was created within the business' Databricks enviroment which conducts a daily ingest of contact centre data via APIs and normalises into tables housed within the bsuiness' Databricks profile.

The primary API used is: '/api/v2/analytics/conversations/details', which can be accessed via https://developer.genesys.cloud/devapps/api-explorer however, Genesys Cloud Licencing, developer permissions and login credentials are required to run any of the APIs available.

**Business Databricks Notebook for Initial Pull**

<img src="Images/Initial_Data.png" width="1200" height="600">


A second table of data was sourced again, from the same business although exported as a cross tab from the busness' Tableau envrionment which sources the related data from a SQL Management Server.  Again, this is data only accessible within the business and was filtered for the same date range as the Genesys data prior to export and subsequent ingest into the study Databricks environment for further transformation.


**Resulting Databricks Table**

![DIFOT](Images/DIFOT.png)


#### *Back end (ETL)*

1. Data Preparation for Machine Learning:
Two distinct datasets were created; "Daily Interactions with DIFOT Score" and "Daily Interactions with Media Type."
After importing the CSV files into Google Colab, we initiated the data cleaning process by introducing a new column named "flag" through a conditional statement.

IMAGE 

The logic behind this statement was to assign a value of 1 if the current interaction count exceeded that of the previous day while simultaneously having a lower DIFOT score; otherwise, a value of 0 was assigned. 
Subsequently, we delved into hyperparameter tuning using Kerastuner, a library designed for systematically exploring hyperparameter spaces to enhance deep learning model performance. 

IMAGE 

The top hyperparameter configurations were then applied to construct, train, and evaluate the machine learning models. 
This approach allowed us to optimise our models for both datasets, ultimately enhancing predictive accuracy and ensuring robust performance.

3.  Machine Learning Model Development:
Random Forest as the supervised learning algorithm for predicting call volumes.
Define the target variable (call volume by media type) and predictor variables (DIFOT %).
Train the Random Forest model using the training dataset. Validate the model. 

4. Model Evaluation:
Assess the model's performance using relevant metrics (e.g., accuracy, precision, recall).
Identify any areas for improvement and fine-tune the model if necessary.

5. Normalisation for Visualisation:
Normalise the model outputs for use in visualisations in Tableau.
Ensure the compatibility of the machine learning model results with the visualisation tool.

6. Analysis 2 - Correlation Analysis:
Use the data from Analysis 1 to perform correlation analysis.
Examine the relationship between call reasons and media types.
Identify patterns and trends that can inform self-service capability improvements.

#### *Visualisations*


[Draft Tableau Public](https://public.tableau.com/app/profile/julie.kent5187/viz/Project4_17010577303390/Sheet3?publish=yes)

Tableau

6. Result Visuals:
Create visualisations to represent the correlation findings.
Utilise Tableau to develop interactive dashboards for easy interpretation.
Highlight key insights and areas for improvement.






7. Conclusion:
Summarise the key findings from both analyses.
Discuss the implications for resource allocation, SLA adherence, and self-service improvements.
Recommend actionable steps based on the results.

8. Future Work:
Propose potential areas for further analysis and refinement of the model.
Consider ongoing monitoring and updating of the model as new data becomes available.

##########Some ideas to consider predicting future call volumes based on historical data for testing; ###############

### Time Series Forecasting:
Factor in seasonality, trends, and any other relevant patterns in the data.

### Call Arrival Rate Prediction:
Analyse patterns in historical data and incorporating external factors like time of day, day of the week, or special events.

### Average Handle Time Prediction:
Consider features such as the type of inquiry, customer information, and historical data on handling times.

### Agent Absence Rate Prediction:
Predict the absence rate of agents. Consider factors such as holidays, weekends, and historical absence patterns.

### Agent Utilisation Modelling:
Calculate agent utilisation rates based on historical data. This involves considering the number of agents available, call volumes, and average handle times to determine how efficiently agents are utilised.

### Staffing Requirement Calculation:
Combine the predicted call volumes, average handle times, and absence rates to calculate the required number of agents for each interval. 

### Machine Learning Regression Models:
Train regression models using features such as historical call volumes, average handle times, and absence rates to predict the number of agents needed.
