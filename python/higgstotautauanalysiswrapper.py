# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import argparse
import glob
import os
import tempfile
import hashlib
import json
import shutil
import subprocess
import re
from string import Template
from datetime import datetime

import Artus.Utility.jsonTools as jsonTools
import Artus.Utility.tools as tools
import Artus.Utility.profile_cpp as profile_cpp

import sys
import importlib

class HiggsToTauTauAnalysisWrapper():
	def __init__(self, executable=None, userArgParsers=None):
		
		self._config = jsonTools.JsonDict()
		self._executable = None

		self._parser = None
		#Load default argument parser
		self._initArgumentParser(userArgParsers)
		#Parse command line arguments and return dict
		self._args = self._parser.parse_args()
		logger.initLogger(self._args)
		
	def run(self):
		#generate artus config
		self.import_analysis_configs()
		#save artus config
		self.saveConfig(filepath)
		
		if self._args.batch:
			#prepare grid-control config
			
			if not self._args.no_run:
				#run gc
		else:
			if not self._args.no_run:
				#run artus locally
		
		if exitCode < 256:
			return exitCode
		else:
			return 1 # Artus sometimes returns exit codes >255 that are not supported
		
	def _initArgumentParser(self, userArgParsers=None):
		
		if userArgParsers is None:
			userArgParsers = []
		
		self._parser = argparse.ArgumentParser(parents=[logger.loggingParser] + userArgParsers, fromfile_prefix_chars="@",
		                                       description="Wrapper for Artus executables. Configs are to be set internally.")
		
		self._parser.add_argument("-x", "--executable", help="Artus executable. [Default: %(default)s]", default=os.path.basename(sys.argv[0]))
		self._parser.add_argument("-a", "--analysis", required=True, help="Analysis nick [SM, MSSM] or path to the config module.")

		fileOptionsGroup = self._parser.add_argument_group("File options")
		fileOptionsGroup.add_argument("-i", "--input-files", nargs="+", required=False,
		                              help="Input root files. Leave empty (\"\") if input files from root file should be taken.")
		fileOptionsGroup.add_argument("-o", "--output-file", default="output.root",
		                              help="Output root file. [Default: %(default)s]")
		fileOptionsGroup.add_argument("-w", "--work", default="$ARTUS_WORK_BASE",
		                              help="Work directory base. [Default: %(default)s]")
		fileOptionsGroup.add_argument("-n", "--project-name", default="analysis",
		                              help="Name for this Artus project specifies the name of the work subdirectory.")

		configOptionsGroup = self._parser.add_argument_group("Config options")
		configOptionsGroup.add_argument("-c", "--base-configs", nargs="+", required=False, default={},
		                                help="JSON base configurations. All configs are merged.")
		configOptionsGroup.add_argument("-C", "--pipeline-base-configs", nargs="+",
		                                help="JSON pipeline base configurations. All pipeline configs will be merged with these common configs.")
		configOptionsGroup.add_argument("-p", "--pipeline-configs", nargs="+", action="append",
		                                help="JSON pipeline configurations. Single entries (whitespace separated strings) are first merged. Then all entries are expanded to get all possible combinations. For each expansion, this option has to be used. Afterwards, all results are merged into the JSON base config.")
		configOptionsGroup.add_argument("--nick", default="auto",
		                                help="Kappa nickname name that can be used for switch between sample-dependent settings.")

		configOptionsGroup.add_argument("--disable-repo-versions", default=False, action="store_true",
		                                help="Add repository versions to the JSON config.")
		configOptionsGroup.add_argument("--repo-scan-base-dirs", nargs="+", required=False, default="$CMSSW_BASE/src/",
		                                help="Base directories for repositories scan. [Default: $CMSSW_BASE/src/]")
		configOptionsGroup.add_argument("--repo-scan-depth", required=False, type=int, default=3,
		                                help="Depth of repositories scran. [Default: %(default)s]")
		configOptionsGroup.add_argument("--enable-envvar-expansion", dest="envvar_expansion", default=True, action="store_true",
		                                help="Enable expansion of environment variables in config.")
		configOptionsGroup.add_argument("--disable-envvar-expansion", dest="envvar_expansion", action="store_false",
		                                help="Disable expansion of environment variables in config.")
		configOptionsGroup.add_argument("-P", "--print-config", default=False, action="store_true",
		                                help="Print out the JSON config before running Artus.")
		configOptionsGroup.add_argument("--print-envvars", nargs="+",
		                                help="Log specified environment variables.")
		configOptionsGroup.add_argument("-s", "--save-config", default="",
		                                help="Save the JSON config to FILENAME.")
		configOptionsGroup.add_argument("-f", "--fast", type=int,
		                                help="Limit number of input files or grid-control jobs. 3=files[0:3].")
		configOptionsGroup.add_argument("-e", "--n-events", type=int,
		                                help="Limit number of events to process.")
		configOptionsGroup.add_argument("--gc-config", default="$CMSSW_BASE/src/Artus/Configuration/data/grid-control_base_config.conf",
		                                help="Path to grid-control base config that is replace by the wrapper. [Default: %(default)s]")
		configOptionsGroup.add_argument("--gc-config-includes", nargs="+",
		                                help="Path to grid-control configs to include in the base config.")

		runningOptionsGroup = self._parser.add_argument_group("Running options")
		runningOptionsGroup.add_argument("--no-run", default=False, action="store_true",
		                                 help="Exit before running Artus to only check the configs.")
		runningOptionsGroup.add_argument("--copy-remote-files", default=False, action="store_true",
		                                 help="Copy remote files first to avoid too many open connections.")
		runningOptionsGroup.add_argument("--ld-library-paths", nargs="+",
		                                 help="Add paths to environment variable LD_LIBRARY_PATH.")
		runningOptionsGroup.add_argument("--profile", default="",
		                                 help="Measure performance with profiler. Choose igprof or valgrind.")
		runningOptionsGroup.add_argument("--profile-options", default="pp",
		                                 help="Additional options for profiling. Choose memory (mp) or performance (pp). [Default: %(default)s]")
		runningOptionsGroup.add_argument("-r", "--root", default=False, action="store_true",
		                                 help="Open output file in ROOT TBrowser after completion.")
		runningOptionsGroup.add_argument("-b", "--batch", default=False, const="naf", nargs="?",
		                                 help="Run with grid-control. Optionally select backend. [Default: %(default)s]")
		runningOptionsGroup.add_argument("--pilot-job-files", "--pilot-jobs", default=None, const=1, type=int, nargs="?",
		                                 help="Number of files per sample to be submitted as pilot jobs. [Default: all/1]")
		runningOptionsGroup.add_argument("--files-per-job", type=int, default=15,
		                                 help="Files per batch job. [Default: %(default)s]")
		runningOptionsGroup.add_argument("--area-files", default=None,
		                                 help="Additional area files. [Default: %(default)s]")
		runningOptionsGroup.add_argument("--wall-time", default="24:00:00",
		                                 help="Wall time of batch jobs. [Default: %(default)s]")
		runningOptionsGroup.add_argument("--memory", type=int, default=3000,
		                                 help="Memory (in MB) for batch jobs. [Default: %(default)s]")
		runningOptionsGroup.add_argument("--cmdargs", default="-cG -m 3",
		                                 help="Command line arguments for go.py. [Default: %(default)s]")
		runningOptionsGroup.add_argument("--se-path",
		                                 help="Custom SE path, if it should different from the work directory.")
		runningOptionsGroup.add_argument("--log-to-se", default=False, action="store_true",
		                                 help="Write logfile in batch mode directly to SE. Does not work with remote batch system")
		runningOptionsGroup.add_argument("--partition-lfn-modifier", default = None,
		                                 help="Forces a certain access to input files. See base conf for corresponding dictionary")
		
	
	def import_analysis_configs(self):
		analysis_configs_dict = {
			#'SM' : 'HiggsAnalysis.KITHiggsToTauTau.data.ArtusWrapperConfigs.Run2Analysis',
			#'sm' : 'HiggsAnalysis.KITHiggsToTauTau.data.ArtusWrapperConfigs.Run2Analysis',
			'MSSM' : 'HiggsAnalysis.KITHiggsToTauTau.data.ArtusWrapperConfigs.Run2MSSM',
			'mssm' : 'HiggsAnalysis.KITHiggsToTauTau.data.ArtusWrapperConfigs.Run2MSSM'
		}
		if self._args.analysis in analysis_configs_dict:
			self._analysis_config_module = importlib.import_module(analysis_configs_dict[self._args.analysis])
		else:
			self._analysis_config_module = importlib.import_module(self._args.analysis)
		self._config = self._analysis_config_module.build_config()
		
	def saveConfig(self, filepath=None):
		"""Save Config to File"""
		if not filepath:
			basename = "artus_{0}.json".format(hashlib.md5(str(self._config)).hexdigest())
			filepath = os.path.join(tempfile.gettempdir(), basename)
		self._configFilename = filepath
		self._config.save(filepath, indent=4)
		log.info("Saved JSON config \"%s\" for temporary usage." % self._configFilename)

	
	
