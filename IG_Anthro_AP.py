import sys
import numpy as np
import os
import math
import pandas as pd
import scipy.stats as st
import datetime
import matplotlib.pyplot as plt

TESTING = False
TESTPROG = 'AP'

def get_new_census():
    while(True):
        new = str(input("New census? (y/n): "))
        if new == '':
            return 'n'
        new = new[0].lower()
        if new == 'y' or new == 'n':
            return new
        else:
            print("Must enter 'y' or 'n'. Please try again.")


def get_weeks():
    while(True):
        weeks = str(input("Age in Weeks: "))
        if weeks == '' or weeks == 'u':
            return weeks
        if 27 <= int(weeks):
            weeks = int(weeks)
            return weeks
        else:
            print("Number of weeks should be 27 or more. Please try again.")
    return weeks


def get_days():
    while(True):
        days = str(input("Days: "))
        if days == '' or days == 'u':
            return days
        if 0 <= int(days) & int(days) <= 6:
            days = int(days)
            return days
        else:
            print("Number of days should be between 0 and 6. Please try again.")

def get_sex():
    while(True):
        sex = str(input("Child sex (m/f): "))
        sex = sex[0].lower()
        if sex == 'm' or sex == 'f' or sex == 'u':
            return sex
        else:
            print("Sex must be either 'm' or 'f'. Please try again.")

def get_lorh():
    while(True):
        lorh = str(input("Length (l) or height (h)? "))
        if lorh == '':
            return lorh
        lorh = lorh[0].lower()
        if lorh == 'l' or lorh == 'h' or lorh == 'u':
            return lorh
        else:
            print("Must enter 'l' or 'h'. Please try again.")

def get_oedema():
    while(True):
        od = str(input("Oedema (y/n): "))
        if od == '':
            return 'n'
        od = od[0].lower()
        if od == 'y' or od == 'n' or od == 'u':
            return od
        else:
            print("Must enter 'y' or 'n'. Please try again.")

def prompt_process(step,prompt):
    inp = str(input(prompt))
    step = process(step,inp)
    return step, inp

def process(step,inp):
    if inp == 'u':
        if not step == 1:
            step -= 1
        return step
    else:
        step += 1
        return step

def length_diagnosis(age_days,z):
    if age_days <= (365 * 5 + 1):
        if z < -3:
            st = 'Baixa estatura grave para a idade'
        if z >= -3 and z <-2:
            st = 'Baixa estatura moderada para a idade'
        if z >= -2 and z <-1:
            st = 'Baixa estatura leve para a idade'
        if z >= -1 and z <3:
            st = 'Estatura adequada para a idade'
        if z >= 3:
            st = 'Estatura elevada para a idade'
    if age_days > (365 * 5 + 1) and age_days <= 365 *10 + 2:
        if z < -3:
            st = 'Baixa estatura grave para a idade'
        if z >= -3 and z <-2:
            st = 'Baixa estatura moderada para a idade'
        if z >= -2 and z <-1:
            st = 'Baixa estatura leve para a idade'
        if z >= -1 and z <3:
            st = 'Estatura adequada para a idade'
        if z >= 3:
            st = 'Estatura elevada para a idade'
    if age_days > (365 * 10 + 2):
        if z < -3:
            st = 'Baixa estatura grave para a idade'
        if z >= -3 and z <-2:
            st = 'Baixa estatura moderada para a idade'
        if z >= -2 and z <-1:
            st = 'Baixa estatura leve para a idade'
        if z >= -1 and z <3:
            st = 'Estatura adequada'
        if z >= 3:
            st = 'Estatura elevada para a idade'
    return st

