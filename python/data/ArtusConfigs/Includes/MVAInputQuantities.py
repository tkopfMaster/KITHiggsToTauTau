#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

def build_list():
  quantities_list = [
    "TrainingSelectionValue",
    "pVecSum",
    "pScalSum",
    "min_ll_jet_eta",
    "abs_min_ll_jet_eta",
    "lep1_centrality",
    "lep2_centrality",
    "product_lep_centrality",
    "diLep_centrality",
    "diLep_diJet_deltaR",
    "abs_min_ll_jet_eta",
    "diLepBoost",
    "diLepJet1DeltaR",
    "diLepDeltaR",
    "dmjj",
    "diJetSymEta_1",
    "diJetSymEta_2",
    "diJetDeltaR",
    "diJetAbsDeltaPhi",
    "nJets20",
    "jccsv_1",
    "jccsv_2",
    "jccsv_3",
    "jccsv_4",
    "diCJetSymEta_1",
    "diCJetSymEta_2",
    "diCJetDeltaR",
    "diCJetAbsDeltaPhi",
    "diCJetDeltam",
    "jcpt_1",
    "jcpt_2",
    "jcm_1",
    "jcm_2",
    "diCJetm",
    "pVecSumCSVJets"
  ]
  '''
    
  '''
  
  return quantities_list