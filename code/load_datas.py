#############################################################################################################
# load features and labels                                                                                  #
# feature dimension : (N,d), (i.e., N*4096), label dimension : (N,)                                         #
# type of all the output will be "list"                                                                     #
#############################################################################################################
# There are two different setting of training and testing :                                                 #
# The default setting (setting-0) is splitting the dataset into two parts, half for training, half for      #
# testing. Training index: lab-1234, office-123, house-123. Testing index: lab-5678, office-456, house-456  #
#############################################################################################################

import sys, os
import numpy as np
import pdb
import warnings

def load_one_label_seq(path):
    npy = np.load(path)
    return npy


def load_label_seqs(path, mode, index):
    labels=[]
    for i in xrange(len(index)):
        loc = index[i][0]
        idx = index[i][1]
        labelnpy = os.path.join(path,loc,mode+"_left"+str(idx)+'.npy')
        labels.append(load_one_label_seq(labelnpy))
        labelnpy = os.path.join(path,loc,mode+"_right"+str(idx)+'.npy')
        labels.append(load_one_label_seq(labelnpy))
    return labels

def gen_index(setting_index):
    train_index=[]
    test_index =[]
    if setting_index == 0:
        for i in xrange(1,9):
            if i <= 4:
                train_index.append(('lab',i))
            else:
                test_index.append(('lab',i))
        for i in xrange(1,7):
            if i <= 3:
                train_index.append(('office',i))
            else:
                test_index.append(('office',i))
        for i in xrange(1,7):
            if i <= 3:
                train_index.append(('house',i))
            else:
                test_index.append(('house',i))
    elif setting_index == 1:
        for i in xrange(1,9):
            train_index.append(('lab',i))
        for i in xrange(1,7):
            train_index.append(('office',i))
        for i in xrange(1,7):
            test_index.append(('house',i))
    else:
        raise ValueError ('error setting index')

    return train_index, test_index



def gen_index_process(index=None, setting_index=None):
    if index == None:
        if setting_index==None:
            raise ValueError('Setting index can not be none')
        else:
            train_index, test_index = gen_index(setting_index)
    return train_index, test_index
    

def load_train_labels(path, mode, index=None, setting_index=None):
    if index == None:
        index,_ = gen_index_process(index,setting_index)
    else:
        if setting_index != None:
            warnings.warn('setting_index has no effect when given particular index')
    labels = load_label_seqs(path, mode, index)
    return labels

def load_test_labels(path, mode, index=None, setting_index=None):
    if index == None:
        _,index = gen_index_process(index,setting_index)
    else:
        if setting_index != None:
            warnings.warn('setting_index has no effect when given particular index')
    labels = load_label_seqs(path, mode, index)
    return labels


def load_all_labels(path, mode, setting_index):
    train_index, test_index = gen_index(setting_index)
    train_labels = load_train_labels(path, mode,train_index)
    test_labels = load_train_labels(path, mode,test_index)
    return train_labels, test_labels




