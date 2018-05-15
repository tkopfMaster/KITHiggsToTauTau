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
  isDY = re.search("DY.?JetsToLLM(10to50|50)", nickname)
  isWjets = re.search("W.?JetsToLNu", nickname)
  isSignal = re.search("HToTauTau",nickname)
  
  
  ## fill config:
  # includes
  includes = [
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsVetoElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJEC",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsBTaggedJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauES",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMinimalPlotlevelFilter_et"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["Channel"] = "ET"
  config["MinNElectrons"] = 1
  config["MinNTaus"] = 1
  # HltPaths_comment: The first path must be the single lepton trigger. A corresponding Pt cut is implemented in the Run2DecayChannelProducer..
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
  config["ElectronLowerPtCuts"] = ["10.0"]
  config["ElectronUpperAbsEtaCuts"] = ["2.1"]
  config["TauLowerPtCuts"] = ["20.0"]
  config["TauUpperAbsEtaCuts"] = ["2.3"]
  config["DiTauPairMinDeltaRCut"] = 0.5
  config["DeltaRTriggerMatchingTaus"] = 0.5
  config["DeltaRTriggerMatchingElectrons"] = 0.5
  config["DiTauPairIsTauIsoMVA"] = True
  config["DiTauPairLepton1LowerPtCuts"] = [
          "HLT_Ele32_WPTight_Gsf_v:34.0",
          "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v:26.0",
          "HLT_Ele35_WPTight_Gsf_v:37.0",
  ]
  config["DiTauPairLepton2LowerPtCuts"] = [
          "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v:33.0",
  ]
  config["DiTauPairLepton2UpperEtaCuts"] = [
          "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v:2.1",
          "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v:2.1",
  ]
  config["CheckLepton1TriggerMatch"] = [
      "trg_singlemuon_lowpt",
      "trg_singlemuon",
      "trg_singletau_leading",
      "trg_singleelectron_lowpt",
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
  config["DiTauPairNoHLT"] = False
  config["DiTauPairHLTLast"] = True
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
      "1:crossTriggerMCEfficiencyWeight",
      "1:crossTriggerDataEfficiencyWeight",
  ]
  config["RooWorkspace"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/htt_scalefactors_v17_1.root"
  config["RooWorkspaceWeightNames"] = [
      "0:crossTriggerMCEfficiencyWeight",
      "0:crossTriggerDataEfficiencyWeight",
      "0:singleTriggerMCEfficiencyWeight",
      "0:singleTriggerDataEfficiencyWeight",
  ]
  config["RooWorkspaceObjectNames"] = [
      "0:e_trg_EleTau_Ele24Leg_desy_mc",
      "0:e_trg_EleTau_Ele24Leg_desy_data",
      "0:e_trg_SingleEle_Ele32OREle35_desy_mc",
      "0:e_trg_SingleEle_Ele32OREle35_desy_data",
  ]
  config["RooWorkspaceObjectArguments"] = [
      "0:e_pt,e_eta",
      "0:e_pt,e_eta",
      "0:e_pt,e_eta",
      "0:e_pt,e_eta",
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
  config["ElectronTriggerFilterNames"] = [
          "HLT_Ele32_WPTight_Gsf_v:hltEle32WPTightGsfTrackIsoFilter",
          "HLT_Ele35_WPTight_Gsf_v:hltEle35noerWPTightGsfTrackIsoFilter",
          "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v:hltEle24erWPTightGsfTrackIsoFilterForTau",
          "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v:hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30"
    ]
  config["TauTriggerFilterNames"] = [
          "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v:hltSelectedPFTau30LooseChargedIsolationL1HLTMatched",
          "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v:hltOverlapFilterIsoEle24WPTightGsfLooseIsoPFTau30",
          "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v:hltPFTau180TrackPt50LooseAbsOrRelMediumHighPtRelaxedIsoIso",
          "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v:hltSelectedPFTau180MediumChargedIsolationL1HLTMatched"
    ]
  config["BTagWPs"] = ["medium"]
  config["InvalidateNonMatchingElectrons"] = True
  config["InvalidateNonMatchingMuons"] = False
  config["InvalidateNonMatchingTaus"] = True
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True
  
  config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.syncQuantities").build_list()
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.weightQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.zptQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.lheWeights").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.fakeFactorWeightQuantities").build_list())
  config["Quantities"].extend([
      "had_gen_match_pT_1",
      "had_gen_match_pT_2"
  ])
  
  config["OSChargeLeptons"] = True
  config["TopPtReweightingStrategy"] = "Run2"
  
  config["Processors"] =                                     []# if (isData or isEmbedded) else ["producer:ElectronCorrectionsProducer"]
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
  #if not isData:                 config["Processors"].append( "producer:TauCorrectionsProducer")
  config["Processors"].extend((                               "producer:ValidTausProducer",
                                                              "filter:ValidTausFilter",
                                                              "producer:TauTriggerMatchingProducer",
                                                              "filter:MinTausCountFilter",
                                                              "producer:NewValidETPairCandidatesProducer",
                                                              #"producer:ValidETPairCandidatesProducer",
                                                              "filter:ValidDiTauPairCandidatesFilter",
                                                              "producer:Run2DecayChannelProducer",
                                                              "producer:DiVetoElectronVetoProducer",
  #                                                            "producer:TaggedJetCorrectionsProducer",
                                                              "producer:ValidTaggedJetsProducer",
                                                              "producer:ValidBTaggedJetsProducer"))
  #if not (isData or isEmbedded): config["Processors"].append( "producer:MetCorrector")
  config["Processors"].extend((                               "producer:TauTauRestFrameSelector",
                                                              "producer:DiLeptonQuantitiesProducer",
                                                              "producer:DiJetQuantitiesProducer"))
  if not isEmbedded:             config["Processors"].extend(("producer:SimpleEleTauFakeRateWeightProducer",
                                                              "producer:SimpleMuTauFakeRateWeightProducer"))
  if isTTbar:                    config["Processors"].append( "producer:TopPtReweightingProducer")
  #if isDY:                       config["Processors"].append( "producer:ZPtReweightProducer")
  #config["Processors"].append(                                "filter:MinimalPlotlevelFilter")
  if not isData:                 config["Processors"].append( "producer:RooWorkspaceWeightProducer")
  if not isData:                 config["Processors"].append( "producer:TauTrigger2017EfficiencyProducer")
  #if not isEmbedded:             config["Processors"].append( "producer:JetToTauFakesProducer")
  config["Processors"].append(                                "producer:EventWeightProducer")
  
  config["AddGenMatchedParticles"] = True
  config["AddGenMatchedTaus"] = True
  config["AddGenMatchedTauJets"] = True
  config["BranchGenMatchedElectrons"] = True
  config["BranchGenMatchedTaus"] = True
  config["Consumers"] = ["KappaLambdaNtupleConsumer",
                         "cutflow_histogram"]
  
  # pipelines - systematic shifts
  return ACU.apply_uncertainty_shift_configs('et', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.syst_shifts_nom").build_config(nickname))
