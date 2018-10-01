#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.jsonTools as jsonTools
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

import re
import os
import importlib


def build_config(nickname, **kwargs):
    etau_fake_es = True if "sub_analysis" in kwargs and kwargs["sub_analysis"] == "etau-fake-es" else False

    config = jsonTools.JsonDict()
    datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))

    # define frequently used conditions
    isEmbedded = datasetsHelper.isEmbedded(nickname)
    isData = datasetsHelper.isData(nickname) and (not isEmbedded)
    isDY = re.search("DY.?JetsToLLM(50|150)", nickname)
    isEWKZ2Jets = re.search("EWKZ2Jets", nickname)

    # includes
    includes = []
    for include_file in includes:
        analysis_config_module = importlib.import_module(include_file)
        config += analysis_config_module.build_config(nickname)

    # explicit configuration for pipelins (keys)
    config["nominal"] = {
        "JetEnergyCorrectionUncertaintyShift": [0.0],
    }

    if not isData:
        config["tauEsOneProngUp"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauEnergyCorrectionOneProng": 1.016,
        }

        config["tauEsOneProngDown"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauEnergyCorrectionOneProng": 0.999,
        }

        config["tauEsOneProngOnePiZeroUp"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauEnergyCorrectionOneProngPiZeros": 0.999,
        }

        config["tauEsOneProngOnePiZeroDown"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauEnergyCorrectionOneProngPiZeros": 0.986,
        }

        config["tauEsThreeProngUp"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauEnergyCorrectionThreeProng": 0.996,
        }

        config["tauEsThreeProngDown"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauEnergyCorrectionThreeProng": 0.983,
        }

    if isDY or isEmbedded:
        config["eleTauEsOneProngZeroPiZeroUp"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauElectronFakeEnergyCorrectionOneProng": 1.029,
        }

        config["eleTauEsOneProngZeroPiZeroDown"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauElectronFakeEnergyCorrectionOneProng": 1.019,
        }

        config["eleTauEsOneProngOnePiZeroUp"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauElectronFakeEnergyCorrectionOneProngPiZeros": 1.086,
        }

        config["eleTauEsOneProngOnePiZeroDown"] = {
            "JetEnergyCorrectionUncertaintyShift": [0.0],
            "TauElectronFakeEnergyCorrectionOneProngPiZeros": 1.066,
        }

    return config
