# DS4002-2: 
# Can Price Tell You Everything?: Sentiment Analysis on Amazon Reviews for Beauty Products
by Catherine Schuster, George Cao, Pulkit Rampa

## SRC

Code Execution:
Source code for this project can be broken down into two contexts. (1) The code to compile, clean, and consolidate the source data into the data used in sentiment analysis. This includes preliminary EDA before sentiment analysis was conducted. This code is compatable with R Studio. (2) The code to conduct and analyze the sentiment analysis process [2]. This code is compatible with python 3.0 or higher.

Code Usage:
If you find our models or code useful, please add suitable reference to our project and in your work.

## DATA

The source data for this project originates from Jianmo Ni’s Amazon Review Data Github [1]. The database is an updated 2018 version of the Amazon review dataset released in 2014, including metadata and review data for all amazon product categories. The specific four datasets used for this project includes the product metadata and reviews data for both luxury and normal beauty products. Data features include product ratings, review text, helpfulness votes, and product metadata (product descriptions, category information, price, and brand). 

For EDA and sentiment analysis, the product metadata and review datasets were cleaned and merged into two files (AllBeauty_Merged.csv and LuxBeauty_Merged.csv). Additionaly, two datasets (AllBeauty_SENTIMENTS.csv and LuxBeauty_SENTIMENTS.csv) contain this data and the features that resulted from VADER sentiment analysis [2]. Full access to all data is located on [Google Drive](https://drive.google.com/drive/folders/1c7KIYtGGA-7gxoceWI1QzwiTHkDHpakx?usp=sharing) in both .json and .csv formats. The data dictionary for the source data and sentiment analysis data is below:

Data Dictionary: Product Metadata (Both Luxury and Regular Product Data Sets)
| Column      | Description |
| ----------- | ----------- |
| Category      | product category       |
| Tech1   | the first technical detail table of the product        |
| description   | description of the product        |
| fit   | fit description or use instructions of the product        |
| title   | name of the product        |
| also_buy   | related products        |
| tech2   | the second technical detail table of the product        |
| brand   | brand name        |
| feature   | bullet-point format features of the product       |
| rank   | sales rank information        |
| also_view   | related products        |
| details   | additional product details        |
| main_cat   | Broad category of the product        |
| similar_item   | similar product table        |
| date   | date of crawl        |
| price   | price in US dollars (at time of crawl)        |
| asin   | ID of the product, e.g. 0000031852        |
| imageURL   | url of the product image        |
| imageURLHighRes   | url of the high resolution product image        |

Data Dictionary: Product Reviews (Both Luxury and Regular Product Data Sets)
| Column      | Description |
| ----------- | ----------- |
| overall      | rating of the product       |
| verified   | whether verified purchase (True/False)     |
| reviewTime   | time of the review (raw)        |
| reviewerID   | ID of the reviewer, e.g. A2SUAM1J3GNN3B        |
| asin   | ID of the product, e.g. 0000013714        |
| reviewerName   | name of the reviewer        |
| reviewText   | text of the review        |
| summary   | summary of the review        |
| unixReviewTime   | time of the review (unix time)        |
| vote   | helpful votes of the review       |
| style   | a disctionary of the product metadata, e.g., "Format" is "Hardcover"       |
| image   | images that users post after they have received the product        |

Data Dictionary: Product Review Sentiments (Both Luxury and Regular Product Data Sets)
| Column      | Description |
| ----------- | ----------- |
| asin      | ID of the product, e.g. 0000013714       |
| overall   | rating of the product     |
| verified   | whether verified purchase (True/False)        |
| reviewerID   | ID of the reviewer, e.g. A2SUAM1J3GNN3B        |
| reviewTime   | time of the review (raw)        |
| reviewerName   | name of the reviewer        |
| reviewText   | text of the review        |
| summary   | summary of the review        |
| unixReviewTime   | time of the review (unix time)        |
| vote   | helpful votes of the review       |
| price   | price in US dollars (at time of crawl)       |
| title   | name of the product         |
| description   | images that users post after they have received the product        |
| brand   | brand name         |
| compound   | score between -1 (most extreme negative) and +1 (most extreme positive)        |
| pos   | ratio for proportion of the review that is positive (pos + neu + neg = 1)       |
| neu   | ratio for proportion of the review that is neutral  (pos + neu + neg = 1)      |
| neg   | ratio for proportion of the review that is negative  (pos + neu + neg = 1)      |
| sentiment   | sentiment of review as a string  ("pos", "neu", or "neg)    |

## FIGURES


## REFERENCES

[1] J Ni, “Amazon Review Data (2018),” UCSD, 2018. [Online]. Available: http://deepyeti.ucsd.edu/jianmo/amazon/index.html. [Accessed Oct. 05, 2022].
[2] CJHUTTO, “Vader Sentiment Analysis: Valence aware dictionary and sentiment Reasoner,” GitHub. [Online]. Available: https://github.com/cjhutto/vaderSentiment. [Accessed: 12-Oct-2022].
