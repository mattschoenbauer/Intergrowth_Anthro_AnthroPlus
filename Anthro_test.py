import math
import pandas as pd
import numpy as np
import scipy.stats as st
import datetime

def adjust_length(length,lorh,age_days):
    length = float(length)
    if (age_days < 731) and (lorh == 'h'):
        length += .7
    if (age_days >= 731) and (lorh == 'l'):
        length += -.7
    return length

def Anthro_get_zlen(length,sex,age_days):
    length = float(length)
    l_df = pd.read_csv('lenanthro.txt',delimiter = '\t')
    l_df = l_df[l_df['sex'] == sex].reset_index()
    m = l_df['m'][age_days]
    s = l_df['s'][age_days]
    l = l_df['l'][age_days]
#     print('length = ' + str(length))
    zlen = (((length/m)**l)-1)/(s*l)
    return zlen

def Anthro_get_zwei(weight,sex,age_days):
    w_df = pd.read_csv('weianthro.txt',delimiter = '\t')
    w_df = w_df[w_df['sex'] == sex].reset_index()
    m = w_df['m'][age_days]
    s = w_df['s'][age_days]
    l = w_df['l'][age_days]
#         print((s,l,m))
    zwei = ((weight/m)**l-1)/(s*l)
    if zwei > 3:
        sd3pos = m*((1+l*s*3)**(1/l))
        sd23pos = sd3pos - m*((1+l*s*2)**(1/l))
        zwei = 3+((weight-sd3pos)/sd23pos)
    if zwei < -3:
        sd3neg = m*((1+l*s*(-3))**(1/l))
        sd23neg = m*((1+l*s*(-2))**(1/l))-sd3neg
        zwei = (-3)+((weight-sd3neg)/sd23neg)
    return zwei

def Anthro_get_zhc(hc,sex,age_days):
    hc = float(hc)
    hc_df = pd.read_csv('hcanthro.txt',delimiter = '\t')
    hc_df = hc_df[hc_df['sex'] == sex].reset_index()
    m = hc_df['m'][age_days]
    s = hc_df['s'][age_days]
    l = hc_df['l'][age_days]
    zhc = (((hc/m)**l)-1)/(s*l)
    return zhc

def Anthro_get_zwfl(weight,length,sex,age_days):
    if(age_days < 731):
        if(length>=45 and length<=110):

            wfl_df = pd.read_csv('wflanthro.txt',delimiter = '\t')
            wfl_df = wfl_df[wfl_df['sex'] == sex].reset_index()

            lowlen = math.floor(length*10)/10
            upplen = math.floor(length*10+1)/10
            difflen = (length-lowlen)/0.1

            wfl_df_low = wfl_df[wfl_df['length'] == lowlen].reset_index()
            wfl_df_high = wfl_df[wfl_df['length'] == upplen].reset_index()
            if(difflen>0):
                l = wfl_df_low['l'][0]+difflen*(wfl_df_high['l'][0]-wfl_df_low['l'][0])
                m = wfl_df_low['m'][0]+difflen*(wfl_df_high['m'][0]-wfl_df_low['m'][0])
                s = wfl_df_low['s'][0]+difflen*(wfl_df_high['s'][0]-wfl_df_low['s'][0])
            else:
                l = wfl_df_low['l'][0]
                m = wfl_df_low['m'][0]
                s = wfl_df_low['s'][0]

            zwfl = (((weight/m)**l)-1)/(s*l)
            if(zwfl>3):
                sd3pos = m*((1+l*s*3)**(1/l))
                sd23pos = sd3pos- m*((1+l*s*2)**(1/l))
                zwfl = 3+((weight-sd3pos)/sd23pos)
            if(zwfl<(-3)):
                sd3neg = m*((1+l*s*(-3))**(1/l))
                sd23neg = m*((1+l*s*(-2))**(1/l))-sd3neg
                zwfl = (-3)-((sd3neg-weight)/sd23neg)
            return zwfl

    else:
        if(length>=65 and length<=120):
            wfl_df = pd.read_csv('wfhanthro.txt',delimiter = '\t')
            wfl_df = wfl_df[wfl_df['sex'] == sex].reset_index()


            lowlen = math.floor(length*10)/10
            upplen = math.floor(length*10+1)/10
            difflen = (length-lowlen)/0.1

            wfl_df_low = wfl_df[wfl_df['height'] == lowlen].reset_index()
            wfl_df_high = wfl_df[wfl_df['height'] == upplen].reset_index()
            if(difflen>0):
                l = wfl_df_low['l'][0]+difflen*(wfl_df_high['l'][0]-wfl_df_low['l'][0])
                m = wfl_df_low['m'][0]+difflen*(wfl_df_high['m'][0]-wfl_df_low['m'][0])
                s = wfl_df_low['s'][0]+difflen*(wfl_df_high['s'][0]-wfl_df_low['s'][0])
            else:
                l = wfl_df_low['l'][0]
                m = wfl_df_low['m'][0]
                s = wfl_df_low['s'][0]

            zwfl = (((weight/m)**l)-1)/(s*l)
            if(zwfl>3):
                sd3pos = m*((1+l*s*3)**(1/l))
                sd23pos = sd3pos- m*((1+l*s*2)**(1/l))
                zwfl = 3+((weight-sd3pos)/sd23pos)
            if(zwfl<(-3)):
                sd3neg = m*((1+l*s*(-3))**(1/l))
                sd23neg = m*((1+l*s*(-2))**(1/l))-sd3neg
                zwfl = (-3)-((sd3neg-weight)/sd23neg)
            return zwfl
    return ''