def bmi_diagnosis(age_days,z):
    if age_days <= (365 * 5 + 1):
        if z < -3:
            st = 'Subnutricao grave'
        if z >= -3 and z <-2:
            st = 'Subnutricao moderada'
        if z >= -2 and z <-1:
            st = 'Subnutricao leve'
        if z >= -1 and z < 1:
            st = 'Eutrofia'
        if z >= 1 and z < 2:
            st = 'Risco para sobrepeso'
        if z >= 2 and z < 3:
            st = 'Sobrepeso'
        if z >= 3:
            st = 'Obesidade'
    if age_days > (365 * 5 + 1) and age_days <= 365 *10 + 2:
        if z < -3:
            st = 'Subnutricao grave'
        if z >= -3 and z <-2:
            st = 'Subnutricao moderada'
        if z >= -2 and z <-1:
            st = 'Subnutricao leve'
        if z >= -1 and z < 1:
            st = 'Eutrofia'
        if z >= 1 and z < 2:
            st = 'Sobrepeso'
        if z >= 2 and z < 3:
            st = 'Obesidade'
        if z >= 3:
            st = 'Obesidade Grave'
    if age_days > (365 * 10 + 2):
        if z < -3:
            st = 'Subnutricao grave'
        if z >= -3 and z <-2:
            st = 'Subnutricao moderada'
        if z >= -2 and z <-1:
            st = 'Subnutricao leve'
        if z >= -1 and z < 1:
            st = 'Eutrofia'
        if z >= 1 and z < 2:
            st = 'Risco para sobrepeso'
        if z >= 2 and z < 3:
            st = 'Sobrepeso'
        if z >= 3:
            st = 'Obesidade'
    return st


def weight_diagnosis(age_days,z):
    st = ''
    if age_days <= (365 * 5 + 1):
        if z < -3:
            st = 'Subnutricao grave para a idade'
        if z >= -3 and z <-2:
            st = 'Subnutricao moderada para a idade'
        if z >= -2 and z <-1:
            st = 'Subnutricao leve para a idade'
        if z >= -1 and z < 1:
            st = 'Peso adequado para a idade'
        if z >= 1 and z < 2:
            st = 'Peso adequado para a idade'
        if z >= 2 and z < 3:
            st = 'Peso elevado para a idade'
        if z >= 3:
            st = 'Peso elevado para a idade'
    if age_days > (365 * 5 + 1) and age_days <= 365 *10 + 2:
        if z < -3:
            st = 'Subnutricao grave para a idade'
        if z >= -3 and z <-2:
            st = 'Subnutricao moderada para a idade'
        if z >= -2 and z <-1:
            st = 'Subnutricao leve para a idade'
        if z >= -1 and z < 1:
            st = 'Peso adequado para a idade'
        if z >= 1 and z < 2:
            st = 'Peso adequado para a idade'
        if z >= 2 and z < 3:
            st = 'Peso elevado para a idade'
        if z >= 3:
            st = 'Peso elevado para a idade'
    return st

def wfl_diagnosis(age_days,z):
    st = ''
    if age_days <= (365 * 5 + 1):
        if z < -3:
            st = 'Subnutricao grave'
        if z >= -3 and z <-2:
            st = 'Subnutricao moderada'
        if z >= -2 and z <-1:
            st = 'Subnutricao leve'
        if z >= -1 and z < 1:
            st = 'Eutrofia'
        if z >= 1 and z < 2:
            st = 'Risco para sobrepeso'
        if z >= 2 and z < 3:
            st = 'Sobrepeso'
        if z >= 3:
            st = 'Obesidade'
    return st

def display(writestr,z,string):
    p = 100*st.norm.cdf(z)
    z = "%0.4f" % z
    p = "%0.2f" % p
    print('')
    print(string + ":")
    print("z-score: " + str(z))
    print("centile: " + str(p))
    writestr +=  ", " + str(z)
    return writestr

def display2(writestr,z,string):
    p = 100*st.norm.cdf(z)
    z = "%0.2f" % z
    p = "%0.2f" % p
    print('')
    print(string + ":")
    print("z-score: " + str(z))
    print("centile: " + str(p))
    writestr += ", " + str(z)
    return writestr

def run_Intergrowth(weeks,days,writestr,sex,length,weight,hc):

    df = pd.read_csv("ig_data.txt")

    if sex == 2:
        mw = "m_girls_wt"
        sw = "s_girls_wt"
        ml = "m_girls_lh"
        sl = "s_girls_lh"
        mh = "m_girls_hc"
        sh = "s_girls_hc"

    if sex == 1:
        mw = "m_boys_wt"
        sw = "s_boys_wt"
        ml = "m_boys_lh"
        sl = "s_boys_lh"
        mh = "m_boys_hc"
        sh = "s_boys_hc"

    index = days-189

    if not length == '':
        length = float(length)
        l_var = math.log(length)
        zlen = (l_var - df[ml][index])/df[sl][index]
        writestr = display(writestr,zlen,"Length")
        dstr = length_diagnosis(days,zlen)
        writestr += ", " + dstr
        print('Diagnosis: ' + dstr)
    else:
        writestr += ', , '

    if not weight == '':
        weight = float(weight)
        w_var = math.log(weight)
        zwei = (w_var - df[mw][index])/df[sw][index]
        writestr = display(writestr,zwei,"Weight")
        dstr = weight_diagnosis(days,zwei)
        writestr += ", " + dstr
        print('Diagnosis: ' + dstr)
    else:
        writestr += ', , '

    writestr += ', , , , '

    if not hc == '':
        hc = float(hc)
        zhc = (hc - df[mh][index])/df[sh][index]
        writestr = display(writestr,zhc,"Head Circumference")
    else:
        writestr += ', '

    print('')
    IG_display(days,length,weight,hc,sex)
    return writestr

