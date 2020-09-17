import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import threading
from matplotlib.pyplot import plot, draw, show
import seaborn as sns


#explore graph: gender
def task1():
    df = pd.read_csv('covid.csv')
    patients_no = df['id'].count()
    patients_f = df.loc[df['sex'] == 2]['sex'].count()
    patients_m = df.loc[df['sex'] == 1]['sex'].count()
    labels = 'Females', 'Males'
    sizes = [patients_f / patients_no * 100, patients_m / patients_no * 100]
    colors = ['#F48FB1', '#42A5F5']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=colors)
    ax1.axis('equal')
    plt.title('COVID-19 cases by Gender')
    plt.show()

#explore dataset: tabacco
def task2():
    df = pd.read_csv('covid.csv', usecols=['tobacco'])
    df.tobacco.unique()
    df['tobacco'].replace(1, 'Yes', inplace=True)
    df['tobacco'].replace(2, 'No', inplace=True)
    df['tobacco'].replace(98, 'N/A', inplace=True)
    sns.catplot(x="tobacco", data=df, kind='count')
    plt.title('COVID-19 and Tobacco Usage', size=15)
    plt.xticks(size=10)
    plt.show()

#explore dataset: contact with positive COVID-19 cases
def task3():
    df = pd.read_csv('covid.csv', usecols=['contact_other_covid'])
    df.contact_other_covid.unique()
    df['contact_other_covid'].replace(1, 'Yes', inplace=True)
    df['contact_other_covid'].replace(2, 'No', inplace=True)
    df['contact_other_covid'].replace(99, 'N/A', inplace=True)
    sns.catplot(x='contact_other_covid', data=df, kind='count')
    plt.title('Contact with positive COVID-19 cases', size=15)
    plt.xlabel('Contact with positive COVID-19 cases')
    plt.xticks(size=10)

# explore dataset: obesity pre-condition
def task4():
    df = pd.read_csv('covid.csv', usecols=['obesity'])
    df.obesity.unique()
    df['obesity'].replace(1, 'Yes', inplace=True)
    df['obesity'].replace(2, 'No', inplace=True)
    df['obesity'].replace(98, 'N/A', inplace=True)
    sns.catplot(x='obesity', data=df, kind='count')
    plt.title('COVID-19 and Obesity Pre-condition', size=15)
    plt.xticks(size=10)

# explore dataset: hypertension
def task5():
    df = pd.read_csv('covid.csv', usecols=['hypertension'])
    df.hypertension.unique()
    df['hypertension'].replace(1, 'Yes', inplace=True)
    df['hypertension'].replace(2, 'No', inplace=True)
    df['hypertension'].replace(98, 'N/A', inplace=True)
    sns.catplot(x='hypertension', data=df, kind='count')
    plt.title('COVID-19 and Hypertension Pre-condition', size=15)
    plt.xticks(size=10)

# explore dataset: asthma
def task6():
    df = pd.read_csv('covid.csv', usecols=['asthma'])
    df.asthma.unique()
    df['asthma'].replace(1, 'Yes', inplace=True)
    df['asthma'].replace(2, 'No', inplace=True)
    df['asthma'].replace(98, 'N/A', inplace=True)
    sns.catplot(x='asthma', data=df, kind='count')
    plt.title('COVID-19 and Asthma Pre-condition', size=15)
    plt.xticks(size=10)

# explore dataset: diabetes
def task7():
    df = pd.read_csv('covid.csv', usecols=['diabetes'])
    df.diabetes.unique()
    df['diabetes'].replace(1, 'Yes', inplace=True)
    df['diabetes'].replace(2, 'No', inplace=True)
    df['diabetes'].replace(98, 'N/A', inplace=True)
    sns.catplot(x='diabetes', data=df, kind='count')
    plt.title('COVID-19 Diabetes Pre-condition', size=15)
    plt.xticks(size=10)

# explore dataset: pregnancy
def task8():
    df = pd.read_csv('covid.csv', usecols=['pregnancy'])
    df.pregnancy.unique()
    df['pregnancy'].replace(1, 'Yes', inplace=True)
    df['pregnancy'].replace(2, 'No', inplace=True)
    df['pregnancy'].replace(97, 'N/A', inplace=True)
    df['pregnancy'].replace(98, 'N/A', inplace=True)
    sns.catplot(x='pregnancy', data=df, kind='count')
    plt.title('COVID-19 and Pregnant Patients', size=15)
    plt.xticks(size=10)