def Anthro_get_zbmi(weight,length,sex,age_days):
    bmi_df = pd.read_csv('bmianthro.txt',delimiter = '\t')
    bmi_df = bmi_df[bmi_df['sex'] == sex].reset_index()
    cbmi = weight/((length/100)**2)

    if(age_days>=0 and age_days<=1856):

        m = bmi_df['m'][age_days]
        s = bmi_df['s'][age_days]
        l = bmi_df['l'][age_days]

        zbmi = (((cbmi/m)**l)-1)/(s*l)
        if(zbmi>3):
            sd3pos = m*((1+l*s*3)**(1/l))
            sd23pos = sd3pos- m*((1+l*s*2)**(1/l))
            zbmi = 3+((cbmi-sd3pos)/sd23pos)
        if(zbmi< (-3)):
            sd3neg = m*((1+l*s*(-3))**(1/l))
            sd23neg = m*((1+l*s*(-2))**(1/l))-sd3neg
            zbmi = (-3)+((cbmi-sd3neg)/sd23neg)
        return zbmi
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


def run_Anthro_test(df):
    correct_count = 0
    totalcount = 0
    for index, row in df.iterrows():
        totalcount += 1
        correct = True

        sex = row['GENDER']
        age_days = row['age.days']
        lorh = row['measure']
        length = row['HEIGHT']
        weight = row['WEIGHT']
        hc = row['HEAD']
        od = row['oedema']

        if not pd.isnull(length):
            length = adjust_length(length,lorh,age_days)
            zlen = Anthro_get_zlen(length,sex,age_days)
            correct = check(zlen,'zlen',row,correct)
        if not pd.isnull(weight):
            zwei = Anthro_get_zwei(weight,sex,age_days)
            correct = check(zwei,'zwei',row,correct)
        if not pd.isnull(hc):
            zhc = Anthro_get_zhc(hc,sex,age_days)
            correct = check(zhc,'zhc',row,correct)
        if(not od == 'y'):
            if (not pd.isnull(length)) and (not pd.isnull(weight)):
                zwfl = Anthro_get_zwfl(weight,length,sex,age_days)
                if (not str(zwfl) == ''):
                    correct = check(zwfl,'zwfl',row,correct)
                zbmi = Anthro_get_zbmi(weight,length,sex,age_days)
                if (not str(zbmi) == ''):
                    correct = check(zbmi,'zbmi',row,correct)
        if(correct):
            correct_count += 1

    print('Accuracy = ' + str(correct_count/totalcount))



df = pd.read_csv('MySurvey_z_st.csv')

run_Anthro_test(df)


