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
  config["TauEnergyCorrection"] = "mssmhtt2016" if re.search("Summer16|Embedding2016", nickname) else "none"
  
  if re.search("Run201", nickname):
    config["TauEnergyCorrectionOneProng"] = 1.0
    config["TauEnergyCorrectionOneProngPiZeros"] = 1.0
    config["TauEnergyCorrectionThreeProng"] = 1.0
    config["TauElectronFakeEnergyCorrectionOneProng"] = 1.0
    config["TauElectronFakeEnergyCorrectionOneProngPiZeros"] = 1.0
  else:
    config["TauEnergyCorrectionOneProng"] = 0.995
    config["TauEnergyCorrectionOneProngPiZeros"] = 1.011
    config["TauEnergyCorrectionThreeProng"] = 1.006
    config["TauElectronFakeEnergyCorrectionOneProng"] = 1.024
    config["TauElectronFakeEnergyCorrectionOneProngPiZeros"] = 1.076
  

  return config