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
from Artus.HenryPlotter.estimation_methods_2017 import Ztt_estimation, Zll_estimation, Data_estimation, TT_estimation, WJ_estimation, QCD_estimation # roughest possible estimations. Write your own, inheriting from Estimation_method
from Artus.HenryPlotter.era import Run2017BCD
from Artus.HenryPlotter.channel import MT

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

directory = "/storage/b/akhmet/merged_files_from_nrg/06_10_2017_mssm_data_mc_2017_test/"
era=Run2017BCD()

mt = MT()
ztt_mt = Process("ZTT", Ztt_estimation(era, directory, mt))
zll_mt = Process("ZLL", Zll_estimation(era, directory, mt))
tt_mt =  Process("TT",  TT_estimation(era, directory, mt))
wj_mt =  Process("WJ",  WJ_estimation(era, directory, mt))
data_mt = Process("data", Data_estimation(era, directory, mt))
qcd_mt = Process("QCD", QCD_estimation(era, directory, mt, [ztt_mt, zll_mt, tt_mt, wj_mt], data_mt))

# systematic variations. Start with "nominal" for the central values without any variation

nominal = Nominal()

pt_1 = Variable("pt_1", Constant_Binning(25,25,100))
pt_2 = Variable("pt_2", Constant_Binning(25,25,100))
eta_1 = Variable("eta_1", Constant_Binning(20,-2.5,2.5))
eta_2 = Variable("eta_2", Constant_Binning(20,-2.5,2.5))
phi_1 = Variable("phi_1", Constant_Binning(20,-3.2,3.2))
phi_2 = Variable("phi_2", Constant_Binning(20,-3.2,3.2))
met = Variable("met", Constant_Binning(40,0,200))
m_vis = Variable("m_vis", Constant_Binning(40,0,200))
ptvis = Variable("ptvis", Constant_Binning(30,0,150))
jpt_1 = Variable("jpt_1", Constant_Binning(25,25,100))
jpt_2 = Variable("jpt_2", Constant_Binning(25,25,100))
jeta_1 = Variable("jeta_1", Constant_Binning(20,-2.5,2.5))
jeta_2 = Variable("jeta_2", Constant_Binning(20,-2.5,2.5))
jphi_1 = Variable("jphi_1", Constant_Binning(20,-3.2,3.2))
jphi_2 = Variable("jphi_2", Constant_Binning(20,-3.2,3.2))
npv = Variable("npv", Constant_Binning(40,0,40))
rho = Variable("rho", Constant_Binning(30,0,30))
njetspt30 = Variable("njetspt30", Constant_Binning(10,-0.5,9.5))

variables = [pt_1, pt_2, eta_1, eta_2, phi_1, phi_2, met, m_vis, ptvis, jpt_1, jpt_2, jeta_1, jeta_2, jphi_1, jphi_2, npv, rho, njetspt30]
processes = [ztt_mt,zll_mt,tt_mt,wj_mt,data_mt,qcd_mt]

#definition of categories
mt_inclusive_categories = [ Category("mt_inclusive", mt, Cuts(Cut("mt_1<70","mt")), variable=v) for v in variables]


#mt_btag_tight = Category ("mt_btag_tight", MT(), Cuts(
#        Cut("mt_1<40","mt"),
#        Cut("nbtag > 0")),
#        variable=pt_1)

#systematics object, to be filled
systematics = Systematics(1) # run single-core
# first, create the nominals
for process in processes:
    for category in mt_inclusive_categories:
	systematics.add( Systematic(category=category, process=process, analysis = "mssm", era=era, syst_var=nominal))

systematics.produce()
systematics.summary()
