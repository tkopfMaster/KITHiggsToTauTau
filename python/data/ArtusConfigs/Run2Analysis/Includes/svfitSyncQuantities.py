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
    "m_sv",
    "pt_sv",
    "eta_sv",
    "phi_sv"
    #"met_sv",
    #"m_sv_Up",
    #"m_sv_Down"
  ]
  
  return quantities_list