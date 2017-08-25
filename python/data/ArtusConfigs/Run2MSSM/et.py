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

import HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.ArtusConfigUtility as ACU

def build_config(nickname):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz("Kappa/Skimming/data/datasets.json")
  
  
  # define frequently used conditions
  isEmbedded = datasetsHelper.isEmbedded(nickname)
  isData = datasetsHelper.isData(nickname) and (not isEmbedded)
  isTTbar = re.search("TT(To|_|Jets)", nickname)
  isDY = re.search("DY.?JetsToLLM(50|150)", nickname)
  isWjets = re.search("W.?JetsToLNu", nickname)
  
  
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
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsMinimalPlotlevelFilter_et"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["Channel"] = "ET"
  config["MinNElectrons"] = 1
  config["MinNTaus"] = 1
  # HltPaths_comment: The first path must be the single lepton trigger. A corresponding Pt cut is implemented in the Run2DecayChannelProducer..
  if re.search("(Run2016|Embedding2016|Summer16)", nickname): config["HltPaths"] = [
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
  config["ElectronLowerPtCuts"] = ["26.0"]
  config["ElectronUpperAbsEtaCuts"] = ["2.1"]
  config["TauLowerPtCuts"] = ["30.0"]
  config["TauUpperAbsEtaCuts"] = ["2.3"]
  config["DiTauPairMinDeltaRCut"] = 0.5
  config["DiTauPairIsTauIsoMVA"] = True
  config["DiTauPairNoHLT"] = False
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
  config["RooWorkspace"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/htt_scalefactors_v16_5_embedding.root" if isEmbedded else "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/htt_scalefactors_v16_5.root"
  config["RooWorkspaceWeightNames"] = [
      "0:triggerWeight",
      "0:idweight",
      "0:isoweight",
      "0:trackWeight"
  ]
  config["RooWorkspaceObjectNames"] = [
      "0:e_trg_binned_ratio",
      "0:e_iso_binned_ratio",
      "0:e_id_ratio",
      "0:e_trk_ratio"
  ]
  config["RooWorkspaceObjectArguments"] = [
      "0:e_pt,e_eta,e_iso",
      "0:e_pt,e_eta,e_iso",
      "0:e_pt,e_eta",
      "0:e_pt,e_eta"
  ]
  config["FakeFaktorFiles"] = [
      "inclusive:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/fakeFactorWeights/tight/et/inclusive/fakeFactors_20170628_tight.root",
      "nobtag_tight:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/fakeFactorWeights/tight/et/nobtag_tight/fakeFactors_20170628_tight.root",
      "nobtag_loosemt:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/fakeFactorWeights/tight/et/nobtag_loosemt/fakeFactors_20170628_tight.root",
      "btag_tight:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/fakeFactorWeights/tight/et/btag_tight/fakeFactors_20170628_tight.root",
      "btag_loosemt:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/fakeFactorWeights/tight/et/btag_loosemt/fakeFactors_20170628_tight.root"
  ]
  config["EventWeight"] = "eventWeight"
  config["TauTauRestFrameReco"] = "collinear_approximation"
  if re.search("(Run2016|Embedding2016|Summer16)", nickname): config["ElectronTriggerFilterNames"] = [
          "HLT_Ele25_eta2p1_WPTight_Gsf_v:hltEle25erWPTightGsfTrackIsoFilter",
          "HLT_VLooseIsoPFTau120_Trk50_eta2p1_v:hltPFTau120TrackPt50LooseAbsOrRelVLooseIso"
    ]
  config["TauTriggerFilterNames"] = [
          "HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v:hltPFTau20TrackLooseIso",
          "HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v:hltOverlapFilterIsoEle22WPLooseGsfLooseIsoPFTau20"
    ]
  config["BTagWPs"] = ["medium"]
  config["InvalidateNonMatchingElectrons"] = True
  config["InvalidateNonMatchingMuons"] = False
  config["InvalidateNonMatchingTaus"] = True
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True
  
  config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.syncQuantities").build_list()
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.weightQuantities").build_list())
  #config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.MVAInputQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.zptQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.lheWeights").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.fakeFactorWeightQuantities").build_list())
  config["Quantities"].extend([
      "had_gen_match_pT_1",
      "had_gen_match_pT_2"
  ])
  
  config["OSChargeLeptons"] = True
  config["TopPtReweightingStrategy"] = "Run1"
  
  config["Processors"] =                                     [] if (isData or isEmbedded) else ["producer:ElectronCorrectionsProducer"]
  config["Processors"].extend((                               "producer:HttValidLooseElectronsProducer",
                                                              "producer:HttValidLooseMuonsProducer",
                                                              "producer:HltProducer",
                                                              "producer:MetSelector",
                                                              "producer:ValidElectronsProducer",
                                                              "filter:ValidElectronsFilter",
                                                              "producer:ElectronTriggerMatchingProducer",
                                                              "filter:MinElectronsCountFilter",
                                                              "producer:HttValidVetoElectronsProducer",
                                                              "producer:ValidMuonsProducer"))
  if not isData:                 config["Processors"].append( "producer:TauCorrectionsProducer")
  config["Processors"].extend((                               "producer:ValidTausProducer",
                                                              "filter:ValidTausFilter",
                                                              "producer:TauTriggerMatchingProducer",
                                                              "filter:MinTausCountFilter",
                                                              "producer:ValidETPairCandidatesProducer",
                                                              "filter:ValidDiTauPairCandidatesFilter",
                                                              "producer:Run2DecayChannelProducer", #"producer:MvaMetSelector",
                                                              "producer:DiVetoElectronVetoProducer",
                                                              "producer:ValidTaggedJetsProducer",
                                                              "producer:ValidBTaggedJetsProducer",
                                                              "producer:TaggedJetCorrectionsProducer"))
  if not (isData or isEmbedded): config["Processors"].append( "producer:MetCorrector") #"producer:MvaMetCorrector"
  config["Processors"].extend((                               "producer:TauTauRestFrameSelector",
                                                              "producer:DiLeptonQuantitiesProducer",
                                                              "producer:DiJetQuantitiesProducer"))
  if not isEmbedded:             config["Processors"].extend(("producer:SimpleEleTauFakeRateWeightProducer",
                                                              "producer:SimpleMuTauFakeRateWeightProducer"))
  if isTTbar:                    config["Processors"].append( "producer:TopPtReweightingProducer")
  if isDY:                       config["Processors"].append( "producer:ZPtReweightProducer")
  config["Processors"].append(                                "filter:MinimalPlotlevelFilter") #"producer:MVATestMethodsProducer",
                                                              #"producer:MVAInputQuantitiesProducer"))
  if not isData:                 config["Processors"].append( #"producer:TriggerWeightProducer", "producer:IdentificationWeightProducer"
                                                              "producer:RooWorkspaceWeightProducer")
  if not isEmbedded:             config["Processors"].append( "producer:JetToTauFakesProducer")
  config["Processors"].append(                                "producer:EventWeightProducer")
  

  
  config["AddGenMatchedParticles"] = True
  config["AddGenMatchedTaus"] = True
  config["AddGenMatchedTauJets"] = True
  config["BranchGenMatchedElectrons"] = True
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
  return ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.syst_shifts_et").build_config(nickname))