def adjust_length(l,lorh,age_days):
    length = float(l)
    if (age_days < 731) and (lorh == 'h'):
        length += .7
    if (age_days >= 731) and (lorh == 'l'):
        length += -.7
    return length

def unadjust_length(l,lorh,age_days):
    length = float(l)
    if (age_days < 731) and (lorh == 'h'):
        length += -.7
    if (age_days >= 731) and (lorh == 'l'):
        length += .7
    return length

def determine_n(todaystr):
    n = 0
    if not os.path.isfile(todaystr + '.csv'):
        return n
    n = 1
    while(os.path.isfile(todaystr + "(" + str(n+1) + ").csv")):
        n += 1
    return n

def Anthro_get_zlen(length,sex,age_days):
    length = float(length)
    l_df = pd.read_csv('lenanthro.csv')
    l_df = l_df[l_df['sex'] == sex].reset_index()
    m = l_df['m'][age_days]
    s = l_df['s'][age_days]
    l = l_df['l'][age_days]
    zlen = (((length/m)**l)-1)/(s*l)
    return zlen

def Anthro_get_zwei(weight,sex,age_days):
    w_df = pd.read_csv('weianthro.csv')
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

def Anthro_get_zhc(hc,sex,age_days):
    hc = float(hc)
    hc_df = pd.read_csv('hcanthro.csv')
    hc_df = hc_df[hc_df['sex'] == sex].reset_index()
    m = hc_df['m'][age_days]
    s = hc_df['s'][age_days]
    l = hc_df['l'][age_days]
    zhc = (((hc/m)**l)-1)/(s*l)
    return zhc

def Anthro_get_zwfl(weight,length,sex,age_days):
    if(age_days < 731):
        if(length>=45 and length<=110):
            wfl_df = pd.read_csv('wflanthro.csv')
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
            wfl_df = pd.read_csv('wfhanthro.csv')
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
    bmi_df = pd.read_csv('bmianthro.csv')
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
        return zbmi, cbmi
    return ''

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

