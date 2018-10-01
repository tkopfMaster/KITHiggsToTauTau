#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.jsonTools as jsonTools
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

import re
import os


def build_config(nickname, **kwargs):
    """For estimating the uncertainty arrising from the TauElectronFakeEnergyCorrection*"""
    config = jsonTools.JsonDict()
    datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))

    # define frequently used conditions
    isEmbedded = datasetsHelper.isEmbedded(nickname)
    isDY = re.search("DY.?JetsToLLM(50|150)", nickname)
    isEWKZ2Jets = re.search("EWKZ2Jets", nickname)

    if isDY or isEWKZ2Jets or isEmbedded:
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