#covid by age
def task9():
    df = pd.read_csv('covid.csv')
    ages = [0] * 13
    for index in df['age']:
        i = index // 10
        ages[i] = ages[i] + 1
    fig = plt.figure()
    age = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-99']
    patient_count = ages[:10]
    color = ['#0E6655']
    plt.bar(age, patient_count, color=color)
    plt.xlabel('Age')
    plt.ylabel('Number of patients')
    plt.title('COVID-19 cases by age group')

#compare: intubed: males vs femalesage
def task10():
    df = pd.read_csv('covid.csv')
    df['intubed'] = df['intubed'].map({1: 1, 2: 2, 97: 3, 99: 3})
    df['intubed'].replace(1, 'Yes', inplace=True)
    df['intubed'].replace(2, 'No', inplace=True)
    df['sex'].replace(1, 'Female', inplace=True)
    df['sex'].replace(2, 'Male', inplace=True)
    indexnames = df[df['intubed'] == 3].index
    df.drop(indexnames, inplace=True)
    sns.countplot(x='intubed', data=df, hue='sex')
    plt.title('Patients that required intubation \nBy Gender', size=17)
    plt.xticks(size=10)

#compare: intubed: smokers vs nonsmokers
def task11():
    df = pd.read_csv('covid.csv')
    df['intubed'] = df['intubed'].map({1: 1, 2: 2, 98: 3})
    df['intubed'].replace(1, 'Yes', inplace=True)
    df['intubed'].replace(2, 'No', inplace=True)
    df['tobacco'].replace(1, 'Smokers', inplace=True)
    df['tobacco'].replace(2, 'Non-smokers', inplace=True)
    df['tobacco'].replace(98, 'N/A', inplace=True)
    indexnames = df[df['intubed'] == 3].index
    df.drop(indexnames, inplace=True)
    sns.countplot(x='intubed', data=df, hue='tobacco')
    plt.title('Patients that required intubation \nTobacco Usage', size=17)
    plt.xticks(size=10)

#compare: intubed: obesity vs no
def task12():
        df = pd.read_csv('covid.csv')
        df['intubed'] = df['intubed'].map({1: 1, 2: 2, 98: 3})
        df['intubed'].replace(1, 'Yes', inplace=True)
        df['intubed'].replace(2, 'No', inplace=True)
        df['obesity'].replace(1, 'Obesity Pre-condition', inplace=True)
        df['obesity'].replace(2, 'No Pre-condition', inplace=True)
        df['obesity'].replace(98, 'N/A', inplace=True)
        indexnames = df[df['intubed'] == 3].index
        df.drop(indexnames, inplace=True)
        sns.countplot(x='intubed', data=df, hue='obesity')
        plt.title('Patients that required intubation \nObesity Pre-condition', size=17)
        plt.xticks(size=10)

#compare: intubed: obesity vs no
def task13():
        df = pd.read_csv('covid.csv')
        df['intubed'] = df['intubed'].map({1: 1, 2: 2, 98: 3})
        df['intubed'].replace(1, 'Yes', inplace=True)
        df['intubed'].replace(2, 'No', inplace=True)
        df['hypertension'].replace(1, 'Obesity Pre-condition', inplace=True)
        df['hypertension'].replace(2, 'No Pre-condition', inplace=True)
        df['hypertension'].replace(98, 'N/A', inplace=True)
        indexnames = df[df['intubed'] == 3].index
        df.drop(indexnames, inplace=True)
        sns.countplot(x='intubed', data=df, hue='hypertension')
        plt.title('Patients that required intubation \nHypertension Pre-condition', size=17)
        plt.xticks(size=10)

def task14():
    df = pd.read_csv('covid.csv')
    df['intubed'] = df['intubed'].map({1: 1, 2: 2, 98: 3})
    df['intubed'].replace(1, 'Yes', inplace=True)
    df['intubed'].replace(2, 'No', inplace=True)
    df['asthma'].replace(1, 'Asthma Pre-condition', inplace=True)
    df['asthma'].replace(2, 'No Pre-condition', inplace=True)
    df['asthma'].replace(98, 'N/A', inplace=True)
    indexnames = df[df['intubed'] == 3].index
    df.drop(indexnames, inplace=True)
    sns.countplot(x='intubed', data=df, hue='asthma')
    plt.title('Patients that required intubation \nAsthma Pre-condition', size=17)
    plt.xticks(size=10)

