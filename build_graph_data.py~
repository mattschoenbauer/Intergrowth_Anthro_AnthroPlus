import sys
from IPython.display import display
import numpy as np
import os
import math
import pandas as pd
import scipy.stats as st
import datetime

dct = {}

def construct_IG_inverses(z):

    df = pd.read_csv("ig_data.csv")
    m_len_ls = []
    m_wei_ls = []
    m_hc_ls  = []
    f_len_ls = []
    f_wei_ls = []
    f_hc_ls  = []

    for index, row in df.iterrows():
        m_len_ls.append(IG_len_inverse(row['s_boys_lh'],row['m_boys_lh'],z))
        m_wei_ls.append(IG_len_inverse(row['s_boys_wt'],row['m_boys_wt'],z))
        m_hc_ls.append(IG_hc_inverse(row['s_boys_hc'],row['m_boys_hc'],z))
        f_len_ls.append(IG_len_inverse(row['s_girls_lh'],row['m_girls_lh'],z))
        f_wei_ls.append(IG_len_inverse(row['s_girls_wt'],row['m_girls_wt'],z))
        f_hc_ls.append(IG_hc_inverse(row['s_girls_hc'],row['m_girls_hc'],z))


    st = '_' + str(z)
    df = pd.DataFrame({'m_len' + st: m_len_ls, 'm_wei' + st:  m_wei_ls, 'm_hc' + st:  m_hc_ls, 'f_ls' + st: f_len_ls, 'f_wei' + st: f_wei_ls, 'f_hc' + st: f_hc_ls})

    return df


def IG_len_inverse(s,m,z):
    return math.exp(z * s + m)

def IG_hc_inverse(s,m,z):
    return z * s + m

def construct_Anthro_inverses(z):
    m_len_ls = []
    m_wei_ls = []
    m_bmi_ls = []
    m_wfh_ls = []
    m_wfl_ls = []
    m_hc_ls  = []
    f_len_ls = []
    f_wei_ls = []
    f_bmi_ls = []
    f_wfh_ls = []
    f_wfl_ls = []
    f_hc_ls  = []

    l_df = pd.read_csv('lenanthro.txt',delimiter = '\t')
    w_df = pd.read_csv('weianthro.txt',delimiter = '\t')
    hc_df = pd.read_csv('hcanthro.txt',delimiter = '\t')
    wfl_df = pd.read_csv('wflanthro.txt',delimiter = '\t')
    wfh_df = pd.read_csv('wfhanthro.txt',delimiter = '\t')
    bmi_df = pd.read_csv('bmianthro.txt',delimiter = '\t')

    print('HC')
    for age_days in range(0,1857):
        m_hc_ls.append(Anthro_hc_inverse(hc_df,1,age_days,z))
        f_hc_ls.append(Anthro_hc_inverse(hc_df,2,age_days,z))

    print('Weight')
    for age_days in range(0,1857):
        m_wei_ls.append(Anthro_wei_inverse(w_df,1,age_days,z))
        f_wei_ls.append(Anthro_wei_inverse(w_df,2,age_days,z))

    print('Length')
    for age_days in range(0,1857):
        m_len_ls.append(Anthro_len_inverse(l_df,1,age_days,z))
        f_len_ls.append(Anthro_len_inverse(l_df,2,age_days,z))

    print('BMI')
    for age_days in range(0,1857):
        m_bmi_ls.append(Anthro_bmi_inverse(bmi_df,1,age_days,z))
        f_bmi_ls.append(Anthro_bmi_inverse(bmi_df,2,age_days,z))

    print('WFL')
    for length in np.linspace(45, 110,(110-45)*10 + 1):
        m_wfl_ls.append(Anthro_wfl_inverse(wfl_df,1,length,z))
        f_wfl_ls.append(Anthro_wfl_inverse(wfl_df,2,length,z))

    print('WFH')
    for length in np.linspace(65, 120,(120-65)*10 + 1):
        m_wfh_ls.append(Anthro_wfh_inverse(wfh_df,1,length,z))
        f_wfh_ls.append(Anthro_wfh_inverse(wfh_df,2,length,z))

    st = 'z=' + str(z)
    len_df = pd.DataFrame({st: m_len_ls + f_len_ls})
    wei_df = pd.DataFrame({st: m_wei_ls + f_wei_ls})
    hc_df = pd.DataFrame({st: m_hc_ls + f_hc_ls})
    bmi_df = pd.DataFrame({st: m_bmi_ls + f_bmi_ls})
    wfl_df = pd.DataFrame({st: m_wfl_ls + f_wfl_ls})
    wfh_df = pd.DataFrame({st: m_wfh_ls + f_wfh_ls})
    return len_df, wei_df, hc_df, bmi_df, wfl_df, wfh_df

