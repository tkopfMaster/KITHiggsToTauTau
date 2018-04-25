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
  isSignal = re.search("HToTauTau",nickname)
  
  
  ## fill config:
  # includes
  includes = [
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJEC",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsBTaggedJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauES",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMinimalPlotlevelFilter_tt"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["Channel"] = "TT"
  config["MinNTaus"] = 2
  if re.search("(Run201|Embedding201|Summer1|Fall1)", nickname): config["HltPaths"] = [
          "HLT_IsoMu24",
          "HLT_IsoMu27",
          "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
          "HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau20_SingleL1",
          "HLT_Ele32_WPTight_Gsf",
          "HLT_Ele35_WPTight_Gsf",
          "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
          "HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg",
          "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
          "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
          "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
          "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
          "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
          "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"
    ]
  
  config["TauID"] = "TauIDRecommendation13TeV"
  config["TauUseOldDMs"] = True
  config["TauLowerPtCuts"] = ["20.0"]
  config["TauUpperAbsEtaCuts"] = ["2.1"]
  config["DiTauPairMinDeltaRCut"] = 0.5
  config["DeltaRTriggerMatchingTaus"] = 0.5
  config["DiTauPairIsTauIsoMVA"] = True
  config["DiTauPairLepton1LowerPtCuts"] = [
          "HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v:38.0",
          "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v:38.0",
          "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v:43.0",
          "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v:43.0"
  ]
  config["DiTauPairLepton2LowerPtCuts"] = [
          "HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v:38.0",
          "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v:38.0",
          "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v:43.0",
          "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v:43.0"
  ]
  config["DiTauPairHLTLast"] = True
  config["CheckL1MatchForDiTauPairLepton1"] = True
  config["CheckL1MatchForDiTauPairLepton2"] = True
  config["CheckLepton1TriggerMatch"] = [
      "trg_singlemuon_lowpt",
      "trg_singlemuon",
      "trg_singletau_leading",
      "trg_singleelectron_lowpt",
      "trg_singleelectron_lowpt_fallback",
      "trg_singleelectron",

      "trg_muontau_lowptmu",
      "trg_muontau_lowpttau",
      "trg_electrontau",
      "trg_doubletau_lowpt_mediso",
      "trg_doubletau_lowpt",
      "trg_doubletau_mediso",
      "trg_doubletau",
      "trg_muonelectron_lowptmu",
      "trg_muonelectron_lowpte"
  ]
  config["CheckLepton2TriggerMatch"] = [
      "trg_singletau_trailing",

      "trg_muontau_lowptmu",
      "trg_muontau_lowpttau",
      "trg_electrontau",
      "trg_doubletau_lowpt_mediso",
      "trg_doubletau_lowpt",
      "trg_doubletau_mediso",
      "trg_doubletau",
      "trg_muonelectron_lowptmu",
      "trg_muonelectron_lowpte"
  ]
  config["HLTBranchNames"] = [
      "trg_singlemuon_lowpt:HLT_IsoMu24_v",
      "trg_singlemuon:HLT_IsoMu27_v",
      "trg_muontau_lowptmu:HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v",
      "trg_muontau_lowpttau:HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau20_SingleL1_v",
      "trg_singleelectron_lowpt:HLT_Ele32_WPTight_Gsf_v",
      "trg_singleelectron:HLT_Ele35_WPTight_Gsf_v",
      "trg_electrontau:HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v",
      "trg_doubletau_lowpt_mediso:HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v",
      "trg_doubletau_lowpt:HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v",
      "trg_doubletau_mediso:HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v",
      "trg_doubletau:HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v",
      "trg_singletau_leading:HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v",
      "trg_singletau_trailing:HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v",
      "trg_muonelectron_lowptmu:HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v",
      "trg_muonelectron_lowpte:HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v"
  ]
  config["DiTauPairHltPathsWithoutCommonMatchRequired"] = [
      "HLT_IsoMu24_v",
      "HLT_IsoMu27_v",
      "HLT_Ele32_WPTight_Gsf_v",
      "HLT_Ele35_WPTight_Gsf_v",
      "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v"
  ]
  config["UsingOnlyFirstLeptonPerHLTBranchNames"] = [
      "trg_singletau_leading:1",
      "trg_singletau_trailing:0",
  ]
  config["TauTrigger2017Input"] = "$CMSSW_BASE/src/TauTriggerSFs2017/TauTriggerSFs2017/data/tauTriggerEfficiencies2017.root"
  config["TauTrigger2017WorkingPoint"] = "tight"
  config["TauTrigger2017EfficiencyWeightNames"] = [
      "0:crossTriggerMCEfficiencyWeight",
      "0:crossTriggerDataEfficiencyWeight",
      "1:crossTriggerMCEfficiencyWeight",
      "1:crossTriggerDataEfficiencyWeight",
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
          "HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v:hltDoublePFTau35TrackPt1MediumChargedIsolationDz02Reg",
          "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v:hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg",
          "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v:hltDoublePFTau40TrackPt1MediumChargedIsolationAndTightOOSCPhotonsDz02Reg",
          "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v:hltDoublePFTau40TrackPt1TightChargedIsolationDz02Reg",
          "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v:hltPFTau180TrackPt50LooseAbsOrRelMediumHighPtRelaxedIsoIso",
          "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v:hltSelectedPFTau180MediumChargedIsolationL1HLTMatched"
    ]
  config["TauTriggerCheckL1Match"] = [
          "HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v",
          "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v",
          "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v",
          "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v"
    ]
  config["BTagWPs"] = ["medium"]
  config["InvalidateNonMatchingElectrons"] = False
  config["InvalidateNonMatchingMuons"] = False
  config["InvalidateNonMatchingTaus"] = True
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True
  
  config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.syncQuantities").build_list()
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.weightQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.lheWeights").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.zptQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.fakeFactorWeightQuantities_tt").build_list())
  config["Quantities"].extend([
      "had_gen_match_pT_1",
      "had_gen_match_pT_2"
  ])
  
  config["OSChargeLeptons"] = True
  config["TopPtReweightingStrategy"] = "Run2"
  
  config["Processors"] =                                     ["producer:HttValidLooseElectronsProducer",
                                                              "producer:HttValidLooseMuonsProducer",
                                                              "producer:HltProducer",
                                                              "producer:MetSelector"]
  #if not isData:                 config["Processors"].append( "producer:TauCorrectionsProducer")
  config["Processors"].extend((                               "producer:ValidTausProducer",
                                                              "filter:ValidTausFilter",
                                                              "producer:TauTriggerMatchingProducer",
                                                              "filter:MinTausCountFilter",
                                                              "producer:ValidElectronsProducer",
                                                              "producer:ValidMuonsProducer",
                                                              #"producer:ValidTTPairCandidatesProducer",
                                                              "producer:NewValidTTPairCandidatesProducer",
                                                              "filter:ValidDiTauPairCandidatesFilter",
                                                              "producer:Run2DecayChannelProducer",
  #                                                            "producer:TaggedJetCorrectionsProducer",
                                                              "producer:ValidTaggedJetsProducer",
                                                              "producer:ValidBTaggedJetsProducer"))
  #if not isData:                 config["Processors"].extend((#"producer:MetCorrector",
  #                                                            "producer:SimpleEleTauFakeRateWeightProducer",
  #                                                            "producer:SimpleMuTauFakeRateWeightProducer",
  #                                                            "producer:TauTauTriggerWeightProducer"))
  if isTTbar:                    config["Processors"].append( "producer:TopPtReweightingProducer")
  #if isDY or isEmbedded:        config["Processors"].append( "producer:ZPtReweightProducer")
  config["Processors"].extend((                               #"filter:MinimalPlotlevelFilter",
                                                              "producer:TauTauRestFrameSelector",
                                                              "producer:DiLeptonQuantitiesProducer",
                                                              "producer:DiJetQuantitiesProducer"))#,
                                                              # "producer:JetToTauFakesProducer"))
  if not isData:                 config["Processors"].append( "producer:TauTrigger2017EfficiencyProducer")
  config["Processors"].append(                                "producer:EventWeightProducer")

  config["AddGenMatchedTaus"] = True
  config["AddGenMatchedTauJets"] = True
  config["BranchGenMatchedTaus"] = True
  config["Consumers"] = ["KappaLambdaNtupleConsumer",
                         "cutflow_histogram"]
  
  # pipelines - systematic shifts
  return ACU.apply_uncertainty_shift_configs('tt', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.syst_shifts_nom").build_config(nickname))
