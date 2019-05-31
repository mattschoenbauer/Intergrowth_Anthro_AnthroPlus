import sys
import os
import math
import pandas as pd
import scipy.stats as st
import datetime

def AP_get_hfa(length,sex,age_mons):
    length = float(length)
    hfa_df = pd.read_csv('hfawho2007.txt', delimiter='\t')
    hfa_df = hfa_df[hfa_df['sex'] == sex]

    if(age_mons>=61 and age_mons<229):

        lowage = math.floor(age_mons)
        uppage = math.floor(age_mons+1)
        diffage = (age_mons-lowage)

        hfa_df_low = hfa_df[hfa_df['age'] == lowage].reset_index()
        hfa_df_high = hfa_df[hfa_df['age'] == uppage].reset_index()

        if(diffage>0):
            l = hfa_df_low['l'][0]+diffage*(hfa_df_high['l'][0]-hfa_df_low['l'][0])
            m = hfa_df_low['m'][0]+diffage*(hfa_df_high['m'][0]-hfa_df_low['m'][0])
            s = hfa_df_low['s'][0]+diffage*(hfa_df_high['s'][0]-hfa_df_low['s'][0])
        else:
            l = hfa_df_low['l'][0]
            m = hfa_df_low['m'][0]
            s = hfa_df_low['s'][0]

        return (((length/m)**l)-1)/(s*l)
    return ''


def AP_get_wfa(weight,sex,age_mons,od):
    weight = float(weight)
    wfa_df = pd.read_csv('wfawho2007.txt', delimiter='\t')
    wfa_df = wfa_df[wfa_df['sex'] == sex]

    if(age_mons>=61 and age_mons<121 and (not od == 'y')):

        lowage = math.floor(age_mons)
        uppage = math.floor(age_mons+1)
        diffage = (age_mons-lowage)

        wfa_df_low = wfa_df[wfa_df['age'] == lowage].reset_index()
        wfa_df_high = wfa_df[wfa_df['age'] == uppage].reset_index()

        if(diffage>0):
            l = wfa_df_low['l'][0]+diffage*(wfa_df_high['l'][0]-wfa_df_low['l'][0])
            m = wfa_df_low['m'][0]+diffage*(wfa_df_high['m'][0]-wfa_df_low['m'][0])
            s = wfa_df_low['s'][0]+diffage*(wfa_df_high['s'][0]-wfa_df_low['s'][0])
        else:
            l = wfa_df_low['l'][0]
            m = wfa_df_low['m'][0]
            s = wfa_df_low['s'][0]

        zwei = (((weight/m)**l)-1)/(s*l)
        if(zwei>3):
            sd3pos = m*((1+l*s*3)**(1/l))
            sd23pos = sd3pos- m*((1+l*s*2)**(1/l))
            zwei = 3+((weight-sd3pos)/sd23pos)
        if(zwei < (-3)):
            sd3neg = m*((1+l*s*(-3))**(1/l))
            sd23neg = m*((1+l*s*(-2))**(1/l))-sd3neg
            zwei = (-3)+((weight-sd3neg)/sd23neg)
        return zwei
    return ''

def AP_get_zbfa(length,weight,sex,age_mons,od):

    cbmi = weight/((length/100)**2)

    bfa_df = pd.read_csv('bfawho2007.txt', delimiter='\t')
    bfa_df = bfa_df[bfa_df['sex'] == sex]

    if(age_mons>=61 and age_mons<229 and (not od == 'y')):

        lowage = math.floor(age_mons)
        uppage = math.floor(age_mons+1)
        diffage = (age_mons-lowage)

        bfa_df_low = bfa_df[bfa_df['age'] == lowage].reset_index()
        bfa_df_high = bfa_df[bfa_df['age'] == uppage].reset_index()

        if(diffage>0):
            l = bfa_df_low['l'][0]+diffage*(bfa_df_high['l'][0]-bfa_df_low['l'][0])
            m = bfa_df_low['m'][0]+diffage*(bfa_df_high['m'][0]-bfa_df_low['m'][0])
            s = bfa_df_low['s'][0]+diffage*(bfa_df_high['s'][0]-bfa_df_low['s'][0])
        else:
            l = bfa_df_low['l'][0]
            m = bfa_df_low['m'][0]
            s = bfa_df_low['s'][0]


        zbfa = (((cbmi/m)**l)-1)/(s*l)
        if(zbfa>3):
            sd3pos = m*((1+l*s*3)**(1/l))
            sd23pos = sd3pos- m*((1+l*s*2)**(1/l))
            zbfa = 3+((cbmi-sd3pos)/sd23pos)
        if(zbfa< (-3)):
            sd3neg = m*((1+l*s*(-3))**(1/l))
            sd23neg = m*((1+l*s*(-2))**(1/l))-sd3neg
            zbfa = (-3)+((cbmi-sd3neg)/sd23neg)
        return zbfa
    return ''

def error(elt,row):
    print('ERROR: ' + str(elt))
    print(row)
    return False

def check(z,index,row,correct):
    if abs(z - row[index]) > .005:
        print('ERROR')
        print(z)
        print(index)
        print(row)
        return False
    return correct


def run_AP_test(df):
    correct_count = 0
    totalcount = 0
    for index, row in df.iterrows():
        totalcount += 1
        correct = True

        sex = row['sex']
        age_mons = row['agemons']
        length = row['height']
        weight = row['weight']
        od = row['oedema']

        if not pd.isnull(length):
            zlen = AP_get_hfa(length,sex,age_mons)
            if (not str(zlen) == ''):
                correct = check(zlen,'zhfa',row,correct)
        if not pd.isnull(weight):
            zwei = AP_get_wfa(weight,sex,age_mons,od)
            if (not str(zwei) == ''):
                correct = check(zwei,'zwfa',row,correct)
        if(not od == 'y'):
            if (not pd.isnull(length)) and (not pd.isnull(weight)):
                zbmi = AP_get_zbfa(length,weight,sex,age_mons,od)
                if (not str(zbmi) == ''):
                    correct = check(zbmi,'zbfa',row,correct)
        if(correct):
            correct_count += 1

    print('Accuracy = ' + str(correct_count/totalcount))



df = pd.read_csv('survey_who2007_z.csv')

run_AP_test(df)