def Anthro_len_inverse(l_df,sex,age_days,z):
    l_df = l_df[l_df['sex'] == sex].reset_index()
    m = l_df['m'][age_days]
    s = l_df['s'][age_days]
    l = l_df['l'][age_days]
    return m * (z * s * l + 1)**(1./l)
#    for length in range(0,200,.1):
#        zp = Anthro_get_zlen(l_df,length,sex,age_days)
#        if (not zp == '') and abs(zp - z) < .1:
#            return length
#    print("ERROR: Length value not found")

def Anthro_get_zlen(l_df,length,sex,age_days):
    length = float(length)
    l_df = l_df[l_df['sex'] == sex].reset_index()
    m = l_df['m'][age_days]
    s = l_df['s'][age_days]
    l = l_df['l'][age_days]
    zlen = (((length/m)**l)-1)/(s*l)
    return zlen

def Anthro_wei_inverse(w_df,sex,age_days,z):
    w_df = w_df[w_df['sex'] == sex].reset_index()
    m = w_df['m'][age_days]
    s = w_df['s'][age_days]
    l = w_df['l'][age_days]
    return m * (z * s * l + 1)**(1./l)
#    for weight in range(0,120,.1):
#        zp = Anthro_get_zwei(w_df,weight,sex,age_days)
#        if (not zp == '') and abs(zp - z) < .1:
#            return weight
#    print("ERROR: Weight value not found")

def Anthro_get_zwei(w_df,sex,age_days):
    w_df = w_df[w_df['sex'] == sex].reset_index()
    m = w_df['m'][age_days]
    s = w_df['s'][age_days]
    l = w_df['l'][age_days]
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

def Anthro_hc_inverse(hc_df,sex,age_days,z):
    hc_df = hc_df[hc_df['sex'] == sex].reset_index()
    m = hc_df['m'][age_days]
    s = hc_df['s'][age_days]
    l = hc_df['l'][age_days]
    return m * (z * s * l + 1)**(1./l)
#    for hc in range(0,80,.1):
#        zp = Anthro_get_zhc(hc_df,hc,sex,age_days)
#        if (not zp == '') and abs(zp - z) < .1:
#            return hc
#    print("ERROR: Head Circumference value not found")

def Anthro_get_zhc(hcdf,hc,sex,age_days):
    hc = float(hc)
    hc_df = hc_df[hc_df['sex'] == sex].reset_index()
    m = hc_df['m'][age_days]
    s = hc_df['s'][age_days]
    l = hc_df['l'][age_days]
    zhc = (((hc/m)**l)-1)/(s*l)
    return zhc

def Anthro_wfl_inverse(wfl_df,sex,length,z):
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
    return m * (z * s * l + 1)**(1./l)
#   for weight in range(0,120,.1):
#        zp = Anthro_get_zwfl(df1,df2,weight,length,sex,age_days)
#        if (not zp == '') and abs(zp - z) < .1:
#            return weight
#    print("ERROR: Weight value not found")

def Anthro_wfh_inverse(wfh_df,sex,length,z):
    wfh_df = wfh_df[wfh_df['sex'] == sex].reset_index()

    lowlen = math.floor(length*10)/10
    upplen = math.floor(length*10+1)/10
    difflen = (length-lowlen)/0.1

    wfh_df_low = wfh_df[wfh_df['height'] == lowlen].reset_index()
    wfh_df_high = wfh_df[wfh_df['height'] == upplen].reset_index()
    if(difflen>0):
        l = wfh_df_low['l'][0]+difflen*(wfh_df_high['l'][0]-wfh_df_low['l'][0])
        m = wfh_df_low['m'][0]+difflen*(wfh_df_high['m'][0]-wfh_df_low['m'][0])
        s = wfh_df_low['s'][0]+difflen*(wfh_df_high['s'][0]-wfh_df_low['s'][0])
    else:
        l = wfh_df_low['l'][0]
        m = wfh_df_low['m'][0]
        s = wfh_df_low['s'][0]

    return m * (z * s * l + 1)**(1./l)

