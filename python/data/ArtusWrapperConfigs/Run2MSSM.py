#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import json
import Artus.Utility.jsonTools as jsonTools

def build_config():
	config = jsonTools.JsonDict()
	config["name"]="Dictionary"
	return config