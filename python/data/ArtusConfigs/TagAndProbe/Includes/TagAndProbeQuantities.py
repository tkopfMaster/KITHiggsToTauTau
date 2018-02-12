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
    "usedMuonIDshortTerm",
    "pt_t",
    "eta_t",
    "phi_t",
    "id_t",
    "iso_t",
    "muon_p",
    "trk_p",
    "pt_p",
    "eta_p",
    "phi_p",
    "id_p",
    "iso_p",
    "dxy_p",
    "dz_p",
    "gen_p",
    "genZ_p",
    "m_ll",
    "trg_t_IsoMu24",
    "trg_t_IsoMu27",
    "trg_p_IsoMu24",
    "trg_p_IsoMu27",
    ]

  return quantities_list