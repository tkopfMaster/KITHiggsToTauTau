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
  if re.search("Run2015", nickname):
    config["JetEnergyCorrectionParameters"] = [
      "#$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_L1FastJet_AK4PFchs.txt",
      "#$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_L2Relative_AK4PFchs.txt",
      "#$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_L3Absolute_AK4PFchs.txt",
      "#$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_L2L3Residual_AK4PFchs.txt"
    ]
    config["JetEnergyCorrectionUncertaintyParameters"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_Uncertainty_AK4PFchs.txt"
  else:
    config["JetEnergyCorrectionParameters"] = [
      "#$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_MC_L1FastJet_AK4PFchs.txt",
      "#$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_MC_L2Relative_AK4PFchs.txt",
      "#$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_MC_L3Absolute_AK4PFchs.txt"
    ]
    config["JetEnergyCorrectionUncertaintyParameters"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_MC_Uncertainty_AK4PFchs.txt"
  
  #config["JetEnergyCorrectionUncertaintySource"] = ""
  #config["JetEnergyCorrectionUncertaintyShift"] = 0.0
  config["JetEnergyCorrectionSplitUncertainty"] = True
  config["JetEnergyCorrectionSplitUncertaintyParameters"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Summer16/Summer16_23Sep2016V4_DATA_UncertaintySources_AK4PFchs.txt"
  config["UseJECShiftsForBJets"] = True
  config["JetEnergyCorrectionSplitUncertaintyParameterNames"] = [
    "AbsoluteFlavMap",
    "AbsoluteMPFBias",
    "AbsoluteScale",
    "AbsoluteStat",
    "FlavorQCD",
    "Fragmentation",
    "PileUpDataMC",
    "PileUpPtBB",
    "PileUpPtEC1",
    "PileUpPtEC2",
    "PileUpPtHF",
    "PileUpPtRef",
    "RelativeBal",
    "RelativeFSR",
    "RelativeJEREC1",
    "RelativeJEREC2",
    "RelativeJERHF",
    "RelativePtBB",
    "RelativePtEC1",
    "RelativePtEC2",
    "RelativePtHF",
    "RelativeStatEC",
    "RelativeStatFSR",
    "RelativeStatHF",
    "SinglePionECAL",
    "SinglePionHCAL",
    "TimePtEta",
    "Total",
    "Closure"
  ]


  return config