#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import copy
import Artus.Utility.jsonTools as jsonTools
#import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz
import importlib
#import os

def build_config(nickname):
  config = jsonTools.JsonDict()
  #datasetsHelper = datasetsHelperTwopz.datasetsHelperTwopz(os.path.expandvars("$CMSSW_BASE/src/Kappa/Skimming/data/datasets.json"))
  
  config["PlotlevelFilterExpressionQuantities"] = [
    "againstElectronVLooseMVA6_2",
    "extraelec_veto",
    "againstMuonTight3_2",
    "extramuon_veto",
    "byVLooseIsolationMVArun2017v2DBoldDMwLT2017_2",
    "nDiMuonVetoPairsOS"
  ]
  config["PlotlevelFilterExpression"] = "(nDiMuonVetoPairsOS < 0.5)*(extraelec_veto < 0.5)*(extramuon_veto < 0.5)*(againstMuonTight3_2 > 0.5)*(againstElectronVLooseMVA6_2 > 0.5)*(byVLooseIsolationMVArun2017v2DBoldDMwLT2017_2 > 0.5)"
  
  return config
