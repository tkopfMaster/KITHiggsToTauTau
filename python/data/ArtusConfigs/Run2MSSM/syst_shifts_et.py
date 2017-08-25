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
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  isData = datasetsHelper.isData(nickname) and (not isEmbedded)
  #isTTbar = re.search("TT(To|_|Jets)", nickname)
  isDY = re.search("DY.?JetsToLLM(50|150)", nickname)
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
    
  
  if not isData:
    config["tauEsOneProngUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngUp"]["TauEnergyCorrectionOneProng"] = 1.007
    
    config["tauEsOneProngDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngDown"]["TauEnergyCorrectionOneProng"] = 0.983
    
    
    config["tauEsOneProngOnePiZeroUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngOnePiZeroUp"]["TauEnergyCorrectionOneProngPiZeros"] = 1.023
    
    config["tauEsOneProngOnePiZeroDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsOneProngOnePiZeroDown"]["TauEnergyCorrectionOneProngPiZeros"] = 0.999
    
    
    config["tauEsThreeProngUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsThreeProngUp"]["TauEnergyCorrectionThreeProng"] = 1.018
    
    config["tauEsThreeProngDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsThreeProngDown"]["TauEnergyCorrectionThreeProng"] = 0.994
    
    
  if isDY or isEmbedded:
    config["eleTauEsOneProngZeroPiZeroUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["eleTauEsOneProngZeroPiZeroUp"]["TauElectronFakeEnergyCorrectionOneProng"] = 1.029
    
    config["eleTauEsOneProngZeroPiZeroDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["eleTauEsOneProngZeroPiZeroDown"]["TauElectronFakeEnergyCorrectionOneProng"] = 1.019
    
    
    config["eleTauEsOneProngOnePiZeroUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["eleTauEsOneProngOnePiZeroUp"]["TauElectronFakeEnergyCorrectionOneProngPiZeros"] = 1.086
    
    config["eleTauEsOneProngOnePiZeroDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["eleTauEsOneProngOnePiZeroDown"]["TauElectronFakeEnergyCorrectionOneProngPiZeros"] = 1.066
  
  
  return config