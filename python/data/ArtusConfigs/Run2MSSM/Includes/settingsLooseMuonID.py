#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import copy
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz
import importlib

def build_config(nickname):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz("Kappa/Skimming/data/datasets.json")
  
  
  ## fill config:
  # includes
  includes = [
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsMuonID"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  
  config["Year"] = 2016 if re.search("(Spring16|Summer16|Run2016|Embedding2016)", nickname) else 2015
  
  config["LooseMuonID"] = "mediumHIPsafe2016" if re.search("(Run|Embedding)2016(B|C|D|E|F)|Spring16", nickname) else "medium"
  
  config["LooseMuonIsoType"] = "user"
  config["LooseMuonIso"] = "none"
  config["LooseMuonIsoPtSumOverPtUpperThresholdEB"] = 0.3
  config["LooseMuonIsoPtSumOverPtUpperThresholdEE"] = 0.3
  
  config["LooseMuonLowerPtCuts"] = ["10.0"]
  config["LooseMuonUpperAbsEtaCuts"] = ["2.4"]
  config["LooseMuonTrackDxyCut"] = 0.045
  config["LooseMuonTrackDzCut"] = 0.2
  config["DirectIso"] = True


  return config