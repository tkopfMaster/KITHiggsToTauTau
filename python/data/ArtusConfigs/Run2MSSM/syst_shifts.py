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
  
  if isEmbedded:
    config["tauEsUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsUp"]["TauEnergyCorrectionShift"] = 1.016
    
    config["tauEsDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["tauEsDown"]["TauEnergyCorrectionShift"] = 0.984
    
    
    config["muonEsUp"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["muonEsUp"]["MuonEnergyCorrectionShift"] = 1.01
      
    config["muonEsDown"] = {
      "JetEnergyCorrectionUncertaintyShift" : [0.0]
    }
    config["muonEsDown"]["MuonEnergyCorrectionShift"] = 0.99
  
  if not (isEmbedded or isData):
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
  
  
  return config