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
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsVetoMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsTauID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsJEC",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsBTaggedJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.settingsTauES",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2Analysis.Includes.settingsMinimalPlotlevelFilter_mm"
  ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  # explicit configuration
  config["Channel"] = "MM"
  config["MinNMuons"] = 2
  # HltPaths_comment: The first path must be the single lepton trigger. A corresponding Pt cut is implemented in the Run2DecayChannelProducer.
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
  
  config["RooWorkspace"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/htt_scalefactors_v16_5.root"
  config["RooWorkspaceWeightNames"] = [
      "0:triggerWeight",
      "0:isoweight",
      "0:idweight",
      "0:trackWeight",
      "1:isoweight",
      "1:idweight",
      "1:trackWeight"
  ]
  config["RooWorkspaceObjectNames"] = [
      "0:m_trgOR4_binned_ratio",
      "0:m_iso_binned_ratio",
      "0:m_id_ratio",
      "0:m_trk_ratio",
      "1:m_iso_binned_ratio",
      "1:m_id_ratio",
      "1:m_trk_ratio"
  ]
  config["RooWorkspaceObjectArguments"] = [
      "0:m_pt,m_eta,m_iso",
      "0:m_pt,m_eta,m_iso",
      "0:m_pt,m_eta",
      "0:m_eta",
      "1:m_pt,m_eta,m_iso",
      "1:m_pt,m_eta",
      "1:m_eta"
  ]
  config["TauID"] = "TauIDRecommendation13TeV"
  config["TauUseOldDMs"] = True
  config["MuonLowerPtCuts"] = ["10.0"]
  config["MuonUpperAbsEtaCuts"] = ["2.1"]
  config["DiTauPairMinDeltaRCut"] = 0.3
  config["DiTauPairIsTauIsoMVA"] = True
  config["DiTauPairHltPathsWithoutCommonMatchRequired"] = [
      "HLT_IsoMu22_v",
      "HLT_IsoTkMu22_v",
      "HLT_IsoMu22_eta2p1_v",
      "HLT_IsoTkMu22_eta2p1_v",
      "HLT_VLooseIsoPFTau120_Trk50_eta2p1_v",
      "HLT_Ele25_eta2p1_WPTight_Gsf_v"]
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
      "trg_muonelectron:HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"]
  config["DiTauPairLepton1LowerPtCuts"] = [
      "HLT_IsoMu22_v:23.0",
      "HLT_IsoTkMu22_v:23.0",
      "HLT_IsoMu22_eta2p1_v:23.0",
      "HLT_IsoTkMu22_eta2p1_v:23.0"
    ]
  config["EventWeight"] = "eventWeight"
  config["TauTauRestFrameReco"] = "collinear_approximation"
  if re.search("(Run2016|Embedding2016|Summer16)", nickname): config["MuonTriggerFilterNames"] = [
          "HLT_IsoMu22_v:hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09",
          "HLT_IsoTkMu22_v:hltL3fL1sMu20L1f0Tkf22QL3trkIsoFiltered0p09",
          "HLT_IsoMu22_eta2p1_v:hltL3crIsoL1sSingleMu20erL1f0L2f10QL3f22QL3trkIsoFiltered0p09",
          "HLT_IsoTkMu22_eta2p1_v:hltL3fL1sMu20erL1f0Tkf22QL3trkIsoFiltered0p09",
          "HLT_VLooseIsoPFTau120_Trk50_eta2p1_v:hltPFTau120TrackPt50LooseAbsOrRelVLooseIso"]
  config["BTagWPs"] = ["medium"]
  config["InvalidateNonMatchingElectrons"] = False
  config["InvalidateNonMatchingMuons"] = True
  config["InvalidateNonMatchingTaus"] = False
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True
  
  config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.syncQuantities").build_list()
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.weightQuantities").build_list())
  #config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.MVAInputQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.zptQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.Includes.lheWeights").build_list())
  config["Quantities"].extend([
      "had_gen_match_pT_1",
      "had_gen_match_pT_2"
  ])
  
  config["OSChargeLeptons"] = True
  config["TopPtReweightingStrategy"] = "Run1"
  if re.search("(Fall15MiniAODv2|Run2015)", nickname):
    config["MuonEnergyCorrection"] = "rochcorr2015"
    config["MuonRochesterCorrectionsFile"] = "$CMSSW_BASE/src/Artus/KappaAnalysis/data/rochcorr/RoccoR_13tev_2015.txt"
  else:
    config["MuonEnergyCorrection"] = "rochcorr2016"
    config["MuonRochesterCorrectionsFile"] = "$CMSSW_BASE/src/Artus/KappaAnalysis/data/rochcorr2016"
  
  #config["Processors"] =                                     ["producer:MuonCorrectionsProducer"]
  config["Processors"] = [                                    "producer:HltProducer",
                                                              "producer:MetSelector",
                                                              "producer:HttValidLooseElectronsProducer",
                                                              "producer:HttValidLooseMuonsProducer",
                                                              "producer:ValidMuonsProducer",
                                                              "filter:ValidMuonsFilter",
                                                              "producer:MuonTriggerMatchingProducer",
                                                              "filter:MinMuonsCountFilter",
                                                              "producer:HttValidVetoMuonsProducer",
                                                              "producer:ValidElectronsProducer"]
  if isDY or isWjets:            config["Processors"].append( "producer:TauCorrectionsProducer")
  config["Processors"].extend((                               "producer:ValidTausProducer",
                                                              "producer:TauTriggerMatchingProducer",
                                                              "producer:ValidMMPairCandidatesProducer",
                                                              "filter:ValidDiTauPairCandidatesFilter",
                                                              "producer:Run2DecayChannelProducer",#"producer:MvaMetSelector",
                                                              "producer:DiVetoMuonVetoProducer",
                                                              "producer:TaggedJetCorrectionsProducer",
                                                              "producer:ValidTaggedJetsProducer",
                                                              "producer:ValidBTaggedJetsProducer"))
  if isDY or isWjets:            config["Processors"].append( "producer:MetCorrector") #"producer:MvaMetCorrector"
  config["Processors"].extend((                               "producer:TauTauRestFrameSelector",
                                                              "producer:DiLeptonQuantitiesProducer",
                                                              "producer:DiJetQuantitiesProducer"))
  if isTTbar:                    config["Processors"].append( "producer:TopPtReweightingProducer")
  if isDY:                       config["Processors"].append( "producer:ZPtReweightProducer")
  config["Processors"].append(                                "filter:MinimalPlotlevelFilter") #"producer:MVATestMethodsProducer",
                                                              #"producer:MVAInputQuantitiesProducer"))
  if not isData:                 config["Processors"].append( #"producer:TriggerWeightProducer", "producer:IdentificationWeightProducer"
                                                              "producer:RooWorkspaceWeightProducer")
  config["Processors"].append(                                "producer:EventWeightProducer")
  
    
  
  config["AddGenMatchedParticles"] = True
  config["AddGenMatchedTaus"] = True
  config["AddGenMatchedTauJets"] = True
  config["BranchGenMatchedMuons"] = True
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
  systs = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.syst_shifts_nom").build_config(nickname)
  config_with_systs = jsonTools.JsonDict()
  for key, syst in systs.items():
    longkey = "mm_" + key
    config_with_systs[longkey] = jsonTools.JsonDict(syst)
    config_with_systs[longkey] += config
  return config_with_systs