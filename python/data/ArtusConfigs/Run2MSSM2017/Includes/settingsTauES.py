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

def build_config(nickname, **kwargs):
  config = jsonTools.JsonDict()
  #datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))


  ## fill config:
  # includes
  includes = [
    ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)

  # explicit configuration
  config["TauEnergyCorrection"] = "mssmhtt2016"

  if re.search("Run201|Embedding", nickname):
    config["TauEnergyCorrectionOneProng"] = 1.0
    config["TauEnergyCorrectionOneProngPiZeros"] = 1.0
    config["TauEnergyCorrectionThreeProng"] = 1.0
    config["TauElectronFakeEnergyCorrectionOneProng"] = 1.0
    config["TauElectronFakeEnergyCorrectionOneProngPiZeros"] = 1.0
  else:
    # recent numbers for Tau ES: Slide 14, m_vis fit: https://indico.cern.ch/event/763206/contributions/3170631/attachments/1730040/2795667/Izaak_TauPOG_TauES_20181008_v0.pdf
    config["TauEnergyCorrectionOneProng"] = 1.007 # down: 0.999, central: 1.007, up: 1.015
    config["TauEnergyCorrectionOneProngPiZeros"] = 0.998 # down: 0.990, central: 0.998, up: 1.006
    config["TauEnergyCorrectionThreeProng"] = 1.001 # down: 0.992, central: 1.001, up: 1.010
    config["TauElectronFakeEnergyCorrectionOneProng"] = 1.01 #TODO these are 2017 values from IC!
    config["TauElectronFakeEnergyCorrectionOneProngPiZeros"] = 1.041 #TODO these are 2017 values from IC!
  return config
