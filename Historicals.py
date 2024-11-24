#!/usr/bin/env python
# coding: utf-8

# In[49]:


import yfinance as yf

# Define the ticker symbol for the S&P/TSX Composite Index
ticker = '^GSPTSE'

# Fetch 5-year historical data with weekly intervals
data = yf.download(ticker, period='5y', interval='1wk')

# Display the data
print(data)


# In[46]:


import yfinance as yf

# Define the ticker symbol for the S&P/TSX Composite Index
ticker = 'L.TO'

# Fetch 5-year historical data with weekly intervals
data = yf.download(ticker, period='5y', interval='1wk')

# Display the data
print(data)


# In[33]:


import yfinance as yf

# Define the ticker symbol for Canadian Tire
ticker = 'CTC.TO'

# Fetch 5-year historical data
data = yf.download(ticker, period='5y', interval='1wk')

# Display the data
print(data)


# In[34]:


import yfinance as yf

# Define the ticker symbol for Metro Inc.
ticker = 'MRU.TO'

# Fetch 5-year historical data
data = yf.download(ticker, period='5y', interval='1wk')

# Display the data
print(data)


# In[35]:


import yfinance as yf

# Define the ticker symbol for Alimentation Couche-Tard Inc.
ticker = 'ATD.TO'

# Fetch 5-year historical data
data = yf.download(ticker, period='5y', interval='1wk')

# Display the data
print(data)


# In[36]:


import yfinance as yf

# Define the ticker symbol for The North West Company Inc.
ticker = 'NWC.TO'

# Fetch 5-year historical data
data = yf.download(ticker, period='5y', interval='1wk')

# Display the data
print(data)


# In[ ]:


import yfinance as yf

# Define the ticker symbol for The North West Company Inc.
ticker = 'NWC.TO'

# Fetch 5-year historical data
data = yf.download(ticker, period='5y', interval='1wk')

# Display the data
print(data)