def task15():
    df = pd.read_csv('covid.csv')
    df['intubed'] = df['intubed'].map({1: 1, 2: 2, 98: 3})
    df['intubed'].replace(1, 'Yes', inplace=True)
    df['intubed'].replace(2, 'No', inplace=True)
    df['diabetes'].replace(1, 'Diabetes Pre-condition', inplace=True)
    df['diabetes'].replace(2, 'No Pre-condition', inplace=True)
    df['diabetes'].replace(98, 'N/A', inplace=True)
    indexnames = df[df['intubed'] == 3].index
    df.drop(indexnames, inplace=True)
    sns.countplot(x='intubed', data=df, hue='diabetes')
    plt.title('Patients that required intubation \nDiabetes Pre-condition', size=17)
    plt.xticks(size=10)

def task16():
    df = pd.read_csv('covid.csv')
    df['intubed'] = df['intubed'].map({1: 1, 2: 2, 98: 3})
    df['intubed'].replace(1, 'Yes', inplace=True)
    df['intubed'].replace(2, 'No', inplace=True)
    df['pregnancy'].replace(1, 'Diabetes Pre-condition', inplace=True)
    df['pregnancy'].replace(2, 'No Pre-condition', inplace=True)
    df['pregnancy'].replace(98, 'N/A', inplace=True)
    df['pregnancy'].replace(97, 'N/A', inplace=True)
    indexnames = df[df['intubed'] == 3].index
    df.drop(indexnames, inplace=True)
    sns.countplot(x='intubed', data=df, hue='pregnancy')
    plt.title('Patients that required intubation \nPregnant Patients', size=17)
    plt.xticks(size=10)

def options():
    print("What do you want to find out?")
    print("0.Exit Project")
    print("1.COVID-19 cases by Gender")
    print("2.COVID-19 and Tobacco Usage")
    print("3.Contact with Positive COVID-19 Cases")
    print("4.COVID-19 and Obesity Pre-condition")
    print("5.COVID-19 and Hypertension Pre-condition")
    print("6.COVID-19 and Asthma Pre-condition")
    print("7.COVID-19 and Diabetes Pre-condition")
    print("8.COVID-19 and Pregnant Patients")
    print("9.COVID-19 cases by Age Group")
    print("10.Patients that required intubation - By Gender")
    print("11.Patients that required intubation - Tobacco Usage")
    print("12.Patients that required intubation - Obesity Pre-condition")
    print("13.Patients that required intubation - Hypertension Pre-condition")
    print("14.Patients that required intubation - Asthma Pre-condition")
    print("15.Patients that required intubation - Diabetes Pre-condition")
    print("16.Patients that required intubation - Pregnant Patients")
    opt=input("Your answer:")
    return opt

def introduction():
    print("People with risk factors may be more likely to need hospitalization "
          "or intensive care while infected with COVID-19.\nThis presentation aims"
          " to create an insightful visualisation of these key risk factors.\nBased"
          " on data published by the Mexican Government, this project analyses attributes"
          " of over 500,000 patients.")

def tasks(opt):
    if opt=='1':
        task1()
    elif opt=='2':
        task2()
    elif opt=='3':
        task3()
    elif opt=='4':
        task4()
    elif opt=='5':
        task5()
    elif opt=='6':
        task6()
    elif opt=='7':
        task7()
    elif opt=='8':
        task8()
    elif opt=='9':
        task9()
    elif opt=='10':
        task10()
    elif opt=='11':
        task11()
    elif opt=='12':
        task12()
    elif opt=='13':
        task13()
    elif opt=='14':
        task14()
    elif opt=='15':
        task15()
    elif opt=='16':
        task16()
    else:
        print("The option you have selected is not available.")

def main():
    introduction()
    opt=options()
    while opt!='0':
        tasks(opt)
        plt.tight_layout(pad=1, w_pad=1, h_pad=1)
        plt.show()
        opt=options()
    print("Thank you!\n This project was delivered by Gabriele Blazyte, Raluca-Teodora Pop and Teodora-Elena Toma.")


main()

