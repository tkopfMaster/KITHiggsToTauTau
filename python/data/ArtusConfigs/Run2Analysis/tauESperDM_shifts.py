#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
#import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz
#import os

def build_config(nickname):
  config = jsonTools.JsonDict()
  #datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))
  
  
  # define frequently used conditions
  #isEmbedded = datasetsHelper.isEmbedded(nickname)
  #isData = datasetsHelper.isData(nickname) and (not isEmbedded)
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
  if re.search("Summer16", nickname):
    config["tauEsOneProngUp"] = {
      "TauEnergyCorrectionOneProngShift" : 1.012,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsOneProngDown"] = {
      "TauEnergyCorrectionOneProngShift" : 0.988,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsOneProngPiZerosUp"] = {
      "TauEnergyCorrectionOneProngPiZerosShift" : 1.012,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsOneProngPiZerosDown"] = {
      "TauEnergyCorrectionOneProngPiZerosShift" : 0.988,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsThreeProngUp"] = {
      "TauEnergyCorrectionThreeProngShift" : 1.012,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsThreeProngDown"] = {
      "TauEnergyCorrectionThreeProngShift" : 0.988,
      "SvfitCacheFileFolder" : "nominal"
    }
  elif re.search("Embedding2016", nickname):
    config["tauEsOneProngUp"] = {
      "TauEnergyCorrectionOneProngShift" : 1.03,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsOneProngDown"] = {
      "TauEnergyCorrectionOneProngShift" : 0.97,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsOneProngPiZerosUp"] = {
      "TauEnergyCorrectionOneProngPiZerosShift" : 1.03,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsOneProngPiZerosDown"] = {
      "TauEnergyCorrectionOneProngPiZerosShift" : 0.97,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsThreeProngUp"] = {
      "TauEnergyCorrectionThreeProngShift" : 1.03,
      "SvfitCacheFileFolder" : "nominal"
    }
    config["tauEsThreeProngDown"] = {
      "TauEnergyCorrectionThreeProngShift" : 0.97,
      "SvfitCacheFileFolder" : "nominal"
    }
  
  
  return config