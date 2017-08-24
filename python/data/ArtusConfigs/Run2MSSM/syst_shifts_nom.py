#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

def build_config(nickname):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz("Kappa/Skimming/data/datasets.json")
  
  
  # define frequently used conditions
  isData = datasetsHelper.isData(nickname)
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  #isTTbar = re.search("TT(To|_|Jets)", nickname)
  #isDY = re.search("DY.?JetsToLLM(50|150)", nickname)
  #isWjets = re.search("W.?JetsToLNu", nickname)
  
  
  ## fill config:
  # includes
  includes = [
    ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["nominal"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  
  
  return config