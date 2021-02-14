#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:37:31 2020

@author: fede
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
df = pd.read_csv('/home/fede/Scrivania/ufc/data.csv')
df.head()

df.columns
df_lw = df[df['weight_class']=='LightWeight']

features=df.columns

# esploriamo le variabili

df.R_fighter.describe()
df.R_fighter.isna().sum() #---> 0

df.B_fighter.describe()
df.B_fighter.isna().sum() #---> 0

df.Referee.describe()
df.Referee.isna().sum() #---> 23 missing

df.date.describe()
df.date.isna().sum() #---> 0

df.location.describe()
df.location.isna().sum() #---> 0

df.Winner.describe()
df.Winner.isna().sum() #---> 0

df.title_bout.describe()
df.title_bout.isna().sum() #---> 0

df.weight_class.describe() 
df.weight_class.isna().sum() #---> 0

df.no_of_rounds.describe() 
df.no_of_rounds.isna().sum() #---> 0

df.B_current_lose_streak.describe()
df.B_current_lose_streak.isna().sum() #---> 0

df.B_current_win_streak.describe()
df.B_current_win_streak.isna().sum() #---> 0

df.B_draw.describe() # colonna costante = 0
df.B_draw.isna().sum() #---> 0

df.B_avg_BODY_att.describe()
df.B_avg_BODY_att.isna().sum() #---> 1265, un po' tante, circa il 25%

df.B_avg_BODY_landed.describe()
df.B_avg_BODY_landed.isna().sum() #---> 1265

df.B_avg_CLINCH_att.describe()
df.B_avg_CLINCH_att.isna().sum() #---> 1265

df.B_avg_CLINCH_landed.describe()
df.B_avg_CLINCH_landed.isna().sum() #---> 1265

df.B_avg_DISTANCE_att.describe()
df.B_avg_DISTANCE_att.isna().sum() #---> 1265

df.B_avg_DISTANCE_landed.describe()
df.B_avg_DISTANCE_landed.isna().sum() #---> 1265

df.B_avg_GROUND_att.describe()
df.B_avg_GROUND_att.isna().sum() #---> 1265

df.B_avg_GROUND_landed.describe()
df.B_avg_GROUND_landed.isna().sum() #---> 1265

df.B_avg_HEAD_att.describe()
df.B_avg_HEAD_att.isna().sum() #---> 1265

df.B_avg_HEAD_landed.describe()
df.B_avg_HEAD_landed.isna().sum() #---> 1265

df.B_avg_KD.describe()
df.B_avg_KD.isna().sum() #---> 1265

df.B_avg_LEG_att.describe()
df.B_avg_LEG_att.isna().sum() #---> 1265

df.B_avg_LEG_landed.describe()
df.B_avg_LEG_landed.isna().sum() #---> 1265

df.B_avg_PASS.describe()
df.B_avg_PASS.isna().sum() #---> 1265

df.B_avg_REV.describe()
df.B_avg_REV.isna().sum() #---> 1265

df.B_avg_SIG_STR_att.describe()
df.B_avg_SIG_STR_att.isna().sum() #---> 1265

df.B_avg_SIG_STR_landed.describe()
df.B_avg_SIG_STR_landed.isna().sum() #---> 1265

df.B_avg_SIG_STR_pct.describe()
df.B_avg_SIG_STR_pct.isna().sum() #---> 1265

df.B_Stance.describe()
df.B_Stance.value_counts()
df.B_Stance.isna().sum() #---> 159


R_win_streak_greater_B_win_streak = df[df.R_current_win_streak>df.B_current_win_streak]
(R_win_streak_greater_B_win_streak.Winner=='Red').sum()

B_win_streak_greater_R_win_streak = df[df.B_current_win_streak>df.R_current_win_streak]
(B_win_streak_greater_R_win_streak.Winner=='Blue').sum()

# so always rooting for the fighter with longest current win streak is better than random guessing

