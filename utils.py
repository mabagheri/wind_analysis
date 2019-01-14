import pandas as pd
import numpy as np
import datetime
import glob
import matplotlib
import matplotlib.pyplot as plt
import string
import sys
import re
import os
from os.path import isfile,join,isdir
from itertools import permutations, combinations_with_replacement, product
sys.path.insert(0, 'supplementary files')
#from saxpy import SAX
# import time
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Segoe UI Symbol','simHei','Arial','sans-serif']

###############################################################################################################################
def load_resample_data(years, resampling_period = '15T'):
    raw_data = []
    for year in (years):
        raw_data_year = pd.read_csv(os.path.join('NRGstreamData','Merged_data','original_data_'+ str(year) 
                               + '-01-01_'+ str(year) + '-12-31_5.csv'), index_col = 'DT')
        raw_data.append(raw_data_year)
        print('year:'+ str(year) + '\t' + str(raw_data_year.shape))
    raw_data = pd.concat(raw_data)
    
    # convert index to datestime format
    raw_data.index = raw_data.index.map(datetime_convertor)

    # Resmaple data
    data = raw_data.resample(resampling_period).mean()
    print('resampled to ',str(data.shape))   
    
    #### Convert data to Intetger  OR  round data 
    pd.options.display.float_format = '{:.2f}'.format
    data = data.round(decimals=2)
    # data = data.astype(int)
    
    return data

def read_and_merge_rawdata(fromDate, toDate, data_folder, labels, Sk_rows=0):
    data_files = glob.glob(join(data_folder,"*.csv"))
    for i in range(len(data_files)): #glob.glob(join(data_folder,"*.csv")):    
        print('Reading', data_files[i])
        data = pd.read_csv(data_files[i],skiprows = Sk_rows, names = ["Date/Time","MW"])
        if i == 0:
            original_data = data
            continue

        original_data = pd.merge(original_data,data,on='Date/Time', how='outer')

    original_data.columns = ['DT'] + labels   
    original_data['DT'] = original_data['DT'].apply(datetime_convertor)
    original_data.set_index('DT', inplace =True)
        
    return original_data

def datetime_convertor(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

###############################################################################################################################
def normalize_data(data):
    from sklearn import preprocessing

    # Create a minimum and maximum processor object
    min_max_scaler = preprocessing.MinMaxScaler()

    # Create an object to transform the data to fit minmax processor
    x_scaled = min_max_scaler.fit_transform(data)

    # Run the normalizer on the dataframe
    normalized_data = pd.DataFrame(x_scaled, columns=data.columns, index = data.index)
    
    return normalized_data

def normalize_data_by_min_max(data):
    mins = data.min(axis=0)
    maxs = data.max(axis=0)
    return ((data - mins) / (maxs - mins))  

###############################################################################################################################
def categorical_rep_SAX(data,alphabet_size=8):
    SAX_reps = pd.DataFrame(columns=['Rep'])

    L = data.shape[0]
    n_timeseries = data.shape[1]

    for i in range(n_timeseries):
        sax_object = SAX(wordSize=L, alphabetSize=alphabet_size) #,epsilon
        sax_rep = sax_object.to_letter_rep(data.iloc[:,i].values)[0]
        SAX_reps.loc[i] = sax_rep #list(sax_rep)
        
    return SAX_reps

def categorical_rep_qcut(data,alphabet_size=8):
    
    qcut_reps = pd.DataFrame(columns=['Rep'])

    L = data.shape[0]
    n_timeseries = data.shape[1]

    for i in range(n_timeseries):
        aa = np.array(data.iloc[:,i].values)
        print(aa)
        w = pd.qcut(np.array(data.iloc[:,i]), 8, labels=list(string.ascii_lowercase[:alphabet_size]))
        L = ''.join(k for k in w)

        qcut_reps.loc[i] = L 
        
    return qcut_reps

def categorical_rep_mycode(data,alphabet_size,alphabets):
    qcut_reps = pd.DataFrame(columns=['Rep'])

    L = data.shape[0]
    n_timeseries = data.shape[1]

    for i in range(n_timeseries):
        x = np.array(data.iloc[:,i].values)
        bins = np.arange(min(x),max(x),(max(x)-min(x))/alphabet_size+0.0001)
        bins = np.arange(0,1,1/alphabet_size)

        inds = np.digitize(x,bins,right=False)
        dic = dict(zip(range(1,alphabet_size+1),alphabets))

        L = [dic.get(n, n) for n in inds]
        L = ''.join((k) for k in L)
        #print(L)

        qcut_reps.loc[i] = L 
        
    return qcut_reps

def categorical_rep_mycode_df(data, cols, alphabet_size,alphabets):
    qcut_reps = pd.DataFrame(columns=cols)

    L = data.shape[0]
    n_timeseries = data.shape[1]

    for i in range(len(cols)):
        x = np.array(data.iloc[:,i].values)
        #bins = np.arange(min(x),max(x),(max(x)-min(x))/alphabet_size+0.0001)
        bins = np.arange(0,1,1/alphabet_size)
        inds = np.digitize(x,bins,right=False)
        #print(type(inds))
        #print(inds[:6])
        dic = dict(zip(range(1,alphabet_size+1),alphabets))
        
        L = [dic.get(n, n) for n in inds]
        #print(type(L))
        se = pd.Series(L)
        #L = ''.join((k) for k in L)
        #print(L)

        qcut_reps[cols[i]] = se 
    
    qcut_reps.index = data.index
    return qcut_reps

###############################################################################################################################
def find_most_freq_motifs2(categorical_rep, candidate_motifs, n_most_frequent_motifs, method):
    """ 
    This function finds the most frequent motifs in a single time series   
    """
    if method == 'count':
        motifs = {j: categorical_rep.count(j) for j in candidate_motifs}
    elif method == 're_findall':
        motifs = {j: len(re.findall('(?='+j+')',categorical_rep)) for j in candidate_motifs}
    
    # print(type(motifs))
    motifs_sorted_by_occurance = sorted(motifs.items(), key=lambda x:x[1],reverse=True)[:n_most_frequent_motifs]
        
    return motifs_sorted_by_occurance

###############################################################################################################################
def find_most_frequent_patterns_set_timeseries(categorical_reps_joined):
    """
    This function find the frequency of all pattern (pattern happened at the same time)
    of set of time series; sort them and returns in DF format
    e.x. how often all was at the first level of operation.
    """
    import collections
    counter = collections.Counter(categorical_reps_joined)
    Frequency_patterns = pd.DataFrame.from_dict(counter, orient='index').reset_index()
    Frequency_patterns.rename(columns={'index':'Pattern', 0:'Frequency'}, inplace=True)
    Frequency_patterns.sort_values(by='Frequency',inplace=True,ascending=False)
    Frequency_patterns.set_index('Pattern',inplace=True)
    return Frequency_patterns


###############################################################################################################################
def find_all(main_str, sub_str):
    start = 0
    indices = []
    while True:
        start = main_str.find(sub_str, start)
        if start == -1: break
        #yield start
        indices.append(start)
        start += len(sub_str) # use start += 1 to find overlapping matches
    return indices

def find_all_sparse(a_str,sub):
    x = np.zeros(len(a_str))
    ind = find_all(a_str,sub)
    print(ind)
    x[ind] = 1
    return x

###############################################################################################################################
import itertools
from sklearn.metrics import confusion_matrix
def plot_confusion_matrix(cm, classes, x_label='x_label', y_label='y_label', 
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    else:
        cm = cm

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    
    # Create colorbar
#     cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
#     cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 ha="center", va="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    
###############################################################################################################################

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Arguments:
        data       : A 2D numpy array of shape (N,M)
        row_labels : A list or array of length N with the labels
                     for the rows
        col_labels : A list or array of length M with the labels
                     for the columns
    Optional arguments:
        ax         : A matplotlib.axes.Axes instance to which the heatmap
                     is plotted. If not provided, use current axes or
                     create a new one.
        cbar_kw    : A dictionary with arguments to
                     :meth:`matplotlib.Figure.colorbar`.
        cbarlabel  : The label for the colorbar
    All other arguments are directly passed on to the imshow call.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw, shrink = 1, fraction =0.1) #orientation = 'horizontal'
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)
    
    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Arguments:
        im         : The AxesImage to be labeled.
    Optional arguments:
        data       : Data used to annotate. If None, the image's data is used.
        valfmt     : The format of the annotations inside the heatmap.
                     This should either use the string format method, e.g.
                     "$ {x:.2f}", or be a :class:`matplotlib.ticker.Formatter`.
        textcolors : A list or array of two color specifications. The first is
                     used for values below a threshold, the second for those
                     above.
        threshold  : Value in data units according to which the colors from
                     textcolors are applied. If None (the default) uses the
                     middle of the colormap as separation.

    Further arguments are passed on to the created text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)


    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[im.norm(data[i, j]) > threshold])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

