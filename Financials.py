#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import yfinance as yf


# In[20]:


import yfinance as yf

# Define stock ticker
stock = "L.TO"  # Loblaws Companies Limited on TSX

# Create Ticker object
company = yf.Ticker(stock)

# Retrieve financials
company.balance_sheet.to_csv(r"G:\OWN PROJECTS\PERSONAL PROJECTS\Loblaws\balance_sheet")


# In[23]:


company.quarterly_balance_sheet.to_csv(r"G:\OWN PROJECTS\PERSONAL PROJECTS\Loblaws\balance_sheet_quarterly")


# In[26]:


company.cashflow.to_csv(r"G:\OWN PROJECTS\PERSONAL PROJECTS\Loblaws\cashflow")
company.quarterly_cashflow.to_csv(r"G:\OWN PROJECTS\PERSONAL PROJECTS\Loblaws\cashflow_quarterly")


# In[28]:


company.quarterly_income_stmt.to_csv(r"G:\OWN PROJECTS\PERSONAL PROJECTS\Loblaws\income_statement_quaterly")


# In[ ]:




