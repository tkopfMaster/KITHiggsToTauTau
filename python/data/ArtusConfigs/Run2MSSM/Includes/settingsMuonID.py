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
    ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  
  config["Year"] = 2016 if re.search("(Spring16|Summer16|Run2016|Embedding2016)", nickname) else 2015
  
  config["MuonID"] = "mediumHIPsafe2016" if re.search("(Run|Embedding)2016(B|C|D|E|F)|Spring16", nickname) else "medium"
  
  config["MuonIsoTypeUserMode"] = "fromcmsswr04" if re.search("(Spring16|Summer16|Run2016|Embedding2016)", nickname) else "fromcmssw"
    
  config["MuonIsoType"] = "user"
  config["MuonIso"] = "none"
  config["MuonIsoSignalConeSize"] = 0.4
  config["MuonDeltaBetaCorrectionFactor"] = 0.5
  config["MuonTrackDxyCut"] = 0.045
  config["MuonTrackDzCut"] = 0.2


  return config