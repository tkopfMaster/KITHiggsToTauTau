#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
#import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

def build_list():
  quantities_list = [
    "muR1p0_muF1p0_weight",
    "muR1p0_muF2p0_weight",
    "muR1p0_muF0p5_weight",
    "muR2p0_muF1p0_weight",
    "muR2p0_muF2p0_weight",
    "muR2p0_muF0p5_weight",
    "muR0p5_muF1p0_weight",
    "muR0p5_muF2p0_weight",
    "muR0p5_muF0p5_weight"
  ]
  
  return quantities_list