#!usr/bin/env python
# coding: utf-8

import mne
import numpy as np
import pandas as pd
from mne.time_frequency import tfr_morlet

def type_one():
    chs = ['O1', 'Oz', 'O2']
    freq_min, freq_max = 1, 31
    cyc_min, cyc_max = 1, 12
    sub_list = ['sub-05', 'sub-06', 'sub-08', 'sub-09', 'sub-10', 'sub-11']
    cond = ['Hit', 'FA', 'Miss', 'CR']
    df = pd.DataFrame(None, columns=['Hit', 'FA', 'Miss', 'CR'])
    freqs = np.arange(freq_min, freq_max, 1)
    n_cycles = np.linspace(cyc_min, cyc_max, num=30)
    for i in sub_list:
        epo1 = mne.read_epochs('/home/quantum/Pre Stim 2IFC/' + i + '/type 1 tfr analysis/' + i + '_task-tfr-analysis-1st_epo.fif')
        epo2 = mne.read_epochs('/home/quantum/Pre Stim 2IFC/' + i + '/type 1 tfr analysis/' + i + '_task-tfr-analysis-2nd_epo.fif')
        epochs = mne.concatenate_epochs([epo1, epo2])
        epochs = epochs.pick_channels(chs)
        power = tfr_morlet(epochs, freqs=freqs, n_cycles=n_cycles,
            return_itc=False, average=False)
        power.save('/home/quantum/Pre Stim 2IFC/' + i + '/type 1 tfr analysis/' + i + '_task_morlet-tfr.h5', overwrite=True)
        for x in range(len(cond)):
            temp = power[cond[x]].average()
            cond_avg = temp.data.mean(axis=0)[7:14,:].mean(axis=0)
            shape_avg = cond_avg[1300:1501]
            df[cond[x]] = shape_avg.tolist()
        save = df.to_csv('/home/quantum/Pre Stim 2IFC/' + i + '/' + i + '_task-tfr-analysis-data.csv', index=True)
    return


def type_two():
    chs = ['O1', 'Oz', 'O2']
    freq_min, freq_max = 1, 31
    cyc_min, cyc_max = 1, 8
    sub_list = ['sub-05', 'sub-06', 'sub-08', 'sub-09', 'sub-10', 'sub-11']
    cond = ['Hit', 'FA', 'Miss', 'CR']
    df = pd.DataFrame(None, columns=['Hit', 'FA', 'Miss', 'CR'])
    freqs = np.arange(freq_min, freq_max, 1)
    n_cycles = np.linspace(cyc_min, cyc_max, num=30)
    for i in sub_list:
        epo1 = mne.read_epochs('/home/quantum/Pre Stim 2IFC/' + i + '/type 2 tfr analysis/' + i + '_task-tfr-analysis-1st_epo.fif')
        epo2 = mne.read_epochs('/home/quantum/Pre Stim 2IFC/' + i + '/type 2 tfr analysis/' + i + '_task-tfr-analysis-2nd_epo.fif')
        epochs = mne.concatenate_epochs([epo1, epo2])
        epochs = epochs.pick_channels(chs)
        power = tfr_morlet(epochs, freqs=freqs, n_cycles=n_cycles,
            return_itc=False, average=False)
        power.save('/home/quantum/Pre Stim 2IFC/' + i + '/type 2 tfr analysis/' + i + '_task_morlet_-tfr.h5', overwrite=True)

        for x in range(len(cond)):
            temp = power[cond[x]].average()
            cond_avg = temp.data.mean(axis=0)[7:14,:].mean(axis=0)
            shape_avg = cond_avg[1300:1501]
            df[cond[x]] = shape_avg.tolist()
        save = df.to_csv('/home/quantum/Pre Stim 2IFC/' + i + '/' + i + '_task-tfr-analysis-single-data.csv', index=True)
    return

def main():
    type = input("Which SDT Type?: ")
    if int(type) > 1:
        type_two()
    else:
        type_one()
    return

if __name__ == '__main__':
  main()
