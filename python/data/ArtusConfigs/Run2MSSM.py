#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

def build_config(nickname, process=None):
  config = jsonTools.JsonDict()
  datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz("Kappa/Skimming/data/datasets.json")
  
  # define frequently used conditions
  isData = datasetsHelper.isData(nickname)
  isEmbedding = datasetsHelper.isEmbedding(nickname)
  isTTbar = re.match("TT(To|_|Jets)", nickname)
  isDY = re.match("DY.?JetsToLLM(50|150)", nickname)
  isWjets = re.match("W.?JetsToLNu", nickname)
  
  ## fill config:
  # includes
  includes = [
    ]
  for include_file in includes:
    analysis_config_module = importlib.import_module(include_file)
    config += analysis_config_module.build_config(nickname)
  
  
  config["SkipEvents"] = 0
  config["EventCount"] = -1
  config["InputIsData"] = isData
  
  BosonPdgIds = {
      "default" : [
        0
      ],
      "DY.?JetsToLL|EWKZ2Jets|Embedding(2016|MC)" : [
        23
      ],
      "^(GluGlu|GluGluTo|VBF|Wminus|Wplus|Z)(HToTauTau|H2JetsToTauTau)" : [
        25
      ],
      "W.?JetsToLN|EWKW" : [
        24
      ],
      "SUSY(BB|GluGlu|GluGluTo)(BB)?HToTauTau" : [
        25,
        35,
        36
        ]
    }
  }
  config["BosonPdgIds"] = 0
  for key, pdgids in BosonPdgIds.items():
    if re.match(key, nickname): config["BosonPdgIds"] = pdgids
  
  config["BosonStatuses"] = 62
  config["ChooseMvaMet"] = False
  config["DeltaRMatchingRecoElectronGenParticle"] = 0.2
  config["DeltaRMatchingRecoElectronGenTau"] = 0.2
  config["DeltaRMatchingRecoMuonGenParticle"] = 0.2
  config["DeltaRMatchingRecoMuonGenTau"] = 0.2
  config["DeltaRMatchingRecoTauGenParticle"] = 0.2
  config["DeltaRMatchingRecoTauGenTau"] = 0.2
  config["RecoElectronMatchingGenParticlePdgIds"] = [11,13]
  config["RecoMuonMatchingGenParticlePdgIds"] = [11,13]
  config["RecoTauMatchingGenParticlePdgIds"] = [11,13]
  config["RecoElectronMatchingGenParticleMatchAllElectrons"] = "true"
  config["RecoMuonMatchingGenParticleMatchAllMuons"] = "true"
  config["RecoTauMatchingGenParticleMatchAllTaus"] = "true"
  config["MatchAllElectronsGenTau"] = "true"
  config["MatchAllMuonsGenTau"] = "true"
  config["MatchAllTausGenTau"] = "true"
  config["UpdateMetWithCorrectedLeptons"] = "true"
  
  config["MetFilter"] : [
        "Flag_HBHENoiseFilter",
        "Flag_HBHENoiseIsoFilter",
        "Flag_EcalDeadCellTriggerPrimitiveFilter",
        "Flag_goodVertices",
        "Flag_globalTightHalo2016Filter",
        "Flag_BadPFMuonFilter",
        "Flag_BadChargedCandidateFilter"
  ]
  if isData:
    config["MetFilter"].extend((
        "Flag_eeBadScFilter",
        "!Flag_duplicateMuons",
        "!Flag_badMuons"
    ))
  else:
    config["MetFilter"].extend((
        "!Flag_badGlobalMuonTaggerMAOD",
        "!Flag_cloneGlobalMuonTaggerMAOD"
    ))
  
  config["OutputPath"] = "output.root"
  
  config["Processors"] = []
  #config["Processors"].append("filter:RunLumiEventFilter")
  if not isEmbedding:                  config["Processors"].append( "filter:MetFilter")
  if isData or isEmbedding:            config["Processors"].append( "filter:JsonFilter")
  if isDY or isTTbar:                  config["Processors"].append( "producer:ScaleVariationProducer")
  config["Processors"].append(                                      "producer:NicknameProducer")
  if not isData:
    config["Processors"].extend((                                   "producer:CrossSectionWeightProducer",
                                                                    "producer:NumberGeneratedEventsWeightProducer"))
    if not isEmbedding:                config["Processors"].append( "producer:PUWeightProducer")
    if isWjets or isDY:                config["Processors"].append( "producer:GenBosonFromGenParticlesProducer")
    if isDY or isEmbedding:            config["Processors"].append( "producer:GenDiLeptonDecayModeProducer")
    config["Processors"].extend((                                   "producer:GenParticleProducer",
                                                                    "producer:GenPartonCounterProducer"))
    if isWjets or isDY or isEmbedding: config["Processors"].extend(("producer:GenTauDecayProducer",
                                                                    "producer:GenBosonDiLeptonDecayModeProducer"))
    config["Processors"].extend((                                   "producer:GeneratorWeightProducer",
                                                                    "producer:RecoMuonGenParticleMatchingProducer",
                                                                    "producer:RecoMuonGenTauMatchingProducer",
                                                                    "producer:RecoElectronGenParticleMatchingProducer",
                                                                    "producer:RecoElectronGenTauMatchingProducer",
                                                                    "producer:RecoTauGenParticleMatchingProducer",
                                                                    "producer:RecoTauGenTauMatchingProducer",
                                                                    "producer:MatchedLeptonsProducer"))
    if isTTbar:                        config["Processors"].append( "producer:TTbarGenDecayModeProducer")

  if isData or isEmbedding:            config["PileupWeightFile"] = "not needed"
  elif re.match("Spring16", nickname): config["PileupWeightFile"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/pileup/Data_Pileup_2016_271036-276811_13TeVSpring16_PromptReco_69p2mbMinBiasXS.root"
  elif re.match("Summer16", nickname): config["PileupWeightFile"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/pileup/Data_Pileup_2016_271036-284044_13TeVMoriond17_23Sep2016ReReco_69p2mbMinBiasXS.root"
  else:                                config["PileupWeightFile"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/pileup/Data_Pileup_2015_246908-260627_13TeVFall15MiniAODv2_PromptReco_69mbMinBiasXS.root"

  config["ZptReweightProducerWeights"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/zpt/zpt_weights_2016_BtoH_MSSM_v2.root"
  config["MetRecoilCorrectorFile"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/recoilMet/TypeI-PFMet_Run2016BtoH.root"
  config["MetShiftCorrectorFile"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/recoilMet/PFMEtSys_2016.root"
  config["MvaMetRecoilCorrectorFile"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/recoilMet/MvaMET_2016BCD.root"
  config["MetCorrectionMethod"] = "meanResolution"
  config["BTagScaleFactorFile"] = "$CMSSW_BASE/src/Artus/KappaAnalysis/data/CSVv2_moriond17_BtoH.csv"
  config["BTagEfficiencyFile"] = "$CMSSW_BASE/src/Artus/KappaAnalysis/data/tagging_efficiencies_moriond2017.root"
  
  if isData or isEmbedding:
    if   re.match("Run2016|Embedding2016", nickname):      config["JsonFiles"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
    elif re.match("Run2015(C|D)|Embedding2015", nickname): config["JsonFiles"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/json/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt"
    elif re.match("Run2015B", nickname):                   config["JsonFiles"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/json/Cert_13TeV_16Dec2015ReReco_Collisions15_50ns_JSON_v2.txt"
    
  if re.match("Fall15MiniAODv2", nickname):
    config["SimpleMuTauFakeRateWeightLoose"] = [1.0, 1.0, 1.0, 1.0, 1.0]
    config["SimpleMuTauFakeRateWeightTight"] = [1.0, 1.0, 1.0, 1.0, 1.0]
    config["SimpleEleTauFakeRateWeightVLoose"] = [1.02, 1.11]
    config["SimpleEleTauFakeRateWeightTight"] = [1.80, 1.30]
  else:
    config["SimpleMuTauFakeRateWeightLoose"] = [1.22, 1.12, 1.26, 1.22, 2.39]
    config["SimpleMuTauFakeRateWeightTight"] = [1.47, 1.55, 1.33, 1.72, 2.50]
    config["SimpleEleTauFakeRateWeightVLoose"] = [1.21, 1.38]
    config["SimpleEleTauFakeRateWeightTight"] = [1.40, 1.90]


  # pipelines
  config["Pipelines"] = {}
  if not isData:
    print "nothing yet"
  
  return config