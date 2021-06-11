# Data Science Salary Estimator: Project Overview

- Created a tool taht estimates data science salaries (MAE ~ 13K) to help data scientists negotiate their income when they get a job.
- Scraped over 500 jobs descriptions from Glasdoor using Python and Selenium.
- Engineered features from the text of each job description to quantify the value companies put on Python, Excel, AWS and Spark.
- Optimized Linear, Lasso and Random Forest Regressors using GridsearchCV to reach the best model.
- Built a client facing API using Flask.

## Code and Resources Used

**Python Version:** 3.7
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle, requests
**For Web Framework Requirements:** `pip install -r requirements.txt`

**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium

## Web Scraping

Tweaked the web scraper Github repo (above) to scrape 500 jobs postings from Glassdoor.com. With each job, we got the following:

- Job Title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Company Size
- Company FOunded Date
- Industry
- Revenue

## Data Cleaning

After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

- Parsed numeric data out of salary
- Made columns for employer provided salary and hourly wages
- Removed rows without salary
- Parsed rating out of company text
- Made a new column for company state
- Added a column for if the job was at the company's headquarters
- Trasnformed founded date into age of company
- Made columns for if different skills were listed in the job description:

  - Python
  - R
  - Excel
  - AWS
  - Spark

- Column for simplified job title and Seniority
- Column for description length

## EDA

I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights fro the pivot tables.

## Model

First, I transformed the categorical variables into dummy variables. I also split the data into train and test sets with a test size of 20%.

I tried three different models and evalauted them using Mean Absolute Error. I chose MAE because it is relatively easy to interpet and outliers aren't particulary bad in for this type of model.

I tried three different models:

- **Multiple Regression** - Baseline for the model
- **Lasso Regression** - Because of the sparse data from the many categorical variables. I thought a normalized regression like Lasso would be effective.
- **Random Forest** - Again, with the sparcity associated with the data, I thought that this would be a good fit

## Model Performance

The Random Forest far outperformed the other approaches on the test and validation sets.

- **Random Forest:** MAE = 13.86
- **Lasso Regression** MAE = 20.26
- **Linear Regression** MAE = 25.36

## Productionization

In this step, I built a Flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns and estimates salary.
