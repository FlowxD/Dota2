# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:41:08 2020

@author: Mandar Joshi
"""

import streamlit as st
import pandas as pd
import pickle
import numpy as np
st.title("Dota 2 Team win Prediction")

heros1 = ['antimage',
 'axe',
 'bane',
 'bloodseeker',
 'crystal_maiden',
 'drow_ranger',
 'earthshaker',
 'juggernaut',
 'mirana',
 'nevermore',
 'morphling',
 'phantom_lancer',
 'puck',
 'pudge',
 'razor',
 'sand_king',
 'storm_spirit',
 'sven',
 'tiny',
 'vengefulspirit',
 'windrunner',
 'zuus',
 'kunkka',
 'heroX',
 'lina',
 'lich',
 'lion',
 'shadow_shaman',
 'slardar',
 'tidehunter',
 'witch_doctor',
 'riki',
 'enigma',
 'tinker',
 'sniper',
 'necrolyte',
 'warlock',
 'beastmaster',
 'queenofpain',
 'venomancer',
 'faceless_void',
 'skeleton_king',
 'death_prophet',
 'phantom_assassin',
 'pugna',
 'templar_assassin',
 'viper',
 'luna',
 'dragon_knight',
 'dazzle',
 'rattletrap',
 'leshrac',
 'furion',
 'life_stealer',
 'dark_seer',
 'clinkz',
 'omniknight',
 'enchantress',
 'huskar',
 'night_stalker',
 'broodmother',
 'bounty_hunter',
 'weaver',
 'jakiro',
 'batrider',
 'chen',
 'spectre',
 'doom_bringer',
 'ancient_apparition',
 'ursa',
 'spirit_breaker',
 'gyrocopter',
 'alchemist',
 'invoker',
 'silencer',
 'obsidian_destroyer',
 'lycan',
 'brewmaster',
 'shadow_demon',
 'lone_druid',
 'chaos_knight',
 'meepo',
 'treant',
 'ogre_magi',
 'undying',
 'rubick',
 'disruptor',
 'nyx_assassin',
 'naga_siren',
 'keeper_of_the_light',
 'wisp',
 'visage',
 'slark',
 'medusa',
 'troll_warlord',
 'centaur',
 'magnataur',
 'shredder',
 'bristleback',
 'tusk',
 'skywrath_mage',
 'abaddon',
 'elder_titan',
 'legion_commander',
 'ember_spirit',
 'earth_spirit',
 'abyssal_underlord',
 'terrorblade',
 'phoenix',
 'techies',
 'oracle',
 'winter_wyvern',
 'arc_warden']


options1 = st.multiselect('Select your heros of Team 1:',
heros1)

st.write('You selected for team 1:', options1)


if len(options1) > 5:
    st.write("Select only 5 Heros for Team 2")


try:
    heros1.remove(options1[0])
    heros1.remove(options1[1])
    heros1.remove(options1[2])
    heros1.remove(options1[3])
    heros1.remove(options1[4])
except:
    pass

options2 = st.multiselect('Select your heros of Team 2:',
heros1)

st.write('You selected for team 2:', options2)


a = np.zeros(shape=(1,115))
df = pd.DataFrame(a,columns=['game_mode','game_type','antimage','axe','bane',
         'bloodseeker',
         'crystal_maiden',
         'drow_ranger',
         'earthshaker',
         'juggernaut',
         'mirana',
         'nevermore',
         'morphling',
         'phantom_lancer',
         'puck',
         'pudge',
         'razor',
         'sand_king',
         'storm_spirit',
         'sven',
         'tiny',
         'vengefulspirit',
         'windrunner',
         'zuus',
         'kunkka',
         'heroX',
         'lina',
         'lich',
         'lion',
         'shadow_shaman',
         'slardar',
         'tidehunter',
         'witch_doctor',
         'riki',
         'enigma',
         'tinker',
         'sniper',
         'necrolyte',
         'warlock',
         'beastmaster',
         'queenofpain',
         'venomancer',
         'faceless_void',
         'skeleton_king',
         'death_prophet',
         'phantom_assassin',
         'pugna',
         'templar_assassin',
         'viper',
         'luna',
         'dragon_knight',
         'dazzle',
         'rattletrap',
         'leshrac',
         'furion',
         'life_stealer',
         'dark_seer',
         'clinkz',
         'omniknight',
         'enchantress',
         'huskar',
         'night_stalker',
         'broodmother',
         'bounty_hunter',
         'weaver',
         'jakiro',
         'batrider',
         'chen',
         'spectre',
         'doom_bringer',
         'ancient_apparition',
         'ursa',
         'spirit_breaker',
         'gyrocopter',
         'alchemist',
         'invoker',
         'silencer',
         'obsidian_destroyer',
         'lycan',
         'brewmaster',
         'shadow_demon',
         'lone_druid',
         'chaos_knight',
         'meepo',
         'treant',
         'ogre_magi',
         'undying',
         'rubick',
         'disruptor',
         'nyx_assassin',
         'naga_siren',
         'keeper_of_the_light',
         'wisp',
         'visage',
         'slark',
         'medusa',
         'troll_warlord',
         'centaur',
         'magnataur',
         'shredder',
         'bristleback',
         'tusk',
         'skywrath_mage',
         'abaddon',
         'elder_titan',
         'legion_commander',
         'ember_spirit',
         'earth_spirit',
         'abyssal_underlord',
         'terrorblade',
         'phoenix',
         'techies',
         'oracle',
         'winter_wyvern',
         'arc_warden'])

if len(options2) > 5:
    st.write("Select only 5 Heros for Team 2")

try:

    for i in df.columns:
        if i==options1[0]:
            df[i]=1
        if i==options1[1]:
            df[i]=1
        if i==options1[2]:
            df[i]=1
        if i==options1[3]:
            df[i]=1
        if i==options1[4]:
            df[i]=1
            
    for i in df.columns:
        if i==options2[0]:
            df[i]=-1
        if i==options2[1]:
            df[i]=-1
        if i==options2[2]:
            df[i]=-1
        if i==options2[3]:
            df[i]=-1
        if i==options2[4]:
            df[i]=-1


except:
    pass

lis = list(df.columns) 


game_type = st.radio("What's Game type?",('2', '3'))

game_mode = st.radio("What's Game type?",('2', '9','8'))


df['game_mode'] = game_mode

df['game_type'] = game_type

for i in lis:
    df[i] = df[i].astype(np.int64)

st.write(df)

#test_csv = pd.read_csv(r"C:\Users\Mandar Joshi\Desktop\Proj\MLchallenge\test_sample.csv")
#test_csv = test_csv.drop(["Unnamed: 0"],axis=1)

data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])


if st.button('pred'):
    loaded_model = pickle.load(open(r"C:\Users\Mandar Joshi\Desktop\Proj\MLchallenge\pima.pickle3.dat", "rb"))
    y_pred = loaded_model.predict(df)[0]
    st.write(y_pred)

if st.button('Pred file'):
    try:
            
        loaded_model = pickle.load(open(r"C:\Users\Mandar Joshi\Desktop\Proj\MLchallenge\pima.pickle3.dat", "rb"))
        df2 = pd.read_csv(data)
        df2 = df2.drop(["Unnamed: 0"],axis=1)
        y_pred = loaded_model.predict(df2)
        st.write(y_pred)
    except:
        st.wirte("file contain errors")
    


    #if genre == 'Comedy':
    #   st.write('You selected comedy.')
    #    st.balloons()