'''


fighters = pd.read_csv('/home/fede/Scrivania/ufc/raw_fighter_details.csv')
fights = pd.read_csv('/home/fede/Scrivania/ufc/raw_total_fight_data.csv', sep=';')

df = pd.read_csv('/home/fede/Scrivania/ufc/raw_total_fight_data.csv', sep=';')

weight_classes = {'Strawweight': 'SW', 'Bantamweight': 'BW', 'Flyweight':'FLW', 
                  'Featherweight':'FTW', 'Lightweight':'LW', 'Welterweight':'WW',
                  'Middleweight':'MW', 'Light':'LHW', 'Heavyweight' :'HW',
                  'Open':'OW', 'Catch':'CW'}

def extract_weight(x):
    fields = x.split(' ')
    weight='OW'
    for field in fields:
        try:
            weight=weight_classes[field]
            return weight
        except KeyError:
            #foo
            pass
    return weight
            

### Data Manipulation

fights['R_sig_strikes_att'] = fights['R_SIG_STR.'].apply(lambda x: int(x.split(' ')[2]))
fights['R_sig_strikes_landed'] = fights['R_SIG_STR.'].apply(lambda x: int(x.split(' ')[0]))

fights['B_sig_strikes_att'] = fights['B_SIG_STR.'].apply(lambda x: int(x.split(' ')[2]))
fights['B_sig_strikes_landed'] = fights['B_SIG_STR.'].apply(lambda x: int(x.split(' ')[0]))

fights['R_tot_strikes_att'] = fights['R_TOTAL_STR.'].apply(lambda x: int(x.split(' ')[2]))
fights['R_tot_strikes_landed'] = fights['R_TOTAL_STR.'].apply(lambda x: int(x.split(' ')[0]))

fights['B_tot_strikes_att'] = fights['B_TOTAL_STR.'].apply(lambda x: int(x.split(' ')[2]))
fights['B_tot_strikes_landed'] = fights['B_TOTAL_STR.'].apply(lambda x: int(x.split(' ')[0]))

fights['R_tds_att']= fights['R_TD'].apply(lambda x: int(x.split(' ')[2]))
fights['R_tds_landed'] = fights['R_TD'].apply(lambda x: int(x.split(' ')[0]))

fights['B_tds_att']= fights['B_TD'].apply(lambda x: int(x.split(' ')[2]))
fights['B_tds_landed'] = fights['B_TD'].apply(lambda x: int(x.split(' ')[0]))

fights['R_head_strikes_att']= fights['R_HEAD'].apply(lambda x: int(x.split(' ')[2]))
fights['R_head_strikes_landed'] = fights['R_HEAD'].apply(lambda x: int(x.split(' ')[0]))

fights['B_head_strikes_att']= fights['B_HEAD'].apply(lambda x: int(x.split(' ')[2]))
fights['B_head_strikes_landed'] = fights['B_HEAD'].apply(lambda x: int(x.split(' ')[0]))

fights['R_body_strikes_att']= fights['R_BODY'].apply(lambda x: int(x.split(' ')[2]))
fights['R_body_strikes_landed'] = fights['R_BODY'].apply(lambda x: int(x.split(' ')[0]))

fights['B_body_strikes_att']= fights['B_BODY'].apply(lambda x: int(x.split(' ')[2]))
fights['B_body_strikes_landed'] = fights['B_BODY'].apply(lambda x: int(x.split(' ')[0]))

fights['R_leg_strikes_att']= fights['R_LEG'].apply(lambda x: int(x.split(' ')[2]))
fights['R_leg_strikes_landed'] = fights['R_LEG'].apply(lambda x: int(x.split(' ')[0]))

fights['B_leg_strikes_att']= fights['B_LEG'].apply(lambda x: int(x.split(' ')[2]))
fights['B_leg_strikes_landed'] = fights['B_LEG'].apply(lambda x: int(x.split(' ')[0]))

fights['R_distance_strikes_att']= fights['R_DISTANCE'].apply(lambda x: int(x.split(' ')[2]))
fights['R_distance_strikes_landed'] = fights['R_DISTANCE'].apply(lambda x: int(x.split(' ')[0]))

fights['B_distance_strikes_att']= fights['B_DISTANCE'].apply(lambda x: int(x.split(' ')[2]))
fights['B_distance_strikes_landed'] = fights['B_DISTANCE'].apply(lambda x: int(x.split(' ')[0]))

fights['R_clinch_strikes_att']= fights['R_CLINCH'].apply(lambda x: int(x.split(' ')[2]))
fights['R_clinch_strikes_landed'] = fights['R_CLINCH'].apply(lambda x: int(x.split(' ')[0]))

fights['B_clinch_strikes_att']= fights['B_CLINCH'].apply(lambda x: int(x.split(' ')[2]))
fights['B_clinch_strikes_landed'] = fights['B_CLINCH'].apply(lambda x: int(x.split(' ')[0]))

fights['R_ground_strikes_att']= fights['R_GROUND'].apply(lambda x: int(x.split(' ')[2]))
fights['R_ground_strikes_landed'] = fights['R_GROUND'].apply(lambda x: int(x.split(' ')[0]))

fights['B_ground_strikes_att']= fights['B_GROUND'].apply(lambda x: int(x.split(' ')[2]))
fights['B_ground_strikes_landed'] = fights['B_GROUND'].apply(lambda x: int(x.split(' ')[0]))

fights['3-5rounds'] = fights['Format'].apply(lambda x: 1 if x.split(' ')[0]=='3' else 0)

fights['title_bout'] = fights['Fight_type'].apply(
    lambda x: 1 if x.split(' ')[0]=='UFC' else 0)

fights['women'] = fights['Fight_type'].apply(lambda x: 1 if x.lower().split(' ')[0]=="women's" or x.lower().split(' ')[1]=="women's" else 0)

fights['weight_class'] = fights['Fight_type'].apply(lambda x: extract_weight(x))

fights['year'] = fights['date'].apply(lambda x:  x.split(' ')[2])

##############################################################################



### Data Exploration

# Per prima cosa voglio vedere come vengono vinti gli incontri:

fights['win_by'].value_counts()
# As we can see, some distinction is made between TKO and doctor's stoppage; we also have a Could Not Continue
# outcome. In essence, these are more or less the same thing so that we could merge them.
# Also split decision is very similar to majority decision
# Other stands for draw/time expired

outcome = {'Decision - Unanimous':'Decision', 'KO/TKO':'KO/TKO', 'Submission':'Submission', 
           'Decision - Split':'Decision', "TKO - Doctor's Stoppage":'KO/TKO', 'Decision - Majority':'Decision',
           'Overturned':'NC', 'DQ':'DQ', 'Could Not Continue': 'KO/TKO', 'Other':'Draw (Expired time)'}
fights['outcome'] = fights['win_by'].apply(lambda x: outcome[x]) 

fights['outcome'].hist(xrot=90, grid=True)
fights['outcome'].value_counts()

# It's interesting to notice that judges' decision is the most frequent outcome; however, more than 50% of 
# all fights finish don't ! 

# Now I want to see how this trend has evolved in the years: 
fights['year'].hist(xrot=90)

# as we can see, in the first UFC era (1993-2003), few fights per year were scheduled (the first years even
# had fights concentrated in a one-night tournament!)

fights_per_year_dict = fights['year'].value_counts().to_dict()
fights['fights_per_year'] = fights['year'].apply(lambda x: fights_per_year_dict[x])

fights['fights_per_year_per_outcome'] = fights[['Winner','year','outcome']].groupby(['year','outcome']).count().reset_index(drop=True)

fights_per_year_per_outcome = fights[['Winner','year','outcome']].groupby(['year','outcome']).count().rename({
    'Winner':'tot_fights'}, axis=1).reset_index()
fights_per_year_per_outcome['fights_per_year'] = fights_per_year_per_outcome.year.apply(lambda x: fights_per_year_dict[x])
fights_per_year_per_outcome['pct_fights'] = fights_per_year_per_outcome['tot_fights']/fights_per_year_per_outcome['fights_per_year']

sns.lineplot(x='year',y='tot_fights', hue='outcome', data=fights_per_year_per_outcome).set_xticklabels(range(1993,2020),rotation=90)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

sns.lineplot(x='year',y='pct_fights', hue='outcome', data=fights_per_year_per_outcome).set_xticklabels(range(1993,2020),rotation=90)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# we can see that reality is actually different: trends seem to converge  showing that actually 
# half of the bouts nowadays end by decision; the other percentages are practically 20% for subs, 30% for KOs

fights.weight_class.value_counts()

old_columns = ['R_SIG_STR.','B_SIG_STR.','R_TOTAL_STR.','B_TOTAL_STR.','R_TD','B_TD','R_HEAD','B_HEAD',
               'R_BODY','B_BODY','R_LEG','B_LEG','R_DISTANCE','B_DISTANCE','R_CLINCH','B_CLINCH',
               'R_GROUND','B_GROUND','Format','Fight_type','R_SIG_STR_pct','B_SIG_STR_pct','R_TD_pct',
               'B_TD_pct','win_by']
fights.drop(columns=old_columns, axis=1, inplace=True)
fights.rename({'R_KD':'R_kd','B_KD':'B_kd','R_SUB_ATT':'R_subs_att','B_SUB_ATT':'B_subs_att',
               'R_PASS':'R_passes','B_PASS':'B_passes','R_REV':'R_reversals','B_REV':'B_reversals'}, axis=1, inplace=True)

fights.Winner.fillna('Draw/NC', inplace=True)
##############################################################################



### LW Division 2010-2019
modern_years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
fights['modern_era'] = fights.year.apply(lambda x: x in modern_years)
lw = fights[(fights.weight_class=='LW') & (fights.modern_era)]
lw.outcome.hist()


def tot_wins(name):
    return (fights.Winner==name).sum()

def tot_fights(name):
    return ((fights.R_fighter == name) | (fights.B_fighter==name)).sum()

def tot_losses(name):
    return ( ((fights.R_fighter == name) | (fights.B_fighter==name)) & (fights.Winner!=name)).sum()

def kds_landed(name):
    return fights[fights.R_fighter==name].R_kd.sum() + fights[fights.B_fighter==name].B_kd.sum()

def kds_received(name):
    return fights[fights.R_fighter==name].B_kd.sum() + fights[fights.B_fighter==name].R_kd.sum()

def subs_att(name):
    return fights[fights.R_fighter==name].R_subs_att.sum() + fights[fights.B_fighter==name].B_subs_att.sum()

def subs_thrown_at(name):
    return fights[fights.R_fighter==name].B_subs_att.sum() + fights[fights.B_fighter==name].R_subs_att.sum()

def guard_passes(name):
    return fights[fights.R_fighter==name].R_passes.sum() + fights[fights.B_fighter==name].B_passes.sum()

def guard_passed(name):
    return fights[fights.R_fighter==name].B_passes.sum() + fights[fights.B_fighter==name].R_passes.sum()

def reversals(name):
    return fights[fights.R_fighter==name].R_reversals.sum() + fights[fights.B_fighter==name].B_reversals.sum()

def reversed_(name):
    return fights[fights.R_fighter==name].B_reversals.sum() + fights[fights.B_fighter==name].R_reversals.sum()

def sig_strikes_att(name):
    return fights[fights.R_fighter==name].R_sig_strikes_att.sum() + fights[fights.B_fighter==name].B_sig_strikes_att.sum()

def sig_strikes_landed(name):
    return fights[fights.R_fighter==name].R_sig_strikes_landed.sum() + fights[fights.B_fighter==name].B_sig_strikes_landed.sum()

def sig_strikes_thrown_at(name):
    return fights[fights.R_fighter==name].B_sig_strikes_att.sum() + fights[fights.B_fighter==name].R_sig_strikes_att.sum()

def sig_strikes_received(name):
    return fights[fights.R_fighter==name].B_sig_strikes_landed.sum() + fights[fights.B_fighter==name].R_sig_strikes_landed.sum()

def tot_strikes_att(name):
    return fights[fights.R_fighter==name].R_tot_strikes_att.sum() + fights[fights.B_fighter==name].B_tot_strikes_att.sum()

def tot_strikes_landed(name):
    return fights[fights.R_fighter==name].R_tot_strikes_landed.sum() + fights[fights.B_fighter==name].B_tot_strikes_landed.sum()

def tot_strikes_thrown_at(name):
    return fights[fights.R_fighter==name].B_tot_strikes_att.sum() + fights[fights.B_fighter==name].R_tot_strikes_att.sum()

def tot_strikes_received(name):
    return fights[fights.R_fighter==name].B_tot_strikes_landed.sum() + fights[fights.B_fighter==name].R_tot_strikes_landed.sum()

def tds_att(name):
    return fights[fights.R_fighter==name].R_tds_att.sum() + fights[fights.B_fighter==name].B_tds_att.sum()

def tds_landed(name):
    return fights[fights.R_fighter==name].R_tds_landed.sum() + fights[fights.B_fighter==name].B_tds_landed.sum()

def tds_thrown_at(name):
    return fights[fights.R_fighter==name].B_tds_att.sum() + fights[fights.B_fighter==name].R_tds_att.sum()

def tds_received(name):
    return fights[fights.R_fighter==name].B_tds_landed.sum() + fights[fights.B_fighter==name].R_tds_landed.sum()

def head_strikes_att(name):
    return fights[fights.R_fighter==name].R_head_strikes_att.sum() + fights[fights.B_fighter==name].B_head_strikes_att.sum()

def head_strikes_landed(name):
    return fights[fights.R_fighter==name].R_head_strikes_landed.sum() + fights[fights.B_fighter==name].B_head_strikes_landed.sum()

def head_strikes_thrown_at(name):
    return fights[fights.R_fighter==name].B_head_strikes_att.sum() + fights[fights.B_fighter==name].R_head_strikes_att.sum()

def head_strikes_received(name):
    return fights[fights.R_fighter==name].B_head_strikes_landed.sum() + fights[fights.B_fighter==name].R_head_strikes_landed.sum()

def body_strikes_att(name):
    return fights[fights.R_fighter==name].R_body_strikes_att.sum() + fights[fights.B_fighter==name].B_body_strikes_att.sum()

def body_strikes_landed(name):
    return fights[fights.R_fighter==name].R_body_strikes_landed.sum() + fights[fights.B_fighter==name].B_body_strikes_landed.sum()

def body_strikes_thrown_at(name):
    return fights[fights.R_fighter==name].B_body_strikes_att.sum() + fights[fights.B_fighter==name].R_body_strikes_att.sum()

def body_strikes_received(name):
    return fights[fights.R_fighter==name].B_body_strikes_landed.sum() + fights[fights.B_fighter==name].R_body_strikes_landed.sum()

def leg_strikes_att(name):
    return fights[fights.R_fighter==name].R_leg_strikes_att.sum() + fights[fights.B_fighter==name].B_leg_strikes_att.sum()

def leg_strikes_landed(name):
    return fights[fights.R_fighter==name].R_leg_strikes_landed.sum() + fights[fights.B_fighter==name].B_leg_strikes_landed.sum()

def leg_strikes_thrown_at(name):
    return fights[fights.R_fighter==name].B_leg_strikes_att.sum() + fights[fights.B_fighter==name].R_leg_strikes_att.sum()

def leg_strikes_received(name):
    return fights[fights.R_fighter==name].B_leg_strikes_landed.sum() + fights[fights.B_fighter==name].R_leg_strikes_landed.sum()

def distance_strikes_att(name):
    return fights[fights.R_fighter==name].R_distance_strikes_att.sum() + fights[fights.B_fighter==name].B_distance_strikes_att.sum()

def distance_strikes_landed(name):
    return fights[fights.R_fighter==name].R_distance_strikes_landed.sum() + fights[fights.B_fighter==name].B_distance_strikes_landed.sum()

def distance_strikes_thrown_at(name):
    return fights[fights.R_fighter==name].B_distance_strikes_att.sum() + fights[fights.B_fighter==name].R_distance_strikes_att.sum()

def distance_strikes_received(name):
    return fights[fights.R_fighter==name].B_distance_strikes_landed.sum() + fights[fights.B_fighter==name].R_distance_strikes_landed.sum()

def clinch_strikes_att(name):
    return fights[fights.R_fighter==name].R_clinch_strikes_att.sum() + fights[fights.B_fighter==name].B_clinch_strikes_att.sum()

def clinch_strikes_landed(name):
    return fights[fights.R_fighter==name].R_clinch_strikes_landed.sum() + fights[fights.B_fighter==name].B_clinch_strikes_landed.sum()

def clinch_strikes_thrown_at(name):
    return fights[fights.R_fighter==name].B_clinch_strikes_att.sum() + fights[fights.B_fighter==name].R_clinch_strikes_att.sum()

def clinch_strikes_received(name):
    return fights[fights.R_fighter==name].B_clinch_strikes_landed.sum() + fights[fights.B_fighter==name].R_clinch_strikes_landed.sum()

def ground_strikes_att(name):
    return fights[fights.R_fighter==name].R_ground_strikes_att.sum() + fights[fights.B_fighter==name].B_ground_strikes_att.sum()

def ground_strikes_landed(name):
    return fights[fights.R_fighter==name].R_ground_strikes_landed.sum() + fights[fights.B_fighter==name].B_ground_strikes_landed.sum()

def ground_strikes_thrown_at(name):
    return fights[fights.R_fighter==name].B_ground_strikes_att.sum() + fights[fights.B_fighter==name].R_ground_strikes_att.sum()

def ground_strikes_received(name):
    return fights[fights.R_fighter==name].B_ground_strikes_landed.sum() + fights[fights.B_fighter==name].R_ground_strikes_landed.sum()

def three_rounds(name):
    return fights[fights.R_fighter==name]['3-5rounds'].sum() + fights[fights.B_fighter==name]['3-5rounds'].sum()

def title_bouts(name):
    return fights[fights.R_fighter==name]['title_bout'].sum() + fights[fights.B_fighter==name]['title_bout'].sum()
    
def wins_by_KO(name):
    return fights[(fights.Winner==name) & (fights.outcome=='KO/TKO')].shape[0]

def wins_by_decision(name):
    return fights[(fights.Winner==name) & (fights.outcome=='Decision')].shape[0]

def wins_by_submission(name):
    return fights[(fights.Winner==name) & (fights.outcome=='Submission')].shape[0]

def losses_by_KO(name):
    return fights[((fights.R_fighter==name) | (fights.B_fighter==name)) & (fights.Winner!=name)
                  & (fights.outcome=='KO/TKO')].shape[0]

def losses_by_decision(name):
    return fights[((fights.R_fighter==name) | (fights.B_fighter==name)) & (fights.Winner!=name)
                  & (fights.outcome=='Decision')].shape[0]

def losses_by_submission(name):
    return fights[((fights.R_fighter==name) | (fights.B_fighter==name)) & (fights.Winner!=name)
                  & (fights.outcome=='Submission')].shape[0]

fighters['wins'] = fighters.fighter_name.apply(lambda name: tot_wins(name))
fighters['fights'] = fighters.fighter_name.apply(lambda name: tot_fights(name))
fighters['losses'] = fighters.fighter_name.apply(lambda name: tot_losses(name))

fighters['KDs_landed'] = fighters.fighter_name.apply(lambda name: kds_landed(name))
fighters['KDs_received'] = fighters.fighter_name.apply(lambda name: kds_received(name))

fighters['subs_att'] = fighters.fighter_name.apply(lambda name: subs_att(name))
fighters['subs_thrown_at'] = fighters.fighter_name.apply(lambda name: subs_thrown_at(name))

fighters['guard_passes'] = fighters.fighter_name.apply(lambda name: guard_passes(name))
fighters['guard_passed'] = fighters.fighter_name.apply(lambda name: guard_passed(name))

fighters['reversals'] = fighters.fighter_name.apply(lambda name: reversals(name))
fighters['reversed_'] = fighters.fighter_name.apply(lambda name: reversed_(name))

fighters['sig_strikes_att'] = fighters.fighter_name.apply(lambda name: sig_strikes_att(name))
fighters['sig_strikes_landed'] = fighters.fighter_name.apply(lambda name: sig_strikes_landed(name))
fighters['sig_strikes_thrown_at'] = fighters.fighter_name.apply(lambda name: sig_strikes_thrown_at(name))
fighters['sig_strikes_received'] = fighters.fighter_name.apply(lambda name: sig_strikes_received(name))

fighters['tot_strikes_att'] = fighters.fighter_name.apply(lambda name: tot_strikes_att(name))
fighters['tot_strikes_landed'] = fighters.fighter_name.apply(lambda name: tot_strikes_landed(name))
fighters['tot_strikes_thrown_at'] = fighters.fighter_name.apply(lambda name: tot_strikes_thrown_at(name))
fighters['tot_strikes_received'] = fighters.fighter_name.apply(lambda name: tot_strikes_received(name))

fighters['tds_att'] = fighters.fighter_name.apply(lambda name: tds_att(name))
fighters['tds_landed'] = fighters.fighter_name.apply(lambda name: tds_landed(name))
fighters['tds_thrown_at'] = fighters.fighter_name.apply(lambda name: tds_thrown_at(name))
fighters['tds_received'] = fighters.fighter_name.apply(lambda name: tds_received(name))

fighters['head_strikes_att'] = fighters.fighter_name.apply(lambda name: head_strikes_att(name))
fighters['head_strikes_landed'] = fighters.fighter_name.apply(lambda name: head_strikes_landed(name))
fighters['head_strikes_thrown_at'] = fighters.fighter_name.apply(lambda name: head_strikes_thrown_at(name))
fighters['head_strikes_received'] = fighters.fighter_name.apply(lambda name: head_strikes_received(name))

fighters['body_strikes_att'] = fighters.fighter_name.apply(lambda name: body_strikes_att(name))
fighters['body_strikes_landed'] = fighters.fighter_name.apply(lambda name: body_strikes_landed(name))
fighters['body_strikes_thrown_at'] = fighters.fighter_name.apply(lambda name: body_strikes_thrown_at(name))
fighters['body_strikes_received'] = fighters.fighter_name.apply(lambda name: body_strikes_received(name))

fighters['leg_strikes_att'] = fighters.fighter_name.apply(lambda name: leg_strikes_att(name))
fighters['leg_strikes_landed'] = fighters.fighter_name.apply(lambda name: leg_strikes_landed(name))
fighters['leg_strikes_thrown_at'] = fighters.fighter_name.apply(lambda name: leg_strikes_thrown_at(name))
fighters['leg_strikes_received'] = fighters.fighter_name.apply(lambda name: leg_strikes_received(name))

fighters['distance_strikes_att'] = fighters.fighter_name.apply(lambda name: distance_strikes_att(name))
fighters['distance_strikes_landed'] = fighters.fighter_name.apply(lambda name: distance_strikes_landed(name))
fighters['distance_strikes_thrown_at'] = fighters.fighter_name.apply(lambda name: distance_strikes_thrown_at(name))
fighters['distance_strikes_received'] = fighters.fighter_name.apply(lambda name: distance_strikes_received(name))

fighters['clinch_strikes_att'] = fighters.fighter_name.apply(lambda name: clinch_strikes_att(name))
fighters['clinch_strikes_landed'] = fighters.fighter_name.apply(lambda name: clinch_strikes_landed(name))
fighters['clinch_strikes_thrown_at'] = fighters.fighter_name.apply(lambda name: clinch_strikes_thrown_at(name))
fighters['clinch_strikes_received'] = fighters.fighter_name.apply(lambda name: clinch_strikes_received(name))

fighters['ground_strikes_att'] = fighters.fighter_name.apply(lambda name: ground_strikes_att(name))
fighters['ground_strikes_landed'] = fighters.fighter_name.apply(lambda name: ground_strikes_landed(name))
fighters['ground_strikes_thrown_at'] = fighters.fighter_name.apply(lambda name: ground_strikes_thrown_at(name))
fighters['ground_strikes_received'] = fighters.fighter_name.apply(lambda name: ground_strikes_received(name))

fighters['3rounds'] = fighters.fighter_name.apply(lambda name: three_rounds(name))

fighters['title_bouts'] = fighters.fighter_name.apply(lambda name: title_bouts(name))
 
fighters['wins_by_KO'] = fighters.fighter_name.apply(lambda name: wins_by_KO(name))
fighters['wins_by_decision'] = fighters.fighter_name.apply(lambda name: wins_by_decision(name))
fighters['wins_by_submission'] = fighters.fighter_name.apply(lambda name: wins_by_submission(name))

fighters['losses_by_KO'] = fighters.fighter_name.apply(lambda name: losses_by_KO(name))
fighters['losses_by_decision'] = fighters.fighter_name.apply(lambda name: losses_by_decision(name))
fighters['losses_by_submission'] = fighters.fighter_name.apply(lambda name: losses_by_submission(name))

fighters.to_csv(path_or_buf='/home/fede/Scrivania/fighters.csv', sep=',', header=True)
fights.to_csv(path_or_buf='/home/fede/Scrivania/fights.csv', sep=',', header=True)