def Anthro_get_zwfl(df1,df2,weight,length,sex,age_days):
    if(age_days < 731):
        if(length>=45 and length<=110):
            wfl_df = df1
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
            wfl_df = df2
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


def Anthro_bmi_inverse(bmi_df,sex,age_days,z):
    bmi_df = bmi_df[bmi_df['sex'] == sex].reset_index()

    m = bmi_df['m'][age_days]
    s = bmi_df['s'][age_days]
    l = bmi_df['l'][age_days]

    return m * (z * s * l + 1)**(1./l)
#    for cbmi in range(0,50,.01):
#        zp = Anthro_get_zbmi(bmi_df,weight,length,sex,age_days)
#        if (not zp == '') and abs(zp - z) < .1:
#            return cbmi
#    print("ERROR: Weight value not found")


def Anthro_get_zbmi(bmi_df,cbmi,sex,age_days):
    bmi_df = bmi_df[bmi_df['sex'] == sex].reset_index()

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

# def construct_AP_inverses(z):
# only allow zwei for under 121 months

def construct_AP_inverses(z):
    m_len_ls = []
    m_wei_ls = []
    m_bmi_ls = []
    f_len_ls = []
    f_wei_ls = []
    f_bmi_ls = []

    l_df = pd.read_csv('hfawho2007.txt',delimiter = '\t')
    w_df = pd.read_csv('wfawho2007.txt',delimiter = '\t')
    bmi_df = pd.read_csv('bfawho2007.txt',delimiter = '\t')

    print('Weight')
    for age_mons in range(61,122):
        m_wei_ls.append(AP_zwei_inverse(w_df,1,age_mons,z))
        f_wei_ls.append(AP_zwei_inverse(w_df,2,age_mons,z))

    print('Length')
    for age_mons in range(61,230):
        m_len_ls.append(AP_zlen_inverse(l_df,1,age_mons,z))
        f_len_ls.append(AP_zlen_inverse(l_df,2,age_mons,z))

    print('BMI')
    for age_mons in range(61,230):
        m_bmi_ls.append(AP_zbmi_inverse(bmi_df,1,age_mons,z))
        f_bmi_ls.append(AP_zbmi_inverse(bmi_df,2,age_mons,z))

    st = 'z=' + str(z)
    len_df = pd.DataFrame({st: m_len_ls + f_len_ls})
    wei_df = pd.DataFrame({st: m_wei_ls + f_wei_ls})
    bmi_df = pd.DataFrame({st: m_bmi_ls + f_bmi_ls})
    return len_df, wei_df, bmi_df


def AP_zwei_inverse(wfa_df,sex,age_mons,z):
    wfa_df = wfa_df[wfa_df['sex'] == sex]
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

    return m * (z * s * l + 1)**(1./l)

def AP_get_zwei(weight,sex,age_mons,od):
    weight = float(weight)
    wfa_df = pd.read_csv('wfawho2007.txt', delimiter='\t')
    wfa_df = wfa_df[wfa_df['sex'] == sex]

    if(age_mons<121 and (not od == 'y')):

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
    if od == 'y':
        print("\nNo weight-for-age data for children with oedema")
    if age_mons >= 121:
        print("\nNo weight-for-age data for children over 121 months")
    return ''

def AP_zbmi_inverse(bfa_df,sex,age_mons,z):
    bfa_df = bfa_df[bfa_df['sex'] == sex]
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

    return m * (z * s * l + 1)**(1./l)

def AP_get_zbmi(length,weight,sex,age_mons,od):

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
        return zbfa, cbmi
    if od == 'y':
        print("\nNo bmi-for-age data for children with oedema")
    return '', ''

def AP_zlen_inverse(hfa_df,sex,age_mons,z):
    hfa_df = hfa_df[hfa_df['sex'] == sex]

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

    return m * (z * s * l + 1)**(1./l)

def AP_get_zlen(length,sex,age_mons):
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

