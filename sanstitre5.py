#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:32:01 2021

@author: lucas
"""

from finta import *
from finta.utils import resample
import yfinance as yf
import pandas as pd

class data_set:
    
    def __init__(self, stock):
        self.stock_df = pd.Dataframe(yf.Ticker(stock).history(period="max"))
        
    def add_indice(ind):
        
        
    
    
    
    