
# -*- coding: utf-8 -*-
import ROOT

"""
"""
# import helper classes
# necessary for all analyses
from Artus.HenryPlotter.cutstring import Cut, Cuts
from Artus.HenryPlotter.systematics import Systematics, Systematic
from Artus.HenryPlotter.categories import Category
from Artus.HenryPlotter.binning import Variable_Binning, Constant_Binning
from Artus.HenryPlotter.variable import Variable
from Artus.HenryPlotter.systematic_variations import Nominal, Different_pipeline, Reapply_remove_weight, create_syst_variations
from Artus.HenryPlotter.process import Process

# Estimation methods, import only what is really necessary
from Artus.HenryPlotter.estimation_methods import Data_estimation, TT_estimation, VV_estimation, WJ_estimation, QCD_estimation, ZtoMuMu_estimation, ZtoTauTautoMuMu_estimation, ZtoMuMuFakes_estimation, TTbartoMuMu_estimation, TTbartoTauTautoMuMu_estimation, TTbartoLeptons_estimation, TTbartoMuMuFakes_estimation
from Artus.HenryPlotter.era import Run2016BCDEFGH
from Artus.HenryPlotter.channel import MM, MM_SS

# Logging
import logging
import logging.handlers
logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

file_handler = logging.FileHandler("make_systematic.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


directory = "/storage/b/akhmet/merged_files_from_nrg/artusjobs_embedding_selection_19_10_2017/"
era=Run2016BCDEFGH()

mm = MM()
mm_ss = MM_SS()

ztomm = Process("ZToMM", ZtoMuMu_estimation(era, directory, mm))
ztotttomm = Process("ZToTTToMM", ZtoTauTautoMuMu_estimation(era, directory, mm))
ztommfakes = Process("ZToMMFakes", ZtoMuMuFakes_estimation(era, directory, mm))
ttbartomm = Process("TTbarToMM", TTbartoMuMu_estimation(era, directory, mm))
ttbartotttomm = Process("TTbarToTTToMM", TTbartoTauTautoMuMu_estimation(era, directory, mm))
ttbartoleptons = Process("TTbarToLeptons", TTbartoLeptons_estimation(era, directory, mm))
ttbartommfakes = Process("TTbarToMMFakes", TTbartoMuMuFakes_estimation(era, directory, mm))
wj_mm =  Process("WJ",  WJ_estimation(era, directory, mm))
vv_mm =  Process("VV",  VV_estimation(era, directory, mm))
data_mm = Process("data", Data_estimation(era, directory, mm))

ztomm_ss = Process("ZToMM", ZtoMuMu_estimation(era, directory, mm_ss))
ztotttomm_ss = Process("ZToTTToMM", ZtoTauTautoMuMu_estimation(era, directory, mm_ss))
ztommfakes_ss = Process("ZToMMFakes", ZtoMuMuFakes_estimation(era, directory, mm_ss))
ttbartomm_ss = Process("TTbarToMM", TTbartoMuMu_estimation(era, directory, mm_ss))
ttbartotttomm_ss = Process("TTbarToTTToMM", TTbartoTauTautoMuMu_estimation(era, directory, mm_ss))
ttbartoleptons_ss = Process("TTbarToLeptons", TTbartoLeptons_estimation(era, directory, mm_ss))
ttbartommfakes_ss = Process("TTbarToMMFakes", TTbartoMuMuFakes_estimation(era, directory, mm_ss))
wj_mm_ss =  Process("WJ",  WJ_estimation(era, directory, mm_ss))
vv_mm_ss =  Process("VV",  VV_estimation(era, directory, mm_ss))
data_mm_ss = Process("data", Data_estimation(era, directory, mm_ss))

qcd_mm_ss = Process("QCD", QCD_estimation(era, directory, mm_ss, [ztomm_ss, ztotttomm_ss, ztommfakes_ss, ttbartomm_ss, ttbartotttomm_ss, ttbartommfakes_ss, vv_mm_ss, wj_mm_ss], data_mm_ss))
# systematic variations. Start with "nominal" for the central values without any variation
nominal = Nominal()


m_vis = Variable("m_vis", Constant_Binning(40,20,200))
ptvis = Variable("ptvis", Constant_Binning(40,20,200))
pt_1 = Variable("pt_1", Constant_Binning(40,20,200))
pt_2 = Variable("pt_2", Constant_Binning(40,20,200))

#definition of categories
inclusive_mm = Category( "inclusive", mm, Cuts(), variable=m_vis)
inclusive_mm_ss = Category( "inclusive_ss", mm_ss, Cuts(), variable=m_vis)

#systematics object, to be filled
systematics = Systematics(1) # run single-core

# first, create the nominals
for process in [ztomm, ztotttomm, ztommfakes, ttbartomm, ttbartotttomm, ttbartoleptons, ttbartommfakes, vv_mm, wj_mm, data_mm]:
	systematics.add( Systematic(category=inclusive_mm, process=process, analysis = "embedding_selection", era=era, syst_var=nominal))

for process in [qcd_mm_ss]:
	systematics.add( Systematic(category=inclusive_mm_ss, process=process, analysis = "embedding_selection", era=era, syst_var=nominal))

systematics.produce()
systematics.summary()
