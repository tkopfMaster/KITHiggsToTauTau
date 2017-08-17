#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

def build_config(nickname, process=None):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz("Kappa/Skimming/data/datasets.json")
  
  
  # define frequently used conditions
  isData = datasetsHelper.isData(nickname)
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  #isTTbar = re.match("TT(To|_|Jets)", nickname)
  #isDY = re.match("DY.?JetsToLLM(50|150)", nickname)
  #isWjets = re.match("W.?JetsToLNu", nickname)
  
  
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
  
  
  config["tauEsUp"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["tauEsUp"]["TauEnergyCorrectionShift"] = 1.016 if isEmbedded else 1.0
  
  config["tauEsDown"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["tauEsDown"]["TauEnergyCorrectionShift"] = 0.984 if isEmbedded else 1.0
  
  
  config["muonEsUp"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["muonEsUp"]["MuonEnergyCorrectionShift"] = 1.01 if isEmbedded else 1.0
  
  config["muonEsDown"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["muonEsDown"]["MuonEnergyCorrectionShift"] = 0.99 if isEmbedded else 1.0
  
  
  config["tauEsOneProngUp"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["tauEsOneProngUp"]["TauEnergyCorrectionOneProng"] = 1.0 if isEmbedded or isData else 1.007
  
  config["tauEsOneProngDown"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["tauEsOneProngDown"]["TauEnergyCorrectionOneProng"] = 1.0 if isEmbedded or isData else 0.983
  
  
  config["tauEsOneProngOnePiZeroUp"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["tauEsOneProngOnePiZeroUp"]["TauEnergyCorrectionOneProngPiZeros"] = 1.0 if isEmbedded or isData else 1.023
  
  config["tauEsOneProngOnePiZeroDown"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["tauEsOneProngOnePiZeroDown"]["TauEnergyCorrectionOneProngPiZeros"] = 1.0 if isEmbedded or isData else 0.999
  
  
  config["tauEsThreeProngUp"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["tauEsThreeProngUp"]["TauEnergyCorrectionThreeProng"] = 1.0 if isEmbedded or isData else 1.018
  
  config["tauEsThreeProngDown"] = {
    "JetEnergyCorrectionUncertaintyShift" : [0.0]
  }
  config["tauEsThreeProngDown"]["TauEnergyCorrectionThreeProng"] = 1.0 if isEmbedded or isData else 0.994
  
  
  return config