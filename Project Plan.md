
## Project 4 Plan

### Contact Centre Productivity Improvement

#### *Purpose:*

Analysis 1 - Analyse call centre volumes by media type (call, email, chat) as they correlate to daily DIFOT % (% of orders delivered in full and on time) and see if machine learning can be used to predict future call volume by media type when DIFOT changes.  
Benefit - This will enable more efficient allocation of call centre agent resource to media types to improve adherence to required SLAs.

Analysis 2 - Also, factoring in the reason for the call and how that correlates to the media type used by the customer per enquiry type.
Benefit – understanding where self-service capability can be increased to further reduce interaction volume.

#### *How:*
Analysis 1 – 
1.	drawing data from the business and doing initial cleaning to remove any commercially confidential information and information not relevant to the analysis.
2.	Export to csv and ingest in DB community version
3.	Undertake further cleaning and readying for the machine learning model development
4.	Normalise for use in visualisation to be developed in Tableau

Analysis 2 – 
1.	Using data from analysis 1, undertake correlation analysis
2.	Create result visuals
