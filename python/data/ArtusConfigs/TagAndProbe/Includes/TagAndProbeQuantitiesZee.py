#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import re
import json
import Artus.Utility.jsonTools as jsonTools
import Kappa.Skimming.datasetsHelperTwopz as datasetsHelperTwopz

def build_list():
  quantities_list = [
    "wt",
    "n_vtx",
    "run",
    "lumi",
    "evt",
    "pt_t",
    "eta_t",
    "phi_t",
    "id_t",
    "iso_t",
    "pt_p",
    "eta_p",
    "sc_eta_p",
    "phi_p",
    "id_p",
    "iso_p",
    "gen_p",
    "genZ_p",
    "m_ll",
    "trg_t_Ele27WPTight",
    "trg_p_Ele27WPTight",
    "trg_t_Ele32WPTight",
    "trg_p_Ele32WPTight",
    "trg_t_Ele35WPTight",
    "trg_p_Ele35WPTight"
  ]

  return quantities_list