def create_IG_Anthro_csvs():
    IG_df = pd.read_csv('ig_data.txt').reset_index()
    Anthro_l_df = pd.read_csv('lenanthro.txt',delimiter = '\t').reset_index()
    Anthro_w_df = pd.read_csv('weianthro.txt',delimiter = '\t').reset_index()
    Anthro_hc_df = pd.read_csv('hcanthro.txt',delimiter = '\t').reset_index()
    Anthro_wfl_df = pd.read_csv('wflanthro.txt',delimiter = '\t').reset_index()
    Anthro_wfh_df = pd.read_csv('wfhanthro.txt',delimiter = '\t').reset_index()
    Anthro_bmi_df = pd.read_csv('bmianthro.txt',delimiter = '\t').reset_index()

    for z in range(-3,4):
        print('Computing z=' + str(z))
        IG_add = construct_IG_inverses(z)
        Anthro_len_add, Anthro_wei_add, Anthro_hc_add, Anthro_bmi_add, Anthro_wfl_add, Anthro_wfh_add = construct_Anthro_inverses(z)
        IG_df = IG_df.merge(IG_add.reset_index())
        Anthro_l_df = Anthro_l_df.merge(Anthro_len_add.reset_index(),left_on = 'index', right_on = 'index')
        Anthro_w_df = Anthro_w_df.merge(Anthro_wei_add.reset_index(),left_on = 'index', right_on = 'index')
        Anthro_hc_df = Anthro_hc_df.merge(Anthro_hc_add.reset_index(),left_on = 'index', right_on = 'index')
        Anthro_wfl_df = Anthro_wfl_df.merge(Anthro_wfl_add.reset_index(),left_on = 'index', right_on = 'index')
        Anthro_wfh_df = Anthro_wfh_df.merge(Anthro_wfh_add.reset_index(),left_on = 'index', right_on = 'index')
        Anthro_bmi_df = Anthro_bmi_df.merge(Anthro_bmi_add.reset_index(),left_on = 'index', right_on = 'index')

    Anthro_l_df   = Anthro_l_df.drop(columns = 'index')
    Anthro_w_df   = Anthro_w_df.drop(columns = 'index')
    Anthro_hc_df  = Anthro_hc_df.drop(columns = 'index')
    Anthro_wfl_df = Anthro_wfl_df.drop(columns = 'index')
    Anthro_wfh_df = Anthro_wfh_df.drop(columns = 'index')
    Anthro_bmi_df = Anthro_bmi_df.drop(columns = 'index')

    IG_df.to_csv('ig_data.csv')
    Anthro_l_df.to_csv('lenanthro.csv')
    Anthro_w_df.to_csv('weianthro.csv')
    Anthro_hc_df.to_csv('hcanthro.csv')
    Anthro_wfl_df.to_csv('wflanthro.csv')
    Anthro_wfh_df.to_csv('wfhanthro.csv')
    Anthro_bmi_df.to_csv('bmianthro.csv')

#    display(IG_df)
#    display(Anthro_l_df)
#    display(Anthro_w_df)
#    display(Anthro_hc_df)
#    display(Anthro_wfl_df)
#    display(Anthro_wfh_df)


def create_AP_csvs():
    l_df = pd.read_csv('hfawho2007.txt',delimiter = '\t').reset_index()
    w_df = pd.read_csv('wfawho2007.txt',delimiter = '\t').reset_index()
    bmi_df = pd.read_csv('bfawho2007.txt',delimiter = '\t').reset_index()

    for z in range(-3,4):
        print('Computing z=' + str(z))
        len_add, wei_add, bmi_add = construct_AP_inverses(z)
        l_df = l_df.merge(len_add.reset_index(),left_on = 'index', right_on = 'index')
        w_df = w_df.merge(wei_add.reset_index(),left_on = 'index', right_on = 'index')
        bmi_df = bmi_df.merge(bmi_add.reset_index(),left_on = 'index', right_on = 'index')

    l_df   = l_df.drop(columns = 'index')
    w_df   = w_df.drop(columns = 'index')
    bmi_df = bmi_df.drop(columns = 'index')

    l_df.to_csv('hfawho2007.csv')
    w_df.to_csv('wfawho2007.csv')
    bmi_df.to_csv('bfawho2007.csv')


create_IG_Anthro_csvs()
create_AP_csvs()