def run_Anthro(age_days,writestr,sex,lorh,length,weight,hc,od):
    if age_days < 0:
        print("ERROR: Date of visit must be after date of birth\n")
        return ''

    if not(weight == '' or length == ''):
        weight = float(weight)
        length = float(length)
        zbmi, cbmi = Anthro_get_zbmi(weight,length,sex,age_days)
        cbmi = "%0.2f" % cbmi
    else:
        cbmi = ''

    if not length == '':
        length = adjust_length(length,lorh,age_days)
        writestr += ", " + str(length) + ", " + cbmi
        zlen = Anthro_get_zlen(length,sex,age_days)
        writestr = display2(writestr,zlen,"Length/Height")
        dstr = length_diagnosis(age_days,zlen)
        writestr += ", " + dstr
        print('Diagnosis: ' + dstr)
    else:
        writestr += ', , ' + cbmi + ', , '

    if not weight == '':
        weight = float(weight)
        zwei = Anthro_get_zwei(weight,sex,age_days)
        writestr = display2(writestr,zwei,"Weight")
        dstr = weight_diagnosis(age_days,zwei)
        writestr += ", " + dstr
        if not dstr == '':
            print('Diagnosis: ' + dstr)
    else:
        writestr += ', , '

    if not(weight == '' or length == ''):
        if(not od == 'y'):
            if age_days < 731:
                if length <= 110 and length >= 45:
                    zwfl = Anthro_get_zwfl(weight,length,sex,age_days)
                    if not str(zwfl) == '':
                        writestr = display2(writestr,zwfl,"Weight-for-length")
                        dstr = wfl_diagnosis(age_days,zwfl)
                        writestr += ", " + dstr
                        if not dstr == '':
                            print('Diagnosis: ' + dstr)
                    else:
                        writestr += ', , '
                if length > 110:
                    st = 'No weight-for-length data for children less than 731 days old with adjusted length/height over 110'
                    print('')
                    print(st)
                    writestr += ', , '
                if length < 45:
                    st = 'No weight-for-length data for children less than 731 days old with adjusted length/height under 45'
                    print('')
                    print(st)
                    writestr += ', , '
            else:
                if length <= 120 and length >= 65:
                    zwfl = Anthro_get_zwfl(weight,length,sex,age_days)
                    if not str(zwfl) == '':
                        writestr = display2(writestr,zwfl,"Weight-for-length")
                        dstr = wfl_diagnosis(age_days,zwfl)
                        writestr += ", " + dstr
                        if not dstr == '':
                            print('Diagnosis: ' + dstr)
                    else:
                        writestr += ', , '
                if length > 120:
                    st = 'No weight-for-length data for children over 731 days old with adjusted length/height over 120'
                    print('')
                    print(st)
                    writestr += ', , '
                if length < 65:
                    st = 'No weight-for-length data for children over 731 days old with adjusted length/height under 65'
                    print('')
                    print(st)
                    writestr += ', , '
            zbmi, cbmi = Anthro_get_zbmi(weight,length,sex,age_days)
            if not str(zbmi) == '':
                writestr = display2(writestr,zbmi,"BMI")
                dstr = bmi_diagnosis(age_days,zbmi)
                writestr += ", " + dstr
                if not dstr == '':
                    print('Diagnosis: ' + dstr)
        else:
            print('\nNo weight-for-length data for children with oedema')
    else:
        writestr += ', , , , '

    if not hc == '':
        zhc = Anthro_get_zhc(hc,sex,age_days)
        writestr = display2(writestr,zhc,"Head Circumference")
    else:
        writestr += ', '

    Anthro_display(age_days,length,weight,hc,sex,cbmi)

    print('')
    return writestr

def run_AP(age_days,age_mons,writestr,sex,length,weight,od):
    if age_mons < 0:
        print("ERROR: Date of visit must be after date of birth\n")
        return ''

    if not(weight == '' or length == ''):
        weight = float(weight)
        length = float(length)
        zbmi, cbmi = AP_get_zbmi(length,weight,sex,age_mons,od)
        cbmi = "%0.2f" % cbmi
    else:
        cbmi = ''

    if not length == '':
        writestr += ", " + str(length) + ", " + str(cbmi)
        zlen = AP_get_zlen(length,sex,age_mons)
        if zlen == '':
            writestr += ', '
        else:
            writestr = display2(writestr,zlen,"Height")
            dstr = length_diagnosis(age_days,zlen)
            writestr += ", " + dstr
            if not dstr == '':
                print('Diagnosis: ' + dstr)
    else:
        writestr += ', , ' + cbmi + ', , '

    if not weight == '':
        weight = float(weight)
        zwei = AP_get_zwei(weight,sex,age_mons,od)
        if zwei == '':
            writestr += ', , '
        else:
            writestr = display2(writestr,zwei,"Weight")
            dstr = weight_diagnosis(age_days,zwei)
            writestr += ", " + dstr
            if not dstr == '':
                print('Diagnosis: ' + dstr)
        writestr += ', , '
        if zbmi == '':
            writestr += ', , '
        else:
            writestr = display2(writestr,zbmi,"BMI")
            dstr = bmi_diagnosis(age_days,zbmi)
            writestr += ", " + dstr
            if not dstr == '':
                print('Diagnosis: ' + dstr)
    else:
        writestr += ', , '

    writestr += ', '

    AP_display(age_mons,length,weight,sex,cbmi)

    print('')
    return writestr

