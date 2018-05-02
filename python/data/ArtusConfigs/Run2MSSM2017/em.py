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
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJEC",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsBTaggedJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2Analysis.Includes.settingsMinimalPlotlevelFilter_em"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["Channel"] = "EM"
  config["MinNElectrons"] = 1
  config["MinNMuons"] = 1
  config["MaxNLooseElectrons"] = 1
  config["MaxNLooseMuons"] = 1
  # HltPaths_comment: The first path must be one with the higher pt cut on the electron. The second and last path must be one with the higher pt cut on the muon. Corresponding Pt cuts are implemented in the Run2DecayChannelProducer..
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

  config["ElectronLowerPtCuts"] = ["13.0"]
  config["ElectronUpperAbsEtaCuts"] = ["2.5"]
  config["MuonLowerPtCuts"] = ["13.0"]
  config["MuonUpperAbsEtaCuts"] = ["2.4"]
  config["DiTauPairMinDeltaRCut"] = 0.3
  config["DeltaRTriggerMatchingMuons"] = 0.3
  config["DeltaRTriggerMatchingElectrons"] = 0.3
  config["DiTauPairIsTauIsoMVA"] = True
  config["DiTauPairLepton1LowerPtCuts"] = [
          "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v:24.0"]
  config["DiTauPairLepton2LowerPtCuts"] = [
          "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:24.0"]
  config["DiTauPairNoHLT"] = False
  config["DiTauPairHLTLast"] = True
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
  
  if re.search("Summer1", nickname):
    config["TriggerEfficiencyData"] = [
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_Run2016_Electron_Ele12leg_eff.root",
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_Run2016_Electron_Ele23leg_eff.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_Run2016_Muon_Mu8leg_2016BtoH_eff.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_Run2016_Muon_Mu23leg_2016BtoH_eff.root"]
    config["TriggerEfficiencyMc"] = [
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_MC_Electron_Ele12leg_eff.root",
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_MC_Electron_Ele23leg_eff.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_MC_Muon_Mu8leg_2016BtoH_eff.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_MC_Muon_Mu23leg_2016BtoH_eff.root"]
    config["IdentificationEfficiencyData"] = [
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/identificationWeights/identificationEfficiency_Run2016_Electron_IdIso_IsoLt0p15_eff.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/identificationWeights/identificationEfficiency_Run2016_Muon_IdIso_IsoLt0p2_2016BtoH_eff.root"]
    config["IdentificationEfficiencyMc"] = [
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/identificationWeights/identificationEfficiency_MC_Electron_IdIso_IsoLt0p15_eff.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/identificationWeights/identificationEfficiency_MC_Muon_IdIso_IsoLt0p2_2016BtoH_eff.root"]
  elif re.search("Run201", nickname):
    config["TriggerEfficiencyData"] = [
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_dummy.root",
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_dummy.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_dummy.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_dummy.root"]
    config["TriggerEfficiencyMc"] = [
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_dummy.root",
      "0:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_dummy.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_dummy.root",
      "1:$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/triggerWeights/triggerEfficiency_dummy.root"]
  
  config["TriggerEfficiencyMode"] = "correlate_triggers"
  config["IdentificationEfficiencyMode"] = "multiply_weights"
  config["EventWeight"] = "eventWeight"
  config["TauTauRestFrameReco"] = "collinear_approximation"
  
  config["ElectronTriggerFilterNames"] = [
        "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu12TrkIsoVVLEle23CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter",
        "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu12TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter",
        "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter",
        "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLDZFilter"
      ]
  config["MuonTriggerFilterNames"] = [
        "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu12TrkIsoVVLEle23CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered12",
        "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu12TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter",
        "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered23",
        "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLDZFilter"
      ]
  
  config["BTagWPs"] = ["medium"]
  config["InvalidateNonMatchingElectrons"] = True
  config["InvalidateNonMatchingMuons"] = True
  config["InvalidateNonMatchingTaus"] = False
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True
  
  config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.syncQuantities").build_list()
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.weightQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.lheWeights").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.zptQuantities").build_list())
  config["Quantities"].extend([
      "had_gen_match_pT_1",
      "had_gen_match_pT_2"
  ])
  
  config["OSChargeLeptons"] = True
  config["TopPtReweightingStrategy"] = "Run2"
  
  config["Processors"] = [                                    "producer:HttValidLooseElectronsProducer",
                                                              "producer:HttValidLooseMuonsProducer",
                                                              "producer:HltProducer",
                                                              "producer:MetSelector",
                                                              "producer:ValidElectronsProducer",
                                                              "filter:ValidElectronsFilter",
                                                              "producer:ElectronTriggerMatchingProducer",
                                                              "filter:MinElectronsCountFilter",
                                                              "producer:ValidMuonsProducer",
                                                              "filter:ValidMuonsFilter",
                                                              "producer:MuonTriggerMatchingProducer",
                                                              "filter:MinMuonsCountFilter",
                                                              "producer:ValidTausProducer",
                                                              #"producer:ValidEMPairCandidatesProducer",
                                                              "producer:NewValidEMPairCandidatesProducer",
                                                              "filter:ValidDiTauPairCandidatesFilter",
                                                              "producer:Run2DecayChannelProducer",
  #                                                            "producer:TaggedJetCorrectionsProducer",
                                                              "producer:ValidTaggedJetsProducer",
                                                              "producer:ValidBTaggedJetsProducer"]
  #if not (isData or isEmbedded): config["Processors"].append( "producer:MetCorrector")
  config["Processors"].extend((                               "producer:TauTauRestFrameSelector",
                                                              "producer:DiLeptonQuantitiesProducer",
                                                              "producer:DiJetQuantitiesProducer"))
  if isTTbar:                    config["Processors"].append( "producer:TopPtReweightingProducer")
  #if isDY:                       config["Processors"].append( "producer:ZPtReweightProducer")
  #config["Processors"].append(                                "filter:MinimalPlotlevelFilter")
  #if not (isData or isEmbedded): config["Processors"].extend(("producer:TriggerWeightProducer",
  #                                                            "producer:IdentificationWeightProducer"))
  #if not isData:                 config["Processors"].append( "producer:RooWorkspaceWeightProducer")
  #config["Processors"].extend((                               "producer:EmuQcdWeightProducer",
  config["Processors"].append(
                                                              "producer:EventWeightProducer")#)
    
  config["AddGenMatchedParticles"] = True
  config["BranchGenMatchedElectrons"] = True
  config["BranchGenMatchedMuons"] = True
  config["Consumers"] = ["KappaLambdaNtupleConsumer",
                         "cutflow_histogram"]
  
  # pipelines - systematic shifts
  return ACU.apply_uncertainty_shift_configs('em', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.syst_shifts_nom").build_config(nickname))
