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

import HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.ArtusConfigUtility as ACU

def build_config(nickname):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))


  # define frequently used conditions
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  isData = datasetsHelper.isData(nickname) and (not isEmbedded)
  isTTbar = re.search("TT(To|_|Jets)", nickname)
  isDY = re.search("DY.?JetsToLLM(50|150)", nickname)
  isWjets = re.search("W.?JetsToLNu", nickname)
  isHtt = re.search("HToTauTau", nickname)


  ## fill config:
  # includes
  includes = [
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsLooseElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsLooseMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsVetoElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsTauID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsJEC",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsBTaggedJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsTauES",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2Analysis.Includes.settingsMinimalPlotlevelFilter_ee"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)

  # explicit configuration
  config["Channel"] = "EE"
  config["MinNElectrons"] = 2
  # HltPaths_comment: The first path must be the single lepton trigger. A corresponding Pt cut is implemented in the Run2DecayChannelProducer.
  if re.search("(Run2016|Embedding2016|Summer16|Embedding2017|Run2017|Spring17|Fall17)", nickname): config["HltPaths"] = [
      "HLT_Ele27_WPTight_Gsf",
      "HLT_Ele32_WPTight_Gsf",
      "HLT_Ele35_WPTight_Gsf"
  ]
  #config["ElectronLowerPtCuts"] = ["26.0"]
  config["ElectronLowerPtCuts"] = ["10.0"]
  config["ElectronUpperAbsEtaCuts"] = ["2.1"]
  config["RooWorkspace"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/htt_scalefactors_v16_5.root"
  config["RooWorkspaceWeightNames"] = [
      "0:triggerWeight",
      "0:idweight",
      "0:isoweight",
      "0:trackWeight",
      "1:idweight",
      "1:isoweight",
      "1:trackWeight"
  ]
  config["RooWorkspaceObjectNames"] = [
      "0:e_trg_binned_ratio",
      "0:e_iso_binned_ratio",
      "0:e_id_ratio",
      "0:e_trk_ratio",
      "1:e_iso_binned_ratio",
      "1:e_id_ratio",
      "1:e_trk_ratio"
  ]
  config["RooWorkspaceObjectArguments"] = [
      "0:e_pt,e_eta,e_iso",
      "0:e_pt,e_eta,e_iso",
      "0:e_pt,e_eta",
      "0:e_pt,e_eta",
      "1:e_pt,e_eta,e_iso",
      "1:e_pt,e_eta",
      "1:e_pt,e_eta"
  ]
  config["EventWeight"] = "eventWeight"
  config["TauTauRestFrameReco"] = "collinear_approximation"
  if re.search("(Run2016|Embedding2016|Summer16|Embedding2017|Run2017|Spring17|Fall17)", nickname): config["ElectronTriggerFilterNames"] = [
                    "HLT_Ele27_WPTight_Gsf_v:hltEle27WPTightGsfTrackIsoFilter",
                    "HLT_Ele32_WPTight_Gsf_v:hltEle32WPTightGsfTrackIsoFilter",
                    "HLT_Ele35_WPTight_Gsf_v:hltEle35noerWPTightGsfTrackIsoFilter"
    ]

  config["InvalidateNonMatchingElectrons"] = True
  config["InvalidateNonMatchingMuons"] = False
  config["InvalidateNonMatchingTaus"] = False
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True

  config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.TagAndProbe.Includes.TagAndProbeQuantitiesZee").build_list()

  config["Processors"] = [                                  "producer:HltProducer",
                                                            "producer:TagAndProbeElectronPairProducer",
                                                            "filter:ValidElectronsFilter",
                                                            "producer:ElectronTriggerMatchingProducer",
                                                            "producer:EventWeightProducer"]

  config["AddGenMatchedParticles"] = True
  config["AddGenMatchedTaus"] = True
  config["AddGenMatchedTauJets"] = True
  config["BranchGenMatchedElectrons"] = True
  config["BranchGenMatchedTaus"] = True
  config["Consumers"] = ["TagAndProbeElectronPairConsumer",
                         "cutflow_histogram"]
                         #"CutFlowTreeConsumer",
                         #"KappaElectronsConsumer",
                         #"KappaTausConsumer",
                         #"KappaTaggedJetsConsumer",
                         #"RunTimeConsumer",
                         #"PrintEventsConsumer"


  # pipelines - systematic shifts
  return ACU.apply_uncertainty_shift_configs('ee', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.syst_shifts_nom").build_config(nickname))
