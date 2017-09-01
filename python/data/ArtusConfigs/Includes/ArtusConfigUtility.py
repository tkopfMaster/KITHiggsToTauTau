#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

def apply_uncertainty_shift_configs(configname, config, systs):
  config_with_systs = jsonTools.JsonDict()
  for key, syst in systs.items():
    longkey = configname + "_" + key
    config_with_systs[longkey] = jsonTools.JsonDict(syst)
    config_with_systs[longkey] += config
  return config_with_systs