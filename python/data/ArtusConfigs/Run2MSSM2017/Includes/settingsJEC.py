#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)
import re

import Artus.Utility.jsonTools as jsonTools


def build_config(nickname):
    config = jsonTools.JsonDict()

    config["JEC_documentation"] = [
        "https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2017#Jet_MET_uncertainty_treatment",
        "https://twiki.cern.ch/twiki/bin/view/CMS/JECUncertaintySources#Main_uncertainties_2016_80X",
    ]

    # Explicit configuration
    #   corrections need to be upplied on top of Uncorrected jets which should be cross-checked in Kappa
    if re.search("Run2015", nickname):
        '''
        config["JetEnergyCorrectionParameters"] = [
            "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_L1FastJet_AK4PFchs.txt",
            "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_L2Relative_AK4PFchs.txt",
            "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_L3Absolute_AK4PFchs.txt",
            "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_L2L3Residual_AK4PFchs.txt"
        ]
        '''
        config["JetEnergyCorrectionUncertaintyParameters"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_DATA_Uncertainty_AK4PFchs.txt"
    else:
        '''
        config["JetEnergyCorrectionParameters"] = [
            "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_MC_L1FastJet_AK4PFchs.txt",
            "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_MC_L2Relative_AK4PFchs.txt",
            "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_MC_L3Absolute_AK4PFchs.txt"
        ]
        '''
        config["JetEnergyCorrectionUncertaintyParameters"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Fall15/Fall15_25nsV2_MC_Uncertainty_AK4PFchs.txt"

    # config["JetEnergyCorrectionUncertaintySource"] = ""
    # config["JetEnergyCorrectionUncertaintyShift"] = 0.0
    config["JetEnergyCorrectionSplitUncertainty"] = True
    config["JetEnergyCorrectionSplitUncertaintyParameters"] = "$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/jec/Summer16/Summer16_23Sep2016V4_DATA_UncertaintySources_AK4PFchs.txt"
    config["UseJECShiftsForBJets"] = True
    config["JetEnergyCorrectionSplitUncertaintyParameterNames"] = [  # 28 main uncertainties sources
        "AbsoluteFlavMap",
        "AbsoluteMPFBias",
        "AbsoluteScale",
        "AbsoluteStat",
        "FlavorQCD",
        "Fragmentation",
        "PileUpDataMC",
        "PileUpPtBB",
        "PileUpPtEC1",
        "PileUpPtEC2",
        "PileUpPtHF",
        "PileUpPtRef",
        "RelativeBal",
        "RelativeFSR",
        "RelativeJEREC1",
        "RelativeJEREC2",
        "RelativeJERHF",
        "RelativePtBB",
        "RelativePtEC1",
        "RelativePtEC2",
        "RelativePtHF",
        "RelativeStatEC",
        "RelativeStatFSR",
        "RelativeStatHF",
        "SinglePionECAL",
        "SinglePionHCAL",
        "TimePtEta",
        "Total",
        "Closure"
    ]

    return config
