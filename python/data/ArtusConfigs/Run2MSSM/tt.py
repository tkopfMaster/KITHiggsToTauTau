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
  
  
  # define frequently used conditions
  isData = datasetsHelper.isData(nickname)
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  isTTbar = re.search("TT(To|_|Jets)", nickname)
  isDY = re.search("DY.?JetsToLLM(50|150)", nickname)
  isWjets = re.search("W.?JetsToLNu", nickname)
  
  
  ## fill config:
  # includes
  includes = [
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsLooseElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsLooseMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsTauID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsJEC",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsBTaggedJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsTauES",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsMinimalPlotlevelFilter_tt"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["Channel"] = "TT"
  config["MinNTaus"] = 2
  config["HltPaths"] = [
          "HLT_IsoMu22",
          "HLT_IsoTkMu22",
          "HLT_IsoMu22_eta2p1",
          "HLT_IsoTkMu22_eta2p1",
          "HLT_VLooseIsoPFTau120_Trk50_eta2p1",
          "HLT_Ele25_eta2p1_WPTight_Gsf",
          "HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg",
          "HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg",
          "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",
          "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL"
    ]
  
  config["TauID"] = "TauIDRecommendation13TeV"
  config["TauUseOldDMs"] = True
  config["TauLowerPtCuts"] = ["40.0"]
  config["TauUpperAbsEtaCuts"] = ["2.1"]
  config["DiTauPairMinDeltaRCut"] = 0.5
  config["DiTauPairIsTauIsoMVA"] = True
  config["DiTauPairHLTLast"] = True
  config["HLTBranchNames"] = [
      "trg_singlemuon:HLT_IsoMu22_v",
      "trg_singlemuon:HLT_IsoTkMu22_v",
      "trg_singlemuon:HLT_IsoMu22_eta2p1_v",
      "trg_singlemuon:HLT_IsoTkMu22_eta2p1_v",
      "trg_singletau:HLT_VLooseIsoPFTau120_Trk50_eta2p1_v",
      "trg_singleelectron:HLT_Ele25_eta2p1_WPTight_Gsf_v",
      "trg_doubletau:HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v",
      "trg_doubletau:HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v",
      "trg_muonelectron:HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v",
      "trg_muonelectron:HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"
  ]
  config["DiTauPairHltPathsWithoutCommonMatchRequired"] = [
      "HLT_IsoMu22_v",
      "HLT_IsoTkMu22_v",
      "HLT_IsoMu22_eta2p1_v",
      "HLT_IsoTkMu22_eta2p1_v",
      "HLT_VLooseIsoPFTau120_Trk50_eta2p1_v",
      "HLT_Ele25_eta2p1_WPTight_Gsf_v"
  ]
  config["EventWeight"] = "eventWeight"
  config["RooWorkspace"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/htt_scalefactors_v16_5.root"
  config["TauTauTriggerWeightWorkspace"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/htt_scalefactors_v16_5.root"
  config["TauTauTriggerWeightWorkspaceWeightNames"] = [
      "0:triggerWeight",
      "1:triggerWeight"
  ]
  config["TauTauTriggerWeightWorkspaceObjectNames"] = [
      "0:t_genuine_MediumIso_tt_ratio,t_fake_MediumIso_tt_ratio",
      "1:t_genuine_MediumIso_tt_ratio,t_fake_MediumIso_tt_ratio"
  ]
  config["TauTauTriggerWeightWorkspaceObjectArguments"] = [
      "0:t_pt,t_dm",
      "1:t_pt,t_dm"
  ]
  config["FakeFaktorFiles"] = [
      "inclusive:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/fakeFactorWeights/medium/tt/inclusive/fakeFactors_20170628_medium.root",
      "nobtag:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/fakeFactorWeights/medium/tt/nobtag/fakeFactors_20170628_medium.root",
      "btag:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/fakeFactorWeights/medium/tt/btag/fakeFactors_20170628_medium.root"
  ]
  
  config["TauTauRestFrameReco"] = "collinear_approximation"
  config["TauTriggerFilterNames"] = [
          "HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v:hltDoublePFTau35TrackPt1MediumIsolationDz02Reg",
          "HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v:hltDoublePFTau35TrackPt1MediumCombinedIsolationDz02Reg"
    ]
  config["TriggerObjectLowerPtCut"] = 28.0
  config["BTagWPs"] = ["medium"]
  config["InvalidateNonMatchingElectrons"] = False
  config["InvalidateNonMatchingMuons"] = False
  config["InvalidateNonMatchingTaus"] = True
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True
  
  config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.syncQuantities").build_list()
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.weightQuantities").build_list())
  #config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.MVAInputQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.lheWeights").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.zptQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.fakeFactorWeightQuantities_tt").build_list())
  config["Quantities"].extend([
      "had_gen_match_pT_1",
      "had_gen_match_pT_2"
  ])
  
  config["OSChargeLeptons"] = True
  config["TopPtReweightingStrategy"] = "Run1"
  
  config["Processors"] =                                     ["producer:HttValidLooseElectronsProducer",
                                                              "producer:HttValidLooseMuonsProducer",
                                                              "producer:HltProducer",
                                                              "producer:MetSelector"]
  if not isData:                 config["Processors"].append( "producer:TauCorrectionsProducer")
  config["Processors"].extend((                               "producer:ValidTausProducer",
                                                              "filter:ValidTausFilter",
                                                              "producer:TauTriggerMatchingProducer",
                                                              "filter:MinTausCountFilter",
                                                              "producer:ValidElectronsProducer",
                                                              "producer:ValidMuonsProducer",
                                                              "producer:ValidTTPairCandidatesProducer",
                                                              "filter:ValidDiTauPairCandidatesFilter",
                                                              "producer:Run2DecayChannelProducer",#"producer:MvaMetSelector",
                                                              "producer:ValidTaggedJetsProducer",
                                                              "producer:ValidBTaggedJetsProducer",
                                                              "producer:TaggedJetCorrectionsProducer"))
  if not isData:                 config["Processors"].extend(("producer:MetCorrector", #"producer:MvaMetCorrector"
                                                              "producer:SimpleEleTauFakeRateWeightProducer",
                                                              "producer:SimpleMuTauFakeRateWeightProducer",
                                                              "producer:TauTauTriggerWeightProducer"))
  if isTTbar:                    config["Processors"].append( "producer:TopPtReweightingProducer")
  if isDY:                       config["Processors"].append( "producer:ZPtReweightProducer")
  config["Processors"].extend((                               "filter:MinimalPlotlevelFilter",
                                                              "producer:TauTauRestFrameSelector",
                                                              "producer:DiLeptonQuantitiesProducer",
                                                              "producer:DiJetQuantitiesProducer",
                                                              "producer:JetToTauFakesProducer",
                                                              "producer:EventWeightProducer"))
  
  
  
  config["AddGenMatchedTaus"] = True
  config["AddGenMatchedTauJets"] = True
  config["BranchGenMatchedTaus"] = True
  config["Consumers"] = ["KappaLambdaNtupleConsumer",
                         "cutflow_histogram"]
                         #"CutFlowTreeConsumer",
                         #"KappaElectronsConsumer",
                         #"KappaTausConsumer",
                         #"KappaTaggedJetsConsumer",
                         #"RunTimeConsumer",
                         #"PrintEventsConsumer"
  
  
  # pipelines - systematic shifts
  systs = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.syst_shifts").build_config(nickname)
  config_with_systs = jsonTools.JsonDict()
  for key, syst in systs.items():
    longkey = "tt_" + key
    config_with_systs[longkey] = jsonTools.JsonDict(syst)
    config_with_systs[longkey] += config
  return config_with_systs