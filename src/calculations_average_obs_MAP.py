#!/usr/bin/env python3

import numpy as np
#import h5py
import sys, os, glob
# Input data format
from calculations_file_format_single_event import *
# Output data format
from configurations import *
from calculations_average_obs import *

if __name__ == '__main__':
    print("Computing observables for MAP events ")
    MAP_dir = str(workdir/'model_calculations/MAP') + '/' + idf_label_short[idf]
    for system in system_strs:
        try:
            print("System = " + system)
            file_input = MAP_dir + '/Events/results_' + system + '.dat'
            file_output = MAP_dir + '/Obs/obs_' + system + '.dat'
            print("Averaging events in " + file_input)
            print("##########################")
            results = []
            results.append(load_and_compute(file_input, system)[0])
            results = np.array(results)
            print("results.shape = " + str(results.shape))
            results.tofile(file_output)
        except:
            print("No MAP events found for system " + s)