'''
class HiggsToTauTauAnalysisWrapper(kappaanalysiswrapper.KappaAnalysisWrapper):

	def __init__(self):
		super(HiggsToTauTauAnalysisWrapper, self).__init__("HiggsToTauTauAnalysis")

	def _initArgumentParser(self, userArgParsers=None):
		super(HiggsToTauTauAnalysisWrapper, self)._initArgumentParser(userArgParsers)

	def modify_replacing_dict(self):
		self.replacingDict["areafiles"] += " auxiliaries/mva_weights"

	def remove_pipeline_copies(self):
		pipelines = self._config.get("Pipelines", {}).keys()
		pipelines_to_remove = []
		pipeline_renamings = {}
		for index1, pipeline1 in enumerate(pipelines):
			if pipeline1 in pipelines_to_remove:
				continue

			for pipeline2 in pipelines[index1+1:]:
				if pipeline2 in pipelines_to_remove:
					continue

				difference = jsonTools.JsonDict.deepdiff(self._config["Pipelines"][pipeline1],
				                                         self._config["Pipelines"][pipeline2])
				if len(difference[0]) == 0 and len(difference[1]) == 0:
					pipelines_to_remove.append(pipeline2)
					new_name = tools.find_common_string(pipeline_renamings.get(pipeline1, pipeline1),
					                                    pipeline_renamings.get(pipeline2, pipeline2))
					# Needed for systematic shifts that are only applied to certain samples.
					# In that case we do not want an extra pipeline with the same configuration
					# as the nominal one.
					if "Down" not in new_name or "Up" not in new_name:
						new_name = new_name.replace(new_name.split("_")[-1], "")
					# Add "nominal" to pipelines without systematic shifts
					if new_name.endswith("_"):
						new_name += "nominal"
					elif "_" not in new_name:
						new_name += "_nominal"
					pipeline_renamings[pipeline1] = new_name.strip("_").replace("__", "_")

		for pipeline in pipelines_to_remove:
			self._config["Pipelines"].pop(pipeline)

		for old_name, new_name in pipeline_renamings.iteritems():
			self._config["Pipelines"][new_name] = self._config["Pipelines"].pop(old_name)

	def readInExternals(self):
		if not "NumberGeneratedEvents" in self._config or (int(self._config["NumberGeneratedEvents"]) < 0):
			from Kappa.Skimming.registerDatasetHelper import get_n_generated_events_from_nick
			from Kappa.Skimming.datasetsHelper2015 import isData
			n_events_from_db = get_n_generated_events_from_nick(self._config["Nickname"])
			if(n_events_from_db > 0):
				self._config["NumberGeneratedEvents"] = n_events_from_db
			elif not isData(self._config["Nickname"]):
				log.fatal("Number of Generated Events not set! Check your datasets.json for nick " + self._config["Nickname"])
				sys.exit(1)

		if not ("CrossSection" in self._config) or (self._config["CrossSection"] < 0):
			from Kappa.Skimming.registerDatasetHelper import get_xsec
			from Kappa.Skimming.datasetsHelper2015 import isData
			xsec = get_xsec(self._config["Nickname"])
			if(xsec > 0):
				self._config["CrossSection"] = xsec
			elif not isData(self._config["Nickname"]):
				log.fatal("Cross section for " + self._config["Nickname"] + " not set! Check your datasets.json")
				sys.exit(1)

		if not ("GeneratorWeight" in self._config):
			from Kappa.Skimming.registerDatasetHelper import get_generator_weight
			from Kappa.Skimming.datasetsHelper2015 import isData
			generator_weight = get_generator_weight(self._config["Nickname"])
			if(generator_weight > 0 and generator_weight <= 1.0):
				self._config["GeneratorWeight"] = generator_weight


	def run(self):
		#symlinkBaseDir = os.path.expandvars("$CMSSW_BASE/src/HiggsAnalysis/KITHiggsToTauTau/data/ArtusOutputs")
		#if not os.path.exists(symlinkBaseDir):
		#	os.makedirs(symlinkBaseDir)
		
		#if not self.projectPath is None:
		#	symlinkDir = os.path.join(symlinkBaseDir, "recent")
		#	if os.path.islink(symlinkDir):
		#		os.remove(symlinkDir)
		#	os.symlink(self.projectPath, symlinkDir)
		
		exitCode = super(HiggsToTauTauAnalysisWrapper, self).run()
		
		#if not self.projectPath is None:
		#	symlinkDir = os.path.join(symlinkBaseDir, os.path.basename(self.projectPath))
		#	os.symlink(self.projectPath, symlinkDir)
		
		return exitCode
'''