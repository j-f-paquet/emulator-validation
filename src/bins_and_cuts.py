#!/usr/bin/env python3
import numpy as np

#we can define these centrality bins for all STAR observables
STAR_cent_bins = np.array( [ [0,5],[5,10],[10,20],[20,30],[30,40],[40,50],[50,60],[60,70], [70,80] ] ) # 9 bins
#more central bins to use for parameter estimation to avoid including empty events
central_STAR_cent_bins = np.array( [ [0,5],[5,10],[10,20],[20,30],[30,40],[40,50] ] ) # 6 bins
#more central bins for some PHENIX measurements
central_PHENIX_cent_bins = np.array( [ [0,5],[5,10],[10,15],[15,20],[20,30],[30,40],[40,50] ] ) # 7 bins
#these bins are common to many ALICE observables
ALICE_cent_bins = np.array( [ [0,5],[5,10],[10,20],[20,30],[30,40],[40,50],[50,60],[60,70] ] ) # 8 bins

Tmunu_cents = ALICE_cent_bins

#the observables which will be used for parameter estimation
obs_cent_list = {

'Pb-Pb-2760': {
	'dNch_deta' : ALICE_cent_bins,
	'dET_deta' : np.array([[0, 2.5], [2.5, 5], [5, 7.5], [7.5, 10],
		                   [10, 12.5], [12.5, 15], [15, 17.5], [17.5, 20],
		                   [20, 22.5], [22.5, 25], [25, 27.5], [27.5, 30],
		                   [30, 32.5], [32.5, 35], [35, 37.5], [37.5, 40],
		                   [40, 45], [45, 50], [50, 55], [55, 60],
		                   [60, 65], [65, 70]]), # 22 bins
	'dN_dy_pion'   : ALICE_cent_bins,
	'dN_dy_kaon'   : ALICE_cent_bins,
	'dN_dy_proton' : ALICE_cent_bins,
	'dN_dy_Lambda' : np.array([[0,5],[5,10],[10,20],[20,40],[40,60]]), # 5 bins
	'dN_dy_Omega'  : np.array([[0,10],[10,20],[20,40],[40,60]]), # 4 bins
	'dN_dy_Xi'     : np.array([[0,10],[10,20],[20,40],[40,60]]), # 4 bins
	#'dN_dy_d'      : np.array([[0,10],[10,20],[20,40],[40,60]]), # 4 bins
	'mean_pT_pion'   : ALICE_cent_bins,
	'mean_pT_kaon'   : ALICE_cent_bins,
	'mean_pT_proton' : ALICE_cent_bins,
	#'mean_pT_d'      : np.array([[0,10],[10,20],[20,40],[40,60]]), # 4 bins
	'pT_fluct' : np.array([[0,5],[5,10],[10,15],[15,20], [20,25],[25,30],[30,35],[35,40], [40,45],[45,50],[50,55],[55,60]]), #12 bins
	'v22' : ALICE_cent_bins,
	'v32' : np.array([[0,5],[5,10],[10,20],[20,30], [30,40],[40,50]]), # 6 bins
	'v42' : np.array([[0,5],[5,10],[10,20],[20,30], [30,40],[40,50]]), # 6 bins

	'Tmunu0' : Tmunu_cents,
    'Tmunu1' : Tmunu_cents,
    'Tmunu2' : Tmunu_cents,
    'Tmunu3' : Tmunu_cents,
    'Tmunu4' : Tmunu_cents,
    'Tmunu5' : Tmunu_cents,
    'Tmunu6' : Tmunu_cents,
    'Tmunu7' : Tmunu_cents,
    'Tmunu8' : Tmunu_cents,
    'Tmunu9' : Tmunu_cents,
    'Tmunu_A': Tmunu_cents,
    'Tmunu_00_00': Tmunu_cents,
    'Tmunu_0i_0i': Tmunu_cents,
    'Tmunu_ij_ij': Tmunu_cents,
    #'Tmunu_A2': Tmunu_cents,
    #'Tmunu_xy': Tmunu_cents,
    'Tmunu_tr': Tmunu_cents,
    'Tmunu_cums_0_0_0': Tmunu_cents,
    'Tmunu_cums_0_0_1': Tmunu_cents,
    'Tmunu_cums_0_0_2': Tmunu_cents,
    'Tmunu_cums_0_1_0': Tmunu_cents,
    'Tmunu_cums_0_1_1': Tmunu_cents,
    'Tmunu_cums_0_1_2': Tmunu_cents,
    'Tmunu_cums_0_2_0': Tmunu_cents,
    'Tmunu_cums_0_2_1': Tmunu_cents,
    'Tmunu_cums_0_2_2': Tmunu_cents,
    'Tmunu_cums_1_0_0': Tmunu_cents,
    'Tmunu_cums_1_0_1': Tmunu_cents,
    'Tmunu_cums_1_0_2': Tmunu_cents,
    'Tmunu_cums_1_1_0': Tmunu_cents,
    'Tmunu_cums_1_1_1': Tmunu_cents,
    'Tmunu_cums_1_1_2': Tmunu_cents,
    'Tmunu_cums_1_2_0': Tmunu_cents,
    'Tmunu_cums_1_2_1': Tmunu_cents,
    'Tmunu_cums_1_2_2': Tmunu_cents,
    'Tmunu_cums_2_0_0': Tmunu_cents,
    'Tmunu_cums_2_0_1': Tmunu_cents,
    'Tmunu_cums_2_0_2': Tmunu_cents,
    'Tmunu_cums_2_1_0': Tmunu_cents,
    'Tmunu_cums_2_1_1': Tmunu_cents,
    'Tmunu_cums_2_1_2': Tmunu_cents,
    'Tmunu_cums_2_2_0': Tmunu_cents,
    'Tmunu_cums_2_2_1': Tmunu_cents,
    'Tmunu_cums_2_2_2': Tmunu_cents,
    },

'Pb-Pb-5020': {
	'dNch_deta' : np.array( [ [0,2.5],[2.5,5],[5,7.5],[7.5,10],[10,20],[20,30],[30,40],[40,50],[50,60],[60,70] ] ),
	'dN_dy_pion'   : ALICE_cent_bins,
	'dN_dy_kaon'   : ALICE_cent_bins,
	'dN_dy_proton' : ALICE_cent_bins,
	'dN_dy_d'      : np.array([[0,10],[10,20],[20,40],[40,60]]), # 4 bins
	'mean_pT_pion'   : ALICE_cent_bins,
	'mean_pT_kaon'   : ALICE_cent_bins,
	'mean_pT_proton' : ALICE_cent_bins,
	'mean_pT_d'      : np.array([[0,10],[10,20],[20,40],[40,60]]), # 4 bins
	'v22' : ALICE_cent_bins,
	'v32' : np.array([[0,5],[5,10],[10,20],[20,30],[30,40],[40,50]]), # 6 bins
	'v42' : np.array([[0,5],[5,10],[10,20],[20,30],[30,40],[40,50]]), # 6 bins
    },

'Xe-Xe-5440': {
	'dNch_deta' : np.array( [ [0,2.5],[2.5,5],[5,7.5],[7.5,10],[10,20],[20,30],[30,40],[40,50],[50,60],[60,70] ] ),
	'v22' : ALICE_cent_bins,
	'v32' : ALICE_cent_bins,
    },

'Au-Au-200': {
	'dN_dy_pion'   : central_STAR_cent_bins,
	'dN_dy_kaon'   : central_STAR_cent_bins,
	#current calculations use STAR centrality bins
	#NOTE that the model calculations need to be re-averaged using the PHENIX cent bins if we want to include proton
	'dN_dy_proton' : central_STAR_cent_bins,
	'mean_pT_pion'   : central_STAR_cent_bins,
	'mean_pT_kaon'   : central_STAR_cent_bins,
	'mean_pT_proton' : central_STAR_cent_bins,
	'v22' : central_STAR_cent_bins,
	'v32' : central_STAR_cent_bins,
    },


}

