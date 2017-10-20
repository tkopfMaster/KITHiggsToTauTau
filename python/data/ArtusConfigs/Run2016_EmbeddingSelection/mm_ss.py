#!usr/bin/env python
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
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsLooseElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsLooseMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsElectronID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsVetoMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsMuonID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsTauID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsJEC",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsBTaggedJetID",
    "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.settingsTauES",
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
      "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
      "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ"
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
  config["MuonUpperAbsEtaCuts"] = ["2.5"]
  config["LowerZMassCut"] = 20.0
  config["ZMassRange"] = 13000.0
  config["VetoMultipleZs"] = False
  config["InvalidateNonZLeptons"] = True
  config["RequireOSZBoson"] = False
  config["DiTauPairMinDeltaRCut"] = 0.0 
  config["DiTauPairIsTauIsoMVA"] = True
  config["DiTauPairHltPathsWithoutCommonMatchRequired"] = [
      ]
  config["DiTauPairHLTLast"] = True
  config["HLTBranchNames"] = [
      "trg_doublemuon:HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
      "trg_doublemuon:HLT_Mu17_TrkIsoVVL_TrkMu8_TrkIsoVVL_DZ"
    ]
  config["DiTauPairLepton1LowerPtCuts"] = [
      "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v:19",
      "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v:19"
    ]
  config["EventWeight"] = "eventWeight"
  config["TauTauRestFrameReco"] = "collinear_approximation"
  if re.search("(Run2016|Embedding2016|Summer16)", nickname): config["MuonTriggerFilterNames"] = [
      "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v:hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4DzFiltered0p2",
      "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v:hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4DzFiltered0p2"
          ]
  config["BTagWPs"] = ["medium"]
  config["InvalidateNonMatchingElectrons"] = False
  config["InvalidateNonMatchingMuons"] = True
  config["InvalidateNonMatchingTaus"] = False
  config["InvalidateNonMatchingJets"] = False
  config["DirectIso"] = True
  
  config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.syncQuantities").build_list()
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.weightQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.zptQuantities").build_list())
  config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.Includes.lheWeights").build_list())
  config["Quantities"].extend([
      "had_gen_match_pT_1",
      "had_gen_match_pT_2",
      "ZMass"
  ])
  
  config["OSChargeLeptons"] = True
  config["TopPtReweightingStrategy"] = "Run1"
  config["MuonEnergyCorrection"] = "rochcorr2016"
  config["MuonRochesterCorrectionsFile"] = "$CMSSW_BASE/src/Artus/KappaAnalysis/data/rochcorr2016"
  
  config["Processors"] =                                     ["producer:MuonCorrectionsProducer"]
  config["Processors"] = [                                    "producer:HltProducer",
                                                              "producer:MetSelector",
                                                              "producer:HttValidLooseElectronsProducer",
                                                              "producer:HttValidLooseMuonsProducer",
                                                              "producer:ValidMuonsProducer",
                                                              "filter:ValidMuonsFilter",
                                                              "producer:MuonTriggerMatchingProducer",
                                                              "filter:MinMuonsCountFilter",
                                                              "producer:ZmmProducer",
                                                              "filter:ZFilter",
                                                              "producer:HttValidVetoMuonsProducer",
                                                              "producer:ValidElectronsProducer"]
  if isDY or isWjets or isHtt:   config["Processors"].append( "producer:TauCorrectionsProducer")
  config["Processors"].extend((                               "producer:ValidTausProducer",
                                                              "producer:TauTriggerMatchingProducer",
                                                              "producer:ValidMMPairCandidatesProducer",
                                                              "filter:ValidDiTauPairCandidatesFilter",
                                                              "producer:Run2DecayChannelProducer",
                                                              "producer:DiVetoMuonVetoProducer",
                                                              "producer:TaggedJetCorrectionsProducer",
                                                              "producer:ValidTaggedJetsProducer",
                                                              "producer:ValidBTaggedJetsProducer"))
  if isDY or isWjets or isHtt:   config["Processors"].append( "producer:MetCorrector") 
  config["Processors"].extend((                               "producer:TauTauRestFrameSelector",
                                                              "producer:DiLeptonQuantitiesProducer",
                                                              "producer:DiJetQuantitiesProducer"))
  if isTTbar:                    config["Processors"].append( "producer:TopPtReweightingProducer")
  if isDY:                       config["Processors"].append( "producer:ZPtReweightProducer")
  if not isData:                 config["Processors"].append(
                                                              "producer:RooWorkspaceWeightProducer")
  config["Processors"].append(                                "producer:EventWeightProducer")
  
    
  
  config["AddGenMatchedParticles"] = True
  config["AddGenMatchedTaus"] = True
  config["AddGenMatchedTauJets"] = True
  config["BranchGenMatchedMuons"] = True
  config["BranchGenMatchedTaus"] = True
  config["Consumers"] = ["KappaLambdaNtupleConsumer",
                         "cutflow_histogram"]
  
  # pipelines - systematic shifts
  return ACU.apply_uncertainty_shift_configs('mm_ss', config, importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2016_EmbeddingSelection.syst_shifts_nom").build_config(nickname))
