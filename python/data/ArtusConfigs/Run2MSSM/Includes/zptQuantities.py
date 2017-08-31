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
    "zPtWeightEsUp",
    "zPtWeightEsDown",
    "zPtWeightStatPt0Up",
    "zPtWeightStatPt0Down",
    "zPtWeightStatPt40Up",
    "zPtWeightStatPt40Down",
    "zPtWeightStatPt80Up",
    "zPtWeightStatPt80Down",
    "zPtWeightTTbarUp",
    "zPtWeightTTbarDown"
  ]
  
  return quantities_list