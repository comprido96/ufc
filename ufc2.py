#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:51:36 2020

@author: fede
"""
import pandas as pd

fighters = pd.read_csv('/home/fede/Scrivania/fighters.csv')
fights = pd.read_csv('/home/fede/Scrivania/fights.csv')
fighters.Weight.fillna(0, inplace=True)
fighters['numericalWeight'] = fighters.Weight.apply(lambda x: int(str(x).split(' ')[0]))

upper_weight_limits = {115:'Straw', 125:'Fly', 135:'Bantam', 145:'Feather', 155:'Light', 
                       170:'Welter', 185:'Middle', 205:'Light Heavy'}

fighters.numericalWeight.describe()
fighters.numericalWeight.value_counts()[:15]
fighters[fighters.numericalWeight>500].fighter_name

def weight_category(weight):
    try:
        return upper_weight_limits[weight]+'weight'
    except KeyError:
        return 'HeavyWeight'
    
fighters['weight_category'] = fighters.numericalWeight.apply(lambda x: weight_category(x))
fighters.weight_category.value_counts()

lw = fighters[fighters.weight_category=='Lightweight']