######################################################################################
def heatmap2(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", ind_0 = 0, ind_1=1, **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Arguments:
        data       : A 2D numpy array of shape (N,M)
        row_labels : A list or array of length N with the labels
                     for the rows
        col_labels : A list or array of length M with the labels
                     for the columns
    Optional arguments:
        ax         : A matplotlib.axes.Axes instance to which the heatmap
                     is plotted. If not provided, use current axes or
                     create a new one.
        cbar_kw    : A dictionary with arguments to
                     :meth:`matplotlib.Figure.colorbar`.
        cbarlabel  : The label for the colorbar
    All other arguments are directly passed on to the imshow call.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar : YOU HAD TO UNCOMMENT THEN COMMENT THE FOLLOWING TWO LINES !!
#     cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw, shrink = 1, fraction =0.1) #orientation = 'horizontal'
#     cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")
    
    # ax.set_title('Joint Probabilty: Cluster {} & Cluster{}'.format(ind_0+1, ind_1+1), y=-0.1, fontsize=11)
    # ax.set_xlabel('Cluster {}'.format(ind_0+1),fontsize=11)
    ax.set_title('Cluster {}'.format(ind_0+1),fontsize=11, pad = 25)
    ax.set_ylabel('Cluster {}'.format(ind_1+1),fontsize=11)

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels, fontsize=12)
    ax.set_yticklabels(row_labels, fontsize= 12)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
#     plt.setp(ax.get_xticklabels(), rotation=0, ha="right",
#              rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    # the following lines's goal is to show white grids
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)
    
    #fig.tight_layout()

    return im #, cbar


def annotate_heatmap2(im, data=None, valfmt="{x:.2f}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Arguments:
        im         : The AxesImage to be labeled.
    Optional arguments:
        data       : Data used to annotate. If None, the image's data is used.
        valfmt     : The format of the annotations inside the heatmap.
                     This should either use the string format method, e.g.
                     "$ {x:.2f}", or be a :class:`matplotlib.ticker.Formatter`.
        textcolors : A list or array of two color specifications. The first is
                     used for values below a threshold, the second for those
                     above.
        threshold  : Value in data units according to which the colors from
                     textcolors are applied. If None (the default) uses the
                     middle of the colormap as separation.

    Further arguments are passed on to the created text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)


    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[im.norm(data[i, j]) > threshold])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

def dist_two_points(lat1,lon1,lat2,lon2):
    from math import sin, cos, sqrt, atan2, radians
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c