def IG_display(days,length,weight,hc,sex):
    df = pd.read_csv('ig_graph_data.csv')
    if sex == 1:
        sst = 'm_'
    if sex == 2:
        sst = 'f_'
    iterator = []
    if not length == '':
        iterator.append((sst + 'len_',length,'Length (cm)','Length for Age'))
    if not weight == '':
        iterator.append((sst + 'wei_',weight,'Weight (kg)','Weight for Age'))
    if not hc == '':
        iterator.append((sst + 'hc_',hc,'Head Circumference (cm)','Head Circumference for Age'))
    for dat in iterator:
        dct = {}
        for z in range(-3,4):
            dct[z] = df[dat[0] + str(z)].tolist()
        inp = range(189,189+266)
        plt.plot(inp,dct[3],'k',label = '3DP')
        plt.plot(inp,dct[2],'r',label = '2DP')
        plt.plot(inp,dct[1],'y',label = '1DP')
        plt.plot(inp,dct[0],'g',label = 'Mediana')
        plt.plot(inp,dct[-1],'y',label = '-1DP')
        plt.plot(inp,dct[-2],'r',label = '-2DP')
        plt.plot(inp,dct[-3],'k',label = '-3DP')
        plt.plot([days],[dat[1]], 'ko')
        plt.legend()
        plt.title(dat[2] + ' DP')
        plt.xlabel('Age (days)')
        plt.ylabel(dat[2])
        plt.show()



def Anthro_display(age_days,length,weight,hc,sex,cbmi):
    iterator = []
    if not length == '':
        df = pd.read_csv('lenanthro.csv')
        if age_days < 731:
            iterator.append((df[df['age'] < 731],age_days,length,'Age (days)','Length/Height (cm)',range(0,731),'Length for Age'))
        else:
            iterator.append((df[df['age'] >= 731],age_days,length,'Age (days)','Length/Height (cm)',range(731,1857),'Length for Age'))
    if not weight == '':
        iterator.append((pd.read_csv('weianthro.csv'),age_days,weight,'Age (days)','Weight',range(0,1857),'Weight for Age'))
    if (not weight == '') and (not length == ''):
        bmi_df = pd.read_csv('bmianthro.csv')
        if age_days < 731:
            if length >= 45 and length <= 110:
                iterator.append((pd.read_csv('wflanthro.csv'),length,weight,'Length (cm)','Weight (kg)',np.linspace(45, 110,(110-45)*10 + 1),'Weight for length'))
            iterator.append((bmi_df[bmi_df['age'] < 731],age_days,cbmi,'Age (days)','BMI',range(0,731),'BMI for Age'))
        else:
            if length >= 65 and length <= 120:
                iterator.append((pd.read_csv('wfhanthro.csv'),length,weight,'Height (cm)','Weight (kg)',np.linspace(65, 120,(120-65)*10 + 1),'Weight for height'))
            iterator.append((bmi_df[bmi_df['age'] >= 731],age_days,cbmi,'Age (days)','BMI',range(731,1857),'BMI for Age'))
    if not hc == '':
        iterator.append((pd.read_csv('hcanthro.csv'),age_days,hc,'Age (days)','Head Circumference',range(0,1857),'Head Circumference for Age'))

    for dat in iterator:
        df = dat[0]
        df = df[df['sex'] == sex]
        dct = {}
        for z in range(-3,4):
            dct[z] = df['z=' + str(z)].tolist()
#         inp = range(max(df[5], min(df[6] - 2 * (df[6] - df[2]),df[6] - 30),min(df[6], max(2 * (df[2] - df[5]) + df[5],30 + df[5]))
#         print(dat[4])
#         print(dat[5])
        inp = dat[5]
        plt.plot(inp,dct[3],'k',label = '3DP')
        plt.plot(inp,dct[2],'r',label = '2DP')
        plt.plot(inp,dct[1],'y',label = '1DP')
        plt.plot(inp,dct[0],'g',label = 'Mediana')
        plt.plot(inp,dct[-1],'y',label = '-1DP')
        plt.plot(inp,dct[-2],'r',label = '-2DP')
        plt.plot(inp,dct[-3],'k',label = '-3DP')
        plt.plot([dat[1]],[dat[2]], 'ko')
        plt.legend()
        plt.title(dat[6])
        plt.xlabel(dat[3])
        plt.ylabel(dat[4])
        plt.show()

