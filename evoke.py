#!/usr/bin/env python
# coding: utf-8

import mne
import os
import numpy as np



def epo_data(epochs):
    epo_name = ['Hit', 'FA', 'Miss', 'CR']
    #epo_name = ['Hit/S', 'FA/S', 'Miss/S', 'CR/S']
    evo_name = ['Hit', 'FA', 'Miss', 'CR']
    #evo_name = ['Hit', 'FA', 'Miss', 'CR']
    evoked_list = []
    #chs = ['O1', 'Oz', 'O2']
    for i in range(len(epo_name)):
        evo_name[i] = epochs[epo_name[i]].average()
        evoked_list.append(evo_name[i])
    return evoked_list



def main():
    sub_list = ['sub-05', 'sub-06', 'sub-07', 'sub-08', 'sub-09', 'sub-10',
        'sub-11']
    for sub in sub_list:
        epo1 = mne.read_epochs('/home/nick/Pre Stim 2IFC/' + sub + '/type 1 tf analysis/' + sub + '_task-tf-analysis-1st_epo.fif')
        epo2 = mne.read_epochs('/home/nick/Pre Stim 2IFC/' + sub + '/type 1 tf analysis/' + sub + '_task-tf-analysis-2nd_epo.fif')
        epochs = mne.concatenate_epochs([epo1, epo2])
        epochs = epochs.filter(l_freq=8.0, h_freq=13.0)
        evoked_list = epo_data(epochs)
        save = mne.write_evokeds('/home/nick/Pre Stim 2IFC/' + sub + '/type 1 tf analysis/' + sub + '_task-evoked-data_ave.fif', evoked_list)
    return



if __name__ == '__main__':
    #ch = input("Which channel(s) do you want to pick?: ")
    main()