calibration_obs_cent_list = {

'Pb-Pb-2760': {
	'Tmunu0' : Tmunu_cents,
	'Tmunu_A': Tmunu_cents,
    'Tmunu_00_00': Tmunu_cents,
    'Tmunu_0i_0i': Tmunu_cents,
    'Tmunu_ij_ij': Tmunu_cents,
    #'Tmunu_A2': Tmunu_cents,
    #'Tmunu_xy': Tmunu_cents,
    'Tmunu_tr': Tmunu_cents,
    'Tmunu_cums_0_0_0': Tmunu_cents,
    'Tmunu_cums_0_0_1': Tmunu_cents,
    'Tmunu_cums_0_0_2': Tmunu_cents,
    'Tmunu_cums_0_1_0': Tmunu_cents,
    'Tmunu_cums_0_1_1': Tmunu_cents,
    'Tmunu_cums_0_1_2': Tmunu_cents,
    'Tmunu_cums_0_2_0': Tmunu_cents,
    'Tmunu_cums_0_2_1': Tmunu_cents,
    'Tmunu_cums_0_2_2': Tmunu_cents,
    'Tmunu_cums_1_0_0': Tmunu_cents,
    'Tmunu_cums_1_0_1': Tmunu_cents,
    'Tmunu_cums_1_0_2': Tmunu_cents,
    'Tmunu_cums_1_1_0': Tmunu_cents,
    'Tmunu_cums_1_1_1': Tmunu_cents,
    'Tmunu_cums_1_1_2': Tmunu_cents,
    'Tmunu_cums_1_2_0': Tmunu_cents,
    'Tmunu_cums_1_2_1': Tmunu_cents,
    'Tmunu_cums_1_2_2': Tmunu_cents,
    'Tmunu_cums_2_0_0': Tmunu_cents,
    'Tmunu_cums_2_0_1': Tmunu_cents,
    'Tmunu_cums_2_0_2': Tmunu_cents,
    'Tmunu_cums_2_1_0': Tmunu_cents,
    'Tmunu_cums_2_1_1': Tmunu_cents,
    'Tmunu_cums_2_1_2': Tmunu_cents,
    'Tmunu_cums_2_2_0': Tmunu_cents,
    'Tmunu_cums_2_2_1': Tmunu_cents,
    'Tmunu_cums_2_2_2': Tmunu_cents,

    },
}