def AP_display(age_mons,length,weight,sex,cbmi):
#     print(age_mons)
    cbmi = float(cbmi)
    iterator = []
    if not length == '':
        df = pd.read_csv('hfawho2007.csv')
        iterator.append((df,age_mons,length,'Age (months)','Height (cm)',range(61,230),'Height for Age'))
    if (not weight == '') and (age_mons <122):
        iterator.append((pd.read_csv('wfawho2007.csv'),age_mons,weight,'Age (months)','Weight',range(61,122),'Weight for Age'))
    if (not weight == '') and (not length == ''):
        bmi_df = pd.read_csv('bfawho2007.csv')
        iterator.append((bmi_df,age_mons,cbmi,'Age (months)','BMI',range(61,230),'BMI for Age'))

    for dat in iterator:
        df = dat[0]
        df = df[df['sex'] == sex]
        dct = {}
        for z in range(-3,4):
            dct[z] = df['z=' + str(z)].tolist()
        inp = dat[5]
        plt.plot(inp,dct[3],'k',label = '3DP')
        plt.plot(inp,dct[2],'r',label = '2DP')
        plt.plot(inp,dct[1],'y',label = '1DP')
        plt.plot(inp,dct[0],'g',label = 'Mediana')
        plt.plot(inp,dct[-1],'y',label = '-1DP')
        plt.plot(inp,dct[-2],'r',label = '-2DP')
        plt.plot(inp,dct[-3],'k',label = '-3DP')
        plt.plot([dat[1]],[dat[2]], 'ko')
        plt.legend()
        plt.title(dat[6])
        plt.xlabel(dat[3])
        plt.ylabel(dat[4])
        plt.show()
print('')

program = 'Anthro'

step = 1

if TESTING:
    step = 19

while(not step == 19):
    if step == 1:
        new = get_new_census()
        step = process(step,new)
    if step == 2:
        step, number = prompt_process(step,"Family Number: ")
    if step == 3:
        step, sequence = prompt_process(step,"Sequence: ")
    if step == 4:
        step, b_month = prompt_process(step,"Birth Month: ")
    if step == 5:
        step, b_day = prompt_process(step,"Birth Day: ")
    if step == 6:
        step, b_year = prompt_process(step,"Birth Year: ")
    if step == 7:
        step, v_month = prompt_process(step,"Visit Month: ")
    if step == 8:
        step, v_day = prompt_process(step,"Visit Day: ")
    if step == 9:
        step, v_year = prompt_process(step,"Visit Year: ")
    if step == 10:
        weeks = get_weeks()
        step = process(step,weeks)
    if step == 11:
        days = get_days()
        step = process(step,days)
        if step == 10:
            continue
        if ((weeks == '') and (not days == '')) or ((not weeks == '') and (days == '')):
            print("Please give values for both weeks and days.")
            step = 10
            continue

        today = datetime.date.today()
        if v_month == '':
            v_month = today.month
        if v_day == '':
            v_day = today.day
        if v_year == '':
            v_year = today.year

        b_month = int(b_month)
        b_day = int(b_day)
        b_year = int(b_year)
        v_month = int(v_month)
        v_day = int(v_day)
        v_year = int(v_year)

        dob = datetime.date(b_year,b_month,b_day)
        visit_day = datetime.date(v_year,v_month,v_day)
        age_days = (visit_day - dob).days

        if not weeks == '':
            if weeks <= 64:
                program = 'IG'
                days = 7 * weeks + days


        if age_days > 1856:
            program = 'AP'

        age_mons = age_days / 30.4375

        if age_mons >= 229:
            print("\nERROR: Child can be at most 19 years old.\n")
            exit()

        if program == 'IG':
            print('')
            print('Running Intergrowth')
            print('')
            progstr = 'INTERGROWTH'
        if program == 'Anthro':
            print('')
            print('Running Anthro')
            print('')
            progstr = 'ANTHRO'
        if program == 'AP':
            print('')
            print('Running AnthroPlus')
            print('')
            progstr = 'ANTHROPLUS'

    if step == 12:
        sex = get_sex()
        step = process(step,sex)

    if program == 'IG':
        if step == 13:
            step, length = prompt_process(step,"Length (cm): ")
        if step == 14:
            step, weight = prompt_process(step,"Weight (kg): ")
        if step == 15:
            step, hc = prompt_process(step,"Head Circumference (cm): ")
        if step == 16:
            step, obs = prompt_process(step,"Observations: ")
        if step == 17:
            step = 19
    if program == 'Anthro':
        if step == 13:
            lorh = get_lorh()
            step = process(step,lorh)
            if lorh == '':
                length = ''
        if step == 14:
            if lorh == 'l':
                step, length = prompt_process(step,"Length (cm): ")
            if lorh == 'h':
                step, length = prompt_process(step,"Height (cm): ")
            if step == 2:
                step = 3
        if step == 15:
            (step, weight) = prompt_process(step,"Weight (kg): ")
            if step == 14 and (not lorh == 'h' and not lorh == 'l'):
                step = 13
        if step == 16:
            step, hc = prompt_process(step,"Head Circumference (cm): ")
        if step == 17:
            od = get_oedema()
            step = process(step,od)
        if step == 18:
            step, obs = prompt_process(step,"Observations: ")
    if program == 'AP':
        if step == 13:
            step, length = prompt_process(step,"Height (cm): ")
        if step == 14:
            step, weight = prompt_process(step,"Weight (kg): ")
        if step == 15:
            od = get_oedema()
            step = process(step,od)
        if step == 16:
            step, obs = prompt_process(step,"Observations: ")
        if step == 17:
            step = 19


