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
import os

def build_config(nickname):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))
  
  # define frequently used conditions
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  
  ## fill config:
  # includes
  includes = [
    ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["BTaggedJetID_documentation"] = "https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#b_tagging"
  config["BTaggedJetCombinedSecondaryVertexName"] = "pfCombinedInclusiveSecondaryVertexV2BJetTags"
  config["BTaggerWorkingPoints"] = [
    "tight:0.9535",
    "medium:0.8484",
    "loose:0.5426"
  ]
  config["BTaggedJetAbsEtaCut"] = 2.4
  config["ApplyBTagSF"] = False
  config["JetTaggerUpperCuts"] = []
  config["BTagSFMethod"] = "PromotionDemotion"
  config["BTagShift"] = 0
  config["BMistagShift"] = 0
  

  return config
