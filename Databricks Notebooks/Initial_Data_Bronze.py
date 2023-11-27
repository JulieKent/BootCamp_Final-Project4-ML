# Databricks notebook source
# MAGIC %sql
# MAGIC create or replace view cx.interactions as
# MAGIC SELECT cd.conversationStart,
# MAGIC     ca.conversationId,
# MAGIC     ca.mediaType,
# MAGIC     ca.wrapUpText,
# MAGIC     COUNT(DISTINCT ca.conversationId) as offered
# MAGIC FROM reporting.genesys__conversations_aggregates_wide AS ca
# MAGIC JOIN edw.genesys__conversations_details as cd ON ca.conversationId = cd.conversationId
# MAGIC JOIN
# MAGIC   (SELECT try_subtract(max(date(conversationStart)),interval '12' month) AS minDate, CURRENT_DATE as maxDate FROM edw.genesys__conversations_details) AS date_range
# MAGIC ON cd.conversationStart between date_range.minDate and date_range.maxDate
# MAGIC WHERE ca.originatingDirection = 'inbound'
# MAGIC AND ca.wrapUpText is not null
# MAGIC GROUP BY cd.conversationStart, ca.conversationId, ca.mediaType, ca.wrapUpText;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM cx.interactions;