if TESTING:
    number = 'test'
    sequence = 'test'
    if TESTPROG == 'IG':
        program = 'IG'
        progstr = 'INTERGROWTH'
        dob = datetime.date(1,1,1)
        visit_day = datetime.date(1,1,1)
        today = datetime.date.today()
        weeks = 45
        days = 45 * 7
        sex = 'm'
        length = 55
        weight = 4
        hc = 37
        new = 'n'
    if TESTPROG == 'Anthro':
        program = 'Anthro'
        progstr = 'ANTHRO'
        dob = datetime.date(1,1,1)
        visit_day = datetime.date(3,5,1)
        today = datetime.date.today()
        sex = 'f'
        length = 98.7
        weight = 14
        hc = ''
        od = 'n'
        new = 'n'
        lorh = 'h'
        age_days = 1277
    if TESTPROG == 'AP':
        program = 'AP'
        progstr = 'ANTHROPLUS'
        dob = datetime.date(87,3,12)
        visit_day = datetime.date(102,7,14)
        today = datetime.date.today()
        sex = 'f'
        length = 141.5
        weight = 33.7
        hc = ''
        od = 'n'
        new = 'n'
        age_days = (visit_day - dob).days
        age_mons = age_days / 30.4375
        age_mons = 99

if not program == 'IG':
    weeks = math.floor(age_days/7)
    days = age_days % 7


today_is_nonempty = os.path.isfile('today.csv')

if not today_is_nonempty or new == 'y':
    writestr =  'date_of_entry_(d/m/y) , family_number, sequence, observations, program, sex, dob_(d/m/y), dov_(d/m/y), age_in_weeks, days, weight_(kg), length/height_(cm), measure, oedema, head_circumference_(cm), age_(days), adj_length_(cm), BMI, zlen, length_diagnosis, zwei, weight_diagnosis, zwfl, weight-for-length_diagnosis, zbmi, bmi_diagnosis, zhc\n'

else:
    writestr = ''

writestr += today.strftime('%d/%m/%Y') + ', ' + str(number) + ', ' + str(sequence) +  ', ' + str(obs) +  ', ' + str(progstr) + ', ' + str(sex) + ', '
writestr += dob.strftime('%d/%m/%Y') + ", " + visit_day.strftime('%d/%m/%Y') + ", " + str(weeks) + ", " + str(days)

if sex == 'm':
    sex = 1
if sex == 'f':
    sex = 2

if program == 'IG':
    writestr += ', ' + str(weight) + ', ' + str(length) + ', , , ' + str(hc) + ', ' + str(days) + ', ' + str(length) + ', '
    writestr = run_Intergrowth(weeks,days,writestr,sex,length,weight,hc)
if program == 'Anthro':
    writestr += ', ' + str(weight) + ', ' + str(length) + ', ' + lorh + ', ' + str(od) + ', ' + str(hc) + ', ' + str(age_days)
    writestr = run_Anthro(age_days,writestr,sex,lorh,length,weight,hc,od)
if program == 'AP':
    writestr += ', ' + str(weight) + ', ' + str(length) + ', h, ' + od + ', , ' + str(age_days)
    writestr = run_AP(age_days,age_mons,writestr,sex,length,weight,od)

writestr += '\n'

if new == 'y' and today_is_nonempty:
    todaystr = today.strftime('%d-%m-%Y') + '_census'
    filename = todaystr + '.csv'
    n = determine_n(todaystr)
    yest = open('today.csv',"r")
    data = yest.read()
    yest.close()
    if n == 0:
        repo = open(filename,"a")
    else:
        todaystr +=  "(" + str(n+1) + ").csv"
        repo = open(todaystr,"a")
    repo.write(data)
    repo.close()
    out = open('today.csv',"w")
else:
    out = open('today.csv',"a")

out.write(writestr)
out.close()

