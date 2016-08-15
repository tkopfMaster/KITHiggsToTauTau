# -*- coding: utf-8 -*-

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import CombineHarvester.CombineTools.ch as ch

import HiggsAnalysis.KITHiggsToTauTau.datacards.datacards as datacards


class ZttPolarisationDatacards(datacards.Datacards):
	def __init__(self, cb=None):
		super(ZttPolarisationDatacards, self).__init__(cb)
		
		if cb is None:
			# ======================================================================
			# MT channel
			self.add_processes(
					channel="mt",
					categories=["mt_"+category for category in ["l_rho"]],
					bkg_processes=["ZLL", "TT", "VV", "W", "QCD"],
					sig_processes=["ZTTPOSPOL", "ZTTNEGPOL"],
					analysis=["ztt"],
					era=["13TeV"],
					mass=["0"]
			)
		
			# efficiencies
			self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL", "ZLL", "TT", "VV"]).AddSyst(self.cb, *self.muon_efficieny_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficieny_corr_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL", "TT", "VV"]).AddSyst(self.cb, *self.tau_efficieny_syst_args)

			# extrapolation uncertainty
			self.cb.cp().channel(["mt"]).process(["W"]).AddSyst(self.cb, *self.wj_extrapol_syst_args)

			# mu->tau fake ES
			#self.cb.cp().channel(["mt"]).process(["ZLL"]).AddSyst(self.cb, *self.muFakeTau_es_syst_args)

			# fake-rate
			self.cb.cp().channel(["mt"]).process(["ZLL"]).AddSyst(self.cb, *self.eFakeTau_vloose_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZLL"]).AddSyst(self.cb, *self.muFakeTau_syst_args)

			# b-tag efficiency and mistag
			self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL", "TT"]).AddSyst(self.cb, *self.btag_efficieny_syst_args)
			self.cb.cp().channel(["mt"]).process(["ZTTPOSPOL", "ZTTNEGPOL", "TT"]).AddSyst(self.cb, *self.btag_mistag_syst_args)

			# ======================================================================
			# All channels
			#self.cb.cp().process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, "ZTT_uniform_2", "lnU", ch.SystMap()(2.0))
		
			# lumi
			self.cb.cp().process(["ZTTPOSPOL", "ZTTNEGPOL", "ZLL", "TT", "VV"]).AddSyst(self.cb, *self.lumi_syst_args)

			# cross section
			self.cb.cp().process(["ZLL"]).AddSyst(self.cb, *self.zll_cross_section_syst_args)
			self.cb.cp().process(["VV"]).AddSyst(self.cb, *self.vv_cross_section_syst_args)
			self.cb.cp().process(["TT"]).AddSyst(self.cb, *self.ttj_cross_section_syst_args)
			self.cb.cp().process(["W"]).AddSyst(self.cb, *self.wj_cross_section_syst_args)

			# signal acceptance/efficiency
			self.cb.cp().process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.ztt_pdf_scale_syst_args)
			self.cb.cp().process(["ZTTPOSPOL", "ZTTNEGPOL"]).AddSyst(self.cb, *self.ztt_qcd_scale_syst_args)

			# QCD systematic
			self.cb.cp().process(["QCD"]).AddSyst(self.cb, *self.qcd_syst_inclusive_args)
		
			if log.isEnabledFor(logging.DEBUG):
				self.cb.PrintAll()

