# Databricks notebook source
# MAGIC %sql
# MAGIC use schema juliekent

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Explore interactions table
# MAGIC SELECT * FROM interactions
# MAGIC WHERE date(conversationStart)>= '2022-12-01'
# MAGIC ORDER BY conversationStart;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Explore the difot_scores table
# MAGIC SELECT * FROM difot_scores;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Sum the count of unique conversations grouped date and media type and joined by the date to the difot score
# MAGIC Create or replace Table daily_interactions_byMediaType_withdifot as
# MAGIC SELECT
# MAGIC   DATE(i.conversationStart) AS intDate,
# MAGIC   i.mediaType,
# MAGIC   COUNT(DISTINCT i.conversationID) AS offerCount,
# MAGIC   d.Score 
# MAGIC FROM interactions as i
# MAGIC JOIN difot_scores AS d ON DATE(i.conversationStart) = d.Date
# MAGIC WHERE DATE(i.conversationStart) >= '2022-12-01' -- filter interactions by the earliest date in the difot_scores table
# MAGIC GROUP BY intDate, i.mediaType, d.Score
# MAGIC ORDER BY intDate ASC;
# MAGIC
# MAGIC SELECT * FROM daily_interactions_byMediaType_withdifot;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Sum the count of unique conversations grouped date and join by the date to the difot score
# MAGIC Create or replace Table daily_interactions_difot as
# MAGIC SELECT
# MAGIC   DATE(i.conversationStart) AS intDate,
# MAGIC   COUNT(DISTINCT i.conversationID) AS offerCount,
# MAGIC   d.Score 
# MAGIC FROM interactions as i
# MAGIC JOIN difot_scores AS d ON DATE(i.conversationStart) = d.Date
# MAGIC WHERE DATE(i.conversationStart) >= '2022-12-01' -- filter interactions by the earliest date in the difot_scores table
# MAGIC GROUP BY intDate, d.Score
# MAGIC ORDER BY intDate ASC;
# MAGIC
# MAGIC SELECT * FROM daily_interactions_difot;