#these just define some 'reasonable' ranges for plotting purposes
obs_range_list = {
    'Pb-Pb-2760': {
		'dNch_deta': [0,2000],
		'dET_deta': [0,2200],
		'dN_dy_pion': [0,1700],
		'dN_dy_kaon': [0,400],
		'dN_dy_proton': [0,120],
		'dN_dy_Lambda': [0,40],
		'dN_dy_Omega': [0,2],
		'dN_dy_Xi': [0,10],
		'mean_pT_pion': [0,1],
		'mean_pT_kaon': [0,1.5],
		'mean_pT_proton': [0,2],
		'pT_fluct': [0,0.05],
		'v22': [0,0.16],
		'v32': [0,0.1],
		'v42': [0,0.1]
    },
	'Au-Au-200': {
		'dNch_deta': [0,1000],
		'dET_deta': [0,1200],
		'dN_dy_pion': [0,800],
		'dN_dy_kaon': [0,120],
		'dN_dy_proton': [0,40],
		'dN_dy_Lambda': [0,40],
		'dN_dy_Omega': [0,2],
		'dN_dy_Xi': [0,10],
		'mean_pT_pion': [0,1],
		'mean_pT_kaon': [0,1.5],
		'mean_pT_proton': [0,2],
		'pT_fluct': [0,0.05],
		'v22': [0,0.16],
		'v32': [0,0.1],
		'v42': [0,0.1]
    },
}
