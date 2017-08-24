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
  config["GenParticles"] = "" if re.search("(?<!PFembedded).Run201", nickname) else "genParticles"
  config["GenTaus"] = "" if re.search("(?<!PFembedded).Run201", nickname) else "genTaus"
  config["GenTauJets"] = "" if re.search("(?<!PFembedded).Run201|8TeV", nickname) else "tauGenJets"
  config["GenMet"] = "" if re.search("(?<!PFembedded).Run201", nickname) else "genmetTrue"
  config["GenJets"] = ""
  config["Electrons"] = "electrons"
  config["ElectronMetadata"] = "electronMetadata"
  config["Muons"] = "muons"
  config["Taus"] = "taus"
  config["TauMetadata"] = "taus"
  
  if re.search("8TeV|13TeV.*_AODSIM", nickname):     config["TaggedJets"] = "AK5PFTaggedJets"
  elif re.search("MINIAOD|USER", nickname): config["TaggedJets"] = "ak4PF"
  
  if re.search("8TeV", nickname):    config["PileupDensity"] = "KT6Area"
  elif re.search("13TeV", nickname): config["PileupDensity"] = "pileupDensity"
  
  config["Met"] = "met"
  config["PuppiMet"] = "metPuppi" if re.search("(16Dec2015v1|Fall15|Spring16|Run2015)", nickname) else ""
  config["MvaMets"] = "MVAMET"
  #config["PFChargedHadronsPileUp"] = "pfPileUpChargedHadrons"
  #config["PFChargedHadronsNoPileUp"] = "pfNoPileUpChargedHadrons"
  #config["PFChargedHadronsNoPileUp"] = "pfAllChargedParticles"
  #config["PFNeutralHadronsNoPileUp"] = "pfNoPileUpNeutralHadrons"
  #config["PFPhotonsNoPileUp"] = "pfNoPileUpPhotons"
  #config["PackedPFCandidates"] = "packedPFCandidates"
  config["BeamSpot"] = "offlineBeamSpot"
  config["VertexSummary"] = "goodOfflinePrimaryVerticesSummary"
  config["EventMetadata"] = "eventInfo"
  config["LumiMetadata"] = "lumiInfo"
  config["GenEventInfoMetadata"] = "genEventInfoMetadata"
  config["FilterMetadata"] = ""
  config["FilterSummary"] = ""
  config["JetMetadata"] = "jetMetadata"
  config["BeamSpot"] = "offlineBeamSpot"
  config["TriggerInfos"] = "triggerObjectMetadata"
  config["TriggerObjects"] = "triggerObjects"
  

  return config