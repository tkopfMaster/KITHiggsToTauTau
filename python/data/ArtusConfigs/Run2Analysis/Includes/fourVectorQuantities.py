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
    "leadingLepLV",
    "lep1LV",
    "posLepLV",
    
    "trailingLepLV",
    "lep2LV",
    "negLepLV",
    
    "leadingGenMatchedLepLV",
    "genMatchedLep1LV",
    "posGenMatchedLepLV",
    
    "leadingGenMatchedLepFound",
    "genMatchedLep1Found",
    "posGenMatchedLepFound",
    
    "trailingGenMatchedLepLV",
    "genMatchedLep2LV",
    "negGenMatchedLepLV",
    
    "trailingGenMatchedLepFound",
    "genMatchedLep2Found",
    "negGenMatchedLepFound",
    
    "diLepLV",
    "genDiLepLV",
    "genDiLepFound",
    "genDiTauLV",
    "genDiTauFound",
    
    "leadingJetLV",
    "trailingJetLV",
    "thirdJetLV",
    "fourthJetLV",
    "fifthJetLV",
    "sixthJetLV"
  ]
  
  return quantities_list