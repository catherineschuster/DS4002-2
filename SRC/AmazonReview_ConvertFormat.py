#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:08:38 2022

@author: catherineschuster
"""

import pandas as pd

['overall',
 'verified',
 'reviewTime',
 'reviewerID',
 'asin',
 'reviewerName',
 'reviewText',
 'summary',
 'unixReviewTime',
 'vote',
 'style',
 'image']

['category',
 'tech1',
 'description',
 'fit',
 'title',
 'also_buy',
 'tech2',
 'brand',
 'feature',
 'rank',
 'also_view',
 'details',
 'main_cat',
 'similar_item',
 'date',
 'price',
 'asin',
 'imageURL',
 'imageURLHighRes']

# READ ALL BEAUTY REVIEWS DATA
allbeauty = pd.read_json("/Users/catherineschuster/Desktop/DS 4002/All_Beauty.json", lines=True)


list(allbeauty.columns)


# READ LUXURY BEAUTY REVIEWS DATA
luxbeauty = pd.read_json("/Users/catherineschuster/Desktop/DS 4002/Luxury_Beauty.json", lines=True)
list(luxbeauty.columns)


# READ ALL BEAUTY PRODUCT DATA
allbeauty_product = pd.read_json("/Users/catherineschuster/Desktop/DS 4002/meta_All_Beauty.json", lines=True)
list(allbeauty_product.columns)
len(allbeauty_product)

allbeauty_product = allbeauty_product[["price", "asin", "title", "description", "brand"]]



# READ LUXURY BEAUTY PRODUCT DATA
luxbeauty_product = pd.read_json("/Users/catherineschuster/Desktop/DS 4002/meta_Luxury_Beauty.json", lines=True)
list(luxbeauty_product.columns)
luxbeauty_product = luxbeauty_product[["price", "asin", "title", "description", "brand"]]
is.na(luxbeauty_product)


allbeauty.to_csv("/Users/catherineschuster/Desktop/DS 4002/All_Beauty.csv")
luxbeauty.to_csv("/Users/catherineschuster/Desktop/DS 4002/Luxury_Beauty.csv")
allbeauty_product.to_csv("/Users/catherineschuster/Desktop/DS 4002/meta_All_Beauty.csv")
luxbeauty_product.to_csv("/Users/catherineschuster/Desktop/DS 4002/meta_Luxury_Beauty.csv")

