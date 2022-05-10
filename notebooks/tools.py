from regex import B
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from gobal_vars import cleanup, cat_cols, replace_columns


def perform_pca(df):
    x=df.values
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
    pca = PCA()
    transf_data = pca.fit_transform(x)
    var_explained = pca.explained_variance_ratio_
    princ_comps = pca.components_
    return princ_comps, var_explained, transf_data, scaler


def plot_transf_data(transf_data, nr_1, nr_2):
    """
    :param nr_1: first principal component that we plot
    :param nr_2: second principal component to plot
    """
    fig, ax = plt.subplots(figsize = (10,10))
    tfont = {'fontname':'Calibri', 'fontsize':20}
    hfont = {'fontname':'Calibri', 'fontsize': 15}
    ax.plot(transf_data[:,nr_1], transf_data[:,nr_2], '*')
    ax.set_title('First two components against each other', **tfont, pad = 10)
    ax.set_xlabel(f'Component {nr_1}', **hfont)
    ax.set_ylabel(f'Component {nr_2}', **hfont)
    return fig, ax

def plot_transf_data_electrics(df, transf_data, nr_1, nr_2):
    el = transf_data[df['FUELTYPE_alternative_fuel']==1]
    non_el = transf_data[df['FUELTYPE_alternative_fuel']!=1]
    fig, ax = plt.subplots(figsize = (10,10))
    tfont = {'fontname':'Calibri', 'fontsize':15}
    hfont = {'fontname':'Calibri', 'fontsize': 10}

    ax.plot(non_el[:,nr_1], non_el[:,nr_2], '*', color='blue')
    ax.plot(el[:,nr_1], el[:,nr_2], '*', color='red')

    ax.set_title('First two components against each other', **tfont, pad = 10)
    ax.set_xlabel(f'Component {nr_1}', **hfont)
    ax.set_ylabel(f'Component {nr_2}', **hfont)
    return fig, ax

def plot_transf_data_electrics_one_comp(df, transf_data, nr_1):
    el = transf_data[df['FUELTYPE_alternative_fuel']==1]
    non_el = transf_data[df['FUELTYPE_alternative_fuel']!=1]
    fig, ax = plt.subplots(figsize = (10,5))
    tfont = {'fontname':'Calibri', 'fontsize':20}
    hfont = {'fontname':'Calibri', 'fontsize': 15}
    ax.plot(np.random.choice(non_el[:,nr_1], len(el[:,nr_1])), np.random.random(len(el[:,nr_1])), '*', color='#990000', label = 'non-electric')
    ax.plot(el[:,nr_1], np.random.random(len(el[:,nr_1])), '*', color='#1f77b4', label = 'electric')
    ax.set_title(f'Component {nr_1+1}', **tfont, pad = 10)
    ax.set_xlabel(f'Component {nr_1+1}', **hfont)
    legend = plt.legend()
    plt.setp(legend.get_texts(), color='black')
    return fig, ax

def plot_comps(princ_comps, x_df, nr_1, nr_2):
    fig, ax = plt.subplots(figsize = (7,10))
    tfont = {'fontname':'Calibri', 'fontsize':20}
    hfont = {'fontname':'Calibri', 'fontsize': 15}
    ax.plot(np.abs(princ_comps[0]))
    ax.plot(np.abs(princ_comps[1]))
    ax.set_xticks(np.arange(len(x_df.columns)), x_df.columns, rotation = 90)
    ax.set_title('First two components against each other', **tfont, pad = 10)
    ax.set_xlabel(f'Component {nr_1}', **hfont)
    ax.set_ylabel(f'Component {nr_2}', **hfont)
    ax.set_ylim(ymin = 0)
    return fig, ax 

def plot_comps_th(princ_comps, df_pca, nr_1,thrshold):
    idxs = princ_comps[nr_1]>thrshold
    fig, ax = plt.subplots(figsize = (7,7))
    tfont = {'fontname':'Calibri', 'fontsize':15}
    hfont = {'fontname':'Calibri', 'fontsize': 10}
    ax.plot(range(np.sum(idxs*1)),np.abs(princ_comps[nr_1][idxs]), color='#1f77b4')
    ax.set_xticks(np.arange(len(df_pca.columns[idxs])), [replace_columns[col_val] for col_val in df_pca.columns[idxs]], rotation = 45)
    ax.set_title(f'Principal component {nr_1+1}', **tfont, pad = 10)
    ax.set_xlabel(f'Component {nr_1}', **hfont)
    ax.set_ylim(ymin = 0)
    return fig, ax 

def one_hot_nhts(df):
    disc_list = ['97', '-9', '-8','-7']
    too_large = pd.get_dummies(df.replace(cleanup), columns = cat_cols)
    all_cols= [i for i in too_large.columns if not any(x in i for x in disc_list)]
    calif2= too_large[all_cols]
    return calif2


def create_pivoted_cars(veh):
    pivoted = veh.pivot_table(index=['HOUSEID',veh.groupby(['HOUSEID','VEHID']).cumcount()], \
                    columns = 'VEHID', \
                    values = ['DRVRCNT','HFUEL', 'HYBRID', 'FUELTYPE', 'HBHUR', 'GSYRGAL'])
    pivoted.columns = [i[0] +'_'+ str(i[1]) for i in pivoted.columns]
    pivoted.index = pivoted.index.droplevel(1)
    pivoted = pivoted.reset_index()
    return pivoted
