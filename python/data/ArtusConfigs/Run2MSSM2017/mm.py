#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import copy
import re
import importlib
import os

import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz
import HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.ArtusConfigUtility as ACU


def build_config(nickname, **kwargs):
    btag_eff = True if "sub_analysis" in kwargs and kwargs["sub_analysis"] == "btag-eff" else False

    config = jsonTools.JsonDict()
    datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))

    # define frequently used conditions
    isEmbedded = datasetsHelper.isEmbedded(nickname)
    isData = datasetsHelper.isData(nickname) and (not isEmbedded)
    isTTbar = re.search("TT(To|_|Jets)", nickname)
    isDY = re.search("DY.?JetsToLLM(10to50|50)", nickname)
    isWjets = re.search("W.?JetsToLNu", nickname)
    isSignal = re.search("HToTauTau", nickname)

    # fill config:
    # includes
    includes = [
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseElectronID",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsLooseMuonID",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsElectronID",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsVetoMuonID",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMuonID",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauID",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJEC",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsSvfit",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsJetID",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsBTaggedJetID",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsTauES",
        "HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.settingsMinimalPlotlevelFilter_mm"
    ]

    for include_file in includes:
        analysis_config_module = importlib.import_module(include_file)
        config += analysis_config_module.build_config(nickname)

    # explicit configuration
    config["Channel"] = "MM"
    config["MinNMuons"] = 2

    # HLT
    # HltPaths_comment: The first path must be the single lepton trigger.
    # A corresponding Pt cut is implemented in the Run2DecayChannelProducer.
    if re.search("(Run201|Embedding201|Summer1|Fall1)", nickname):
        config["HltPaths"] = [
            # triggers from mt
            "HLT_IsoMu24",
            "HLT_IsoMu27",
            "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
            "HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1",
            # triggers from et
            "HLT_Ele27_WPTight_Gsf",
            "HLT_Ele32_WPTight_Gsf",
            "HLT_Ele32_WPTight_Gsf_DoubleL1EG",
            "HLT_Ele35_WPTight_Gsf",
            "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
            # triggers from tt
            "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
            "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
            "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
            # triggers from em
            "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
            "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
            "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"
        ]

    # RooWorksapce for Trigger&ID SFs of lepton in the final state
    # https://github.com/CMS-HTT/CorrectionsWorkspace
    config["RooWorkspace"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/root/scaleFactorWeights/htt_scalefactors_v17_1.root"
    config["RooWorkspaceWeightNames"] = [
        "0:crossTriggerMCEfficiencyWeight",
        "0:crossTriggerDataEfficiencyWeight",
        "0:singleTriggerMCEfficiencyWeight",
        "0:singleTriggerDataEfficiencyWeight",
        "0:singleTriggerMCEfficiencyWeightKIT",
        "0:singleTriggerDataEfficiencyWeightKIT",
        "1:crossTriggerMCEfficiencyWeight",
        "1:crossTriggerDataEfficiencyWeight",
        "1:singleTriggerMCEfficiencyWeight",
        "1:singleTriggerDataEfficiencyWeight",
        "1:singleTriggerMCEfficiencyWeightKIT",
        "1:singleTriggerDataEfficiencyWeightKIT",

        "0:triggerWeight",
        "0:isoweight",
        "0:idweight",
        "0:trackWeight",
        "1:isoweight",
        "1:idweight",
        "1:trackWeight"
    ]
    config["RooWorkspaceObjectNames"] = [
        "0:m_trg_MuTau_Mu20Leg_desy_mc",
        "0:m_trg_MuTau_Mu20Leg_desy_data",
        "0:m_trg_SingleMu_Mu24ORMu27_desy_mc",
        "0:m_trg_SingleMu_Mu24ORMu27_desy_data",
        "0:m_trg24or27_mc",
        "0:m_trg24or27_data",
        "1:m_trg_MuTau_Mu20Leg_desy_mc",
        "1:m_trg_MuTau_Mu20Leg_desy_data",
        "1:m_trg_SingleMu_Mu24ORMu27_desy_mc",
        "1:m_trg_SingleMu_Mu24ORMu27_desy_data",
        "1:m_trg24or27_mc",
        "1:m_trg24or27_data",

        "0:m_trg_ratio",  # "0:m_trgOR4_binned_ratio",
        "0:m_iso_ratio",  # "0:m_iso_binned_ratio",
        "0:m_id_ratio",
        "0:m_trk_ratio",
        "1:m_iso_ratio",  # "1:m_iso_binned_ratio",
        "1:m_id_ratio",
        "1:m_trk_ratio"
    ]
    config["RooWorkspaceObjectArguments"] = [
        "0:m_pt,m_eta",
        "0:m_pt,m_eta",
        "0:m_pt,m_eta",
        "0:m_pt,m_eta",
        "0:m_pt,m_eta",
        "0:m_pt,m_eta",
        "1:m_pt,m_eta",
        "1:m_pt,m_eta",
        "1:m_pt,m_eta",
        "1:m_pt,m_eta",
        "1:m_pt,m_eta",
        "1:m_pt,m_eta",

        "0:m_pt,m_eta",  # ,m_iso
        "0:m_pt,m_eta",  # ,m_iso
        "0:m_pt,m_eta",
        "0:m_eta",
        "1:m_pt,m_eta",  # ,m_iso
        "1:m_pt,m_eta",
        "1:m_eta"
    ]

    # Basic selection criterias
    config["TauID"] = "TauIDRecommendation13TeV"
    config["TauUseOldDMs"] = True
    config["MuonLowerPtCuts"] = ["10.0"]
    config["MuonUpperAbsEtaCuts"] = ["2.1"]

    # Settings for the NewValidDiTauPairCandidatesProducers.h
    config["DiTauPairMinDeltaRCut"] = 0.3
    config["DiTauPairIsTauIsoMVA"] = True
    config["DiTauPairLepton1LowerPtCuts"] = [  # not clear if the cut-off should be the same or different for all pathes
        "HLT_IsoMu24_v:25.0",
        "HLT_IsoMu27_v:28.0",
        "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v:25",  # extra pathes might be not needed?
        "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:10",
        "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:14",
        "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v:24",
    ]
    config["DiTauPairLepton2LowerPtCuts"] = [
        "HLT_IsoMu24_v:25.0",
        "HLT_IsoMu27_v:28.0",
        "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v:25",  # should the threshold be modified for l2?
        "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:10",
        "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:14",
        "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v:24",
    ]
    config["CheckLepton1TriggerMatch"] = [
        "trg_singlemuon_24",
        "trg_singlemuon_27",
        "trg_singletau_leading",
        "trg_singleelectron_27",
        "trg_singleelectron_32",
        "trg_singleelectron_32_fallback",
        "trg_singleelectron_35",

        "trg_crossmuon_mu20tau27",
        "trg_crossele_ele24tau30",
        "trg_doubletau_35_tightiso_tightid",
        "trg_doubletau_40_mediso_tightid",
        "trg_doubletau_40_tightiso",
        "trg_muonelectron_mu12ele23",
        "trg_muonelectron_mu23ele12",
        "trg_muonelectron_mu8ele23",
    ]
    config["CheckLepton2TriggerMatch"] = [
        "trg_singletau_trailing",

        "trg_crossmuon_mu20tau27",
        "trg_crossele_ele24tau30",
        "trg_doubletau_35_tightiso_tightid",
        "trg_doubletau_40_mediso_tightid",
        "trg_doubletau_40_tightiso",
        "trg_muonelectron_mu12ele23",
        "trg_muonelectron_mu23ele12",
        "trg_muonelectron_mu8ele23",
    ]
    config["HLTBranchNames"] = [
        "trg_singlemuon_24:HLT_IsoMu24_v",
        "trg_singlemuon_27:HLT_IsoMu27_v",
        "trg_crossmuon_mu20tau27:HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v",
        "trg_singleelectron_27:HLT_Ele27_WPTight_Gsf_v",
        "trg_singleelectron_32:HLT_Ele32_WPTight_Gsf_v",
        "trg_singleelectron_32_fallback:HLT_Ele32_WPTight_Gsf_DoubleL1EG_v",
        "trg_singleelectron_35:HLT_Ele35_WPTight_Gsf_v",
        "trg_crossele_ele24tau30:HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v",
        "trg_doubletau_35_tightiso_tightid:HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v",
        "trg_doubletau_40_mediso_tightid:HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v",
        "trg_doubletau_40_tightiso:HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v",
        "trg_singletau_leading:HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v",
        "trg_singletau_trailing:HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v",
        "trg_muonelectron_mu12ele23:HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v",
        "trg_muonelectron_mu23ele12:HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v",
        "trg_muonelectron_mu8ele23:HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v",
    ]

    config["EventWeight"] = "eventWeight"
    config["TauTauRestFrameReco"] = "collinear_approximation"

    if re.search("(Run201|Embedding201|Summer1|Fall1)", nickname):
        config["MuonTriggerFilterNames"] = [
            "HLT_IsoMu24_v:hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07",
            "HLT_IsoMu27_v:hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07",
            "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v:hltL3crIsoL1sMu18erTau24erIorMu20erTau24erL1f0L2f10QL3f20QL3trkIsoFiltered0p07",  # extra pathes might be not needed?
            "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMuon8Ele23RelTrkIsoFiltered0p4MuonLeg,hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered8",
            "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter",
            "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu12TrkIsoVVLEle23CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered12",
            "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu12TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter",
            "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered23",
            "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLDZFilter"
        ]

    # BTag setting
    config["InvalidateNonMatchingElectrons"] = False
    config["InvalidateNonMatchingMuons"] = False
    config["InvalidateNonMatchingTaus"] = False
    config["InvalidateNonMatchingJets"] = False
    config["DirectIso"] = True

    # Additional variables to compute
    config["Quantities"] = importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.syncQuantities").build_list()
    config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.weightQuantities").build_list())
    # config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Includes.MVAInputQuantities").build_list())
    config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.zptQuantities").build_list())
    config["Quantities"].extend(importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM2017.Includes.lheWeights").build_list())
    config["Quantities"].extend([
        "had_gen_match_pT_1",
        "had_gen_match_pT_2",
    ])

    config["OSChargeLeptons"] = True
    config["TopPtReweightingStrategy"] = "Run2"
    if re.search("(Run2017|Embedding2017|Summer17|Fall17)", nickname):
        pass
    elif re.search("(Fall15MiniAODv2|Run2015)", nickname):
        config["MuonEnergyCorrection"] = "rochcorr2015"
        config["MuonRochesterCorrectionsFile"] = "$CMSSW_BASE/src/Artus/KappaAnalysis/data/rochcorr/RoccoR_13tev_2015.txt"
    else:
        config["MuonEnergyCorrection"] = "rochcorr2016"
        config["MuonRochesterCorrectionsFile"] = "$CMSSW_BASE/src/Artus/KappaAnalysis/data/rochcorr2016"

    config["Processors"] = []

    if not (isEmbedded):
        config["Processors"].append("producer:ElectronCorrectionsProducer")

    config["Processors"].extend((
        "producer:HttValidLooseElectronsProducer",
        "producer:HttValidLooseMuonsProducer",
        "producer:HltProducer",
        "producer:MetSelector",
        # "producer:MuonCorrectionsProducer",
        "producer:ValidMuonsProducer",
        "filter:ValidMuonsFilter",
        "producer:MuonTriggerMatchingProducer",
        "filter:MinMuonsCountFilter",
        "producer:HttValidVetoMuonsProducer",
        "producer:ValidElectronsProducer",
    ))

    if not isData:
        config["Processors"].append("producer:HttValidGenTausProducer")

    if isDY or isWjets or isSignal:
        config["Processors"].append("producer:TauCorrectionsProducer")

    config["Processors"].extend((
        "producer:ValidTausProducer",
        "producer:TauTriggerMatchingProducer",
        "producer:NewValidMMPairCandidatesProducer",
        "filter:ValidDiTauPairCandidatesFilter",
        "producer:Run2DecayChannelProducer",
        # "producer:MvaMetSelector",
        "producer:DiVetoMuonVetoProducer",
        "producer:TaggedJetCorrectionsProducer",
        "producer:ValidTaggedJetsProducer",
        "producer:ValidBTaggedJetsProducer",
    ))

    if isDY or isWjets or isSignal:
        config["Processors"].append(
            "producer:MetCorrector",
            # "producer:MvaMetCorrector"
        )

    config["Processors"].extend((
        "producer:TauTauRestFrameSelector",
        "producer:DiLeptonQuantitiesProducer",
        "producer:DiJetQuantitiesProducer",
    ))

    config["Processors"].append("producer:SvfitProducer")

    if isTTbar:
        config["Processors"].append("producer:TopPtReweightingProducer")
    if isDY:
        config["Processors"].append("producer:ZPtReweightProducer")

    config["Processors"].append(
        "filter:MinimalPlotlevelFilter",
        # "producer:MVATestMethodsProducer",
        # "producer:MVAInputQuantitiesProducer")
    )

    if not isData:
        config["Processors"].extend((
            # "producer:TriggerWeightProducer",
            # "producer:IdentificationWeightProducer"
            "producer:RooWorkspaceWeightProducer",
        ))

    config["Processors"].append("producer:EventWeightProducer")

    config["AddGenMatchedParticles"] = True
    config["AddGenMatchedTaus"] = True
    config["AddGenMatchedTauJets"] = True
    config["BranchGenMatchedMuons"] = True
    config["BranchGenMatchedTaus"] = True
    config["Consumers"] = [
        "KappaLambdaNtupleConsumer",
        "cutflow_histogram",
        # "CutFlowTreeConsumer",
        # "KappaElectronsConsumer",
        # "KappaTausConsumer",
        # "KappaTaggedJetsConsumer",
        # "RunTimeConsumer",
        # "PrintEventsConsumer",
    ]

    # pipelines - systematic shifts
    return ACU.apply_uncertainty_shift_configs(
        'mm',
        config,
        importlib.import_module("HiggsAnalysis.KITHiggsToTauTau.data.ArtusConfigs.Run2MSSM.syst_shifts_nom").build_config(nickname))
