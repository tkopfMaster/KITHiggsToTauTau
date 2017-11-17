#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import copy
import Artus.Utility.jsonTools as jsonTools
#import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz
import importlib
#import os

def build_config(nickname):
  config = jsonTools.JsonDict()
  #datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))
  
  
  ## fill config:
  # includes
  includes = [
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMuonID"
    ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["VetoMuonID"] = "loose"
  
  config["VetoMuonIsoType"] = "user"
  config["VetoMuonIso"] = "none"
  config["VetoMuonIsoPtSumOverPtUpperThresholdEB"] = 0.3
  config["VetoMuonIsoPtSumOverPtUpperThresholdEE"] = 0.3
  
  config["VetoMuonLowerPtCuts"] = ["15.0"]
  config["VetoMuonUpperAbsEtaCuts"] = ["2.4"]
  config["DiVetoMuonMinDeltaRCut"] = "0.15"
  config["DiVetoMuonVetoMode"] = "veto_os_keep_ss"
  config["DirectIso"] = True
  
  
  return config
