#!/usr/bin/env python

import HiggsAnalysis.KITHiggsToTauTau.plotting.embedding.embedding_plot_classes as pltcl
 
## Vertex Refitting Check for Muon Embedding

Fall17Neutrino = pltcl.single_plotline(
	name = "Fall17Neutrino",
	num_file = "/storage/c/jbechtel/artus_outputs/2018_05_31/ZNuNu_MC/ZJetsToNuNuHT-100To200_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph_v1/ZJetsToNuNuHT-100To200_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph_v1.root",
	num_folder = "nn_nominal",
	den_folder = "nn_nominal",
	num_tree = "ntuple",
	label = "Z#rightarrow#nu#nu simulation",
	color = "kRed")
	
Fall17Neutrino_copy = pltcl.single_plotline(
	name = "Fall17Neutrino_copy",
	num_file = "/storage/c/jbechtel/artus_outputs/2018_05_31/ZNuNu_MC/ZJetsToNuNuHT-600To800_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph_v1/ZJetsToNuNuHT-600To800_RunIIFall17MiniAODv2_PU2017_13TeV_MINIAOD_madgraph_v1_copy.root",
	num_folder = "nn_nominal",
	den_folder = "nn_nominal",
	num_tree = "ntuple",
	label = "Z#rightarrow#nu#nu simulation",
	color = "kRed")

Embedding2017Neutrino = pltcl.single_plotline(
	name = "Embedding2017Neutrino",
	num_file = "/storage/c/jbechtel/artus_outputs/2018_05_31/ZNuNu_MC/Embedding2017B_NeutrinoEmbedding.root",
	num_folder = "nn_nominal",
	den_folder = "nn_nominal",
	num_tree = "ntuple",
	label = "#mu#rightarrow#nu embedded",
	color = "kBlue",
	marker = "PE")
	
vtx_corrected_MM = pltcl.single_plotline(
	name = "vtx_corrected_MM",
	num_file = "/portal/ekpcms5/home/akhmet/CMSSW_7_4_7/src/EmbeddingVertexCorrection.root",
	num_folder = "histograms",
	den_folder = "histograms",
	num_tree = "",
	color = "kRed")

DYPrefitShape = pltcl.single_plotline(
	name = "DYPrefitShape",
	num_file = "/portal/ekpbms2/home/jbechtel/analysis/CMSSW_7_4_7/src/CombineHarvester/MSSMFull2016/shapes_160916.root",
	num_folder = "htt_mt_8_13TeV_prefit",
	#den_folder = "input_check",
	num_tree = "ZTT",
	label = "Monte Carlo",
	color = "kRed")
	
EmbeddingPrefitShape = pltcl.single_plotline(
	name = "EmbeddingPrefitShape",
	num_file = "/portal/ekpbms2/home/jbechtel/analysis/CMSSW_7_4_7/src/CombineHarvester/MSSMFull2016/emb/shapes_160916.root",
	num_folder = "htt_mt_8_13TeV_prefit",
	#den_folder = "input_check",
	num_tree = "ZTT",
	label = "Embedding",
	color = "kBlack")
## Embedding and Cleaning Input Check for Muon Embedding

DoubleMuonSelected = pltcl.single_plotline(
	name = "DoubleMuonSelected",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-45_analysis/merged/selected/selected.root",
	num_folder = "input_check",
	den_folder = "input_check",
	num_tree = "ntuple",
	label = "data ",
	color = "kBlack")

DoubleMuonEmbedded = DoubleMuonSelected.clone(
	name = "DoubleMuonEmbedded",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-36_analysis/merged/embedded/embedded.root",
	label = "#mu#rightarrow#mu embedded",
	color = "kRed")

DoubleMuonCleaned = DoubleMuonSelected.clone(
	name = "DoubleMuonCleaned",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-47_analysis/merged/cleaned/cleaned.root",
	label = "data (cleaned)",
	color = "kSpring-9")

DoubleMuonTrackcleaned = DoubleMuonSelected.clone(
	name = "DoubleMuonTrackcleaned",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-48_analysis/merged/trackcleaned/trackcleaned.root",
	label = "data (tracks cleaned)",
	color = "kCyan+3")

DoubleMuonMirrored= DoubleMuonSelected.clone(
	name = "DoubleMuonMirrored",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-46_analysis/merged/mirrored/mirrored.root",
	label = "#splitline{#mu#rightarrow#mu embedded}{w. mirroring}",
	color = "kBlue")

## Z->mumu selection check for Muon Embedding

DoubleMuonSelectedValidation = pltcl.single_plotline(
	name = "DoubleMuonSelectedValidation",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-45_analysis/merged/selected/selected.root",
	num_folder = "zmumu_selection_for_embedding",
	den_folder = "zmumu_selection_for_embedding",
	num_tree = "ntuple",
	label = "data ",
	color = "kBlack")

DoubleMuonEmbeddedValidation = DoubleMuonSelectedValidation.clone(
	name = "DoubleMuonEmbeddedValidation",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-36_analysis/merged/embedded/embedded.root",
	label = "#mu#rightarrow#mu embedded",
	color = "kRed")

DoubleMuonMirroredValidation = DoubleMuonSelectedValidation.clone(
	name = "DoubleMuonMirroredValidation",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-46_analysis/merged/mirrored/mirrored.root",
	label = "#splitline{#mu#rightarrow#mu embedded}{w. mirroring}",
	color = "kBlue")

DoubleMuonFSRrecoMuons = DoubleMuonSelectedValidation.clone(
	name = "DoubleMuonFSRrecoMuons",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-42_analysis/merged/mureco/mureco.root",
	label = "#mu_{reco}",
	color = "kGray+2")

DoubleMuonFSRsimMuons = DoubleMuonSelectedValidation.clone(
	name = "DoubleMuonFSRsimMuons",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-44_analysis/merged/musim/musim.root",
	label = "#mu_{sim}",
	color = "kRed")

DoubleMuonFSRfsrMuons = DoubleMuonSelectedValidation.clone(
	name = "DoubleMuonFSRfsrMuons",
	num_file = "/portal/ekpbms1/home/akhmet/2016-10-11_23-43_analysis/merged/mufsr/mufsr.root",
	label = "#mu_{FSR}",
	color = "kBlue")	

# corresponding pt flow histograms


DoubleMuonSelectedPtFlowHistograms = pltcl.single_plotline(
	name = "DoubleMuonSelectedPtFlowHistograms",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_photon_finebinning_10GeV/selected.root",
	num_folder = "zmumu_selection_for_embedding",
	den_folder = "zmumu_selection_for_embedding",
	num_tree = "",
	label = "data ",
	scale_factor = 1./2450930.,
	color = "kBlack")

DoubleMuonEmbeddedPtFlowHistograms = DoubleMuonSelectedPtFlowHistograms.clone(
	name = "DoubleMuonEmbeddedPtFlowHistograms",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_photon_finebinning_10GeV/embedded.root",
	label = "#mu#rightarrow#mu embedded",
	scale_factor = 1./2408535.,
	color = "kRed")

DoubleMuonMirroredPtFlowHistograms = DoubleMuonSelectedPtFlowHistograms.clone(
	name = "DoubleMuonMirroredPtFlowHistograms",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_photon_finebinning_10GeV/mirrored.root",
	label = "#splitline{#mu#rightarrow#mu embedded}{w. mirroring}",
	scale_factor = 1./2424583.,
	color = "kBlue")

DoubleMuonRandomPtFlowHistograms = DoubleMuonSelectedPtFlowHistograms.clone(
	name = "DoubleMuonMirroredPtFlowHistograms",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_photon_finebinning_10GeV/random.root",
	label = "random direction",
	color = "kGray+2")


DoubleMuonSelectedPtFlowDistribution = pltcl.single_plotline(
	name = "DoubleMuonSelectedPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_firstbin_10GeV/selected.root",
	num_folder = "zmumu_selection_for_embedding",
	den_folder = "zmumu_selection_for_embedding",
	num_tree = "",
	label = "data ",
	scale_factor = 1.,
	color = "kBlack")

DoubleMuonEmbeddedPtFlowDistribution = DoubleMuonSelectedPtFlowDistribution.clone(
	name = "DoubleMuonEmbeddedPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_firstbin_10GeV/embedded.root",
	label = "#mu#rightarrow#mu embedded",
	scale_factor = 1.,
	color = "kRed")

DoubleMuonMirroredPtFlowDistribution = DoubleMuonSelectedPtFlowDistribution.clone(
	name = "DoubleMuonMirroredPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_firstbin_10GeV/mirrored.root",
	label = "#splitline{#mu#rightarrow#mu embedded}{w. mirroring}",
	scale_factor = 1.,
	color = "kBlue")

DoubleMuonRandomPtFlowDistribution = DoubleMuonSelectedPtFlowDistribution.clone(
	name = "DoubleMuonMirroredPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_firstbin_10GeV/random.root", 
	label = "random direction",
	scale_factor = 1.,
	color = "kGray+2")

DoubleMuonSelectedPtFlowDistribution5GeV = pltcl.single_plotline(
	name = "DoubleMuonSelectedPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_firstbin_5GeV/selected.root",
	num_folder = "zmumu_selection_for_embedding",
	den_folder = "zmumu_selection_for_embedding",
	num_tree = "",
	label = "data ",
	scale_factor = 1.,
	color = "kBlack")

DoubleMuonEmbeddedPtFlowDistribution5GeV = DoubleMuonSelectedPtFlowDistribution5GeV.clone(
	name = "DoubleMuonEmbeddedPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_firstbin_5GeV/embedded.root",
	label = "#mu#rightarrow#mu embedded",
	scale_factor = 1.,
	color = "kRed")

DoubleMuonMirroredPtFlowDistribution5GeV = DoubleMuonSelectedPtFlowDistribution5GeV.clone(
	name = "DoubleMuonMirroredPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_firstbin_5GeV/mirrored.root",
	label = "#splitline{#mu#rightarrow#mu embedded}{w. mirroring}",
	scale_factor = 1.,
	color = "kBlue")

DoubleMuonRandomPtFlowDistribution5GeV = DoubleMuonSelectedPtFlowDistribution5GeV.clone(
	name = "DoubleMuonMirroredPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_firstbin_5GeV/random.root", 
	label = "random direction",
	scale_factor = 1.,
	color = "kGray+2")
	
	
DoubleMuonSelectedPtFlowDistributionMid = pltcl.single_plotline(
	name = "DoubleMuonSelectedPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_midbin_10GeV/selected.root",
	num_folder = "zmumu_selection_for_embedding",
	den_folder = "zmumu_selection_for_embedding",
	num_tree = "",
	label = "data ",
	scale_factor = 1.,
	color = "kBlack")

DoubleMuonEmbeddedPtFlowDistributionMid = DoubleMuonSelectedPtFlowDistribution.clone(
	name = "DoubleMuonEmbeddedPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_midbin_10GeV/embedded.root",
	label = "#mu#rightarrow#mu embedded",
	scale_factor = 1.,
	color = "kRed")

DoubleMuonMirroredPtFlowDistributionMid = DoubleMuonSelectedPtFlowDistribution.clone(
	name = "DoubleMuonMirroredPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_midbin_10GeV/mirrored.root",
	label = "#splitline{#mu#rightarrow#mu embedded}{w. mirroring}",
	scale_factor = 1.,
	color = "kBlue")

DoubleMuonRandomPtFlowDistributionMid = DoubleMuonSelectedPtFlowDistribution.clone(
	name = "DoubleMuonMirroredPtFlowDistribution",
	num_file = "/portal/ekpbms2/home/jbechtel/inputfiles_embeddingplots/ptflow_histogram_photon_midbin_10GeV/random.root", 
	label = "random direction",
	scale_factor = 1.,
	color = "kGray+2")


## Tau Embedding Studies

# Acceptance Efficiency 2D

AccEfficiency2D = pltcl.single_plotline(
	name = "AccEfficiency2D",
	num_file = "AccEfficiency.root",
	num_folder = "histograms",
	den_folder = "histograms",
	num_tree = "",
	marker = "COLZ",
	color = None)

NEntries2DMuTau = pltcl.single_plotline(
	name = "NEntries2DMuTau",
	num_file = "MuTauEmbedding.root",
	num_folder = "acc_eff",
	den_folder = "acc_eff",
	num_tree = "",
	scale_factor = 0.001,
	marker = "COLZ",
	color = None)

NEntries2DElTau = NEntries2DMuTau.clone(
	name = "NEntries2DElTau",
	num_file = "ElTauEmbedding.root")

NEntries2DTauTau = NEntries2DMuTau.clone(
	name = "NEntries2DTauTau",
	num_file = "TauTauEmbedding.root")

NEntries2DElMu = NEntries2DMuTau.clone(
	name = "NEntries2DElMu",
	num_file = "ElMuEmbedding.root")


# Acceptance Efficiency distributions

AccEfficiencyMuTauFile = pltcl.single_plotline(
	name = "AccEfficiencyMuTauFile",
	num_file = "MuTauEmbedding.root",
	num_folder = "acc_eff",
	den_folder = "acc_eff",
	num_tree = "ntuple",
	color = "kBlack")

AccEfficiencyElTauFile = AccEfficiencyMuTauFile.clone(
	name = "AccEfficiencyElTauFile",
	num_file = "ElTauEmbedding.root")

AccEfficiencyTauTauFile = AccEfficiencyMuTauFile.clone(
	name = "AccEfficiencyTauTauFile",
	num_file = "TauTauEmbedding.root")

AccEfficiencyElMuFile = AccEfficiencyMuTauFile.clone(
	name = "AccEfficiencyElMuFile",
	num_file = "ElMuEmbedding.root")

# visible Mass comparison

# TTbar files
TTFileMuTauFile = pltcl.single_plotline(
	name = "TTFileMuTauFile",
	scale_factor = 831.76/77229341.*12891.,
	num_file ="/portal/ekpbms1/home/jbechtel/plotting/2017-03-10_01-34_analysis/merged/TT_RunIISummer16MiniAODv2_PUMoriond17_13TeV_MINIAOD_powheg-pythia8/TT_RunIISummer16MiniAODv2_PUMoriond17_13TeV_MINIAOD_powheg-pythia8.root",	#'/storage/a/akhmet/htautau/artus/2017-02-09_00-10_analysis/merged/DYJetsToLLM50_RunIISummer16MiniAODv2_PUMoriond17_13TeV_MINIAOD_madgraph-pythia8_ext1/DYJetsToLLM50_RunIISummer16MiniAODv2_PUMoriond17_13TeV_MINIAOD_madgraph-pythia8_ext1.root',	
	num_folder = "mt_jecUncNom_tauEsNom",
	den_folder = "mt_jecUncNom_tauEsNom",
	num_tree = "ntuple",
	label = "t#bar{t} simulation",
	color = "kMagenta-1",
	marker = "PE")
TTFileTauTauFile = TTFileMuTauFile.clone(
	name = "TTFileMuTauFile",
	num_folder = "tt_jecUncNom_tauEsNom",
	den_folder = "tt_jecUncNom_tauEsNom")
TTFileMuTauFile_17 = pltcl.single_plotline(
	name = "TTFileMuTauFile_17",
	#scale_factor = 831.76/77229341.*12891.,
	num_file ="/storage/9/sbrommer/artus_outputs/2018-03-21/TT_RunIISummer17MiniAOD_92X_13TeV_MINIAOD_powheg-pythia8_ext1-v1/TT_RunIISummer17MiniAOD_92X_13TeV_MINIAOD_powheg-pythia8_ext1-v1.root",
	num_folder = "mt_nominal",
	den_folder = "mt_nominal",
	num_tree = "ntuple",
	label = "t#bar{t} simulation",
	color = "kMagenta-1",
	marker = "PE")
# DYJets files
DYFileMuTauFile = pltcl.single_plotline(
	name = "DYFileMuTauFile",
	#scale_factor = 1./5.234,
	#num_file ="/home/jbechtel/plotting/dySmeared/dySmeared.root",	#'/storage/a/akhmet/htautau/artus/2017-02-09_00-10_analysis/merged/DYJetsToLLM50_RunIISummer16MiniAODv2_PUMoriond17_13TeV_MINIAOD_madgraph-pythia8_ext1/DYJetsToLLM50_RunIISummer16MiniAODv2_PUMoriond17_13TeV_MINIAOD_madgraph-pythia8_ext1.root',
#	num_file = "/storage/9/sbrommer/artus_outputs/comb/DYJets_RunIISummer17MiniAOD_92X_13TeV_MINIAOD_madgraph-pythia8_merged.root",
	#~ num_folder = "mt_jecUncNom_tauEsNom",
	#~ den_folder = "mt_jecUncNom_tauEsNom",	
	num_file = "/storage/9/sbrommer/artus_outputs/2018-03-21/DYMerge.root",
	num_folder = "mt_nominal",
	den_folder = "mt_nominal",
	num_tree = "ntuple",
	label = "Z#rightarrow#tau#tau simulation",
	color = "kGreen",
	marker = "HISTO")

DYFileMuTauSmeared = DYFileMuTauFile.clone(
	name = "DYFileMuTauSmeared",
	#scale_factor = 1./1.7122,
	num_folder = "mt_ZDecayProductsSmeared",
	den_folder = "mt_ZDecayProductsSmeared",
	color = "kMagenta",
	label = "Z#rightarrow#tau#tau SMEARED",
	marker = "LINE"
)
DYFileElTauFile = DYFileMuTauFile.clone(
	name = "DYFileElTauFile",
	#scale_factor = 1./1.7122,
	num_folder = "et_nominal",
	den_folder = "et_nominal"
)

DYFileTauTauFile = DYFileMuTauFile.clone(
	name = "DYFileTauTauFile",
	#scale_factor = 1./0.273551,
	num_folder = "tt_jecUncNom_tauEsNom",
	den_folder = "tt_jecUncNom_tauEsNom"
)

DYFileElMuFile = DYFileMuTauFile.clone(
	name = "DYFileElMuFile",
	#scale_factor = 1./0.887674,
	num_folder = "em_jecUncNom",
	den_folder = "em_jecUncNom"
)
# DYISOJets files ISO
DYISOFileMuTauFile = pltcl.single_plotline(
	name = "DYFileMuTauFile",
	#scale_factor = 1./5.234,
	num_file = "/home/jbechtel/MVAcheck/DYToLLMCRunIISummer16DR80_AllFinalState_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_unspecified/DYToLLMCRunIISummer16DR80_AllFinalState_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_unspecified.root",
	num_folder = "mt_jecUncNom_tauEsNom",
	den_folder = "mt_jecUncNom_tauEsNom",
	num_tree = "ntuple",
	label = "Z#rightarrow#tau#tau simulation",
	color = "kRed",
	marker = "PE")

DYISOFileElTauFile = DYFileMuTauFile.clone(
	name = "DYFileElTauFile",
	#scale_factor = 1./1.7122,
	num_folder = "et_jecUncNom_tauEsNom",
	den_folder = "et_jecUncNom_tauEsNom"
)

DYISOFileTauTauFile = DYFileMuTauFile.clone(
	name = "DYFileTauTauFile",
	#scale_factor = 1./0.273551,
	num_folder = "tt_jecUncNom_tauEsNom",
	den_folder = "tt_jecUncNom_tauEsNom"
)

DYISOFileElMuFile = DYFileMuTauFile.clone(
	name = "DYFileElMuFile",
	#scale_factor = 1./0.887674,
	num_folder = "em_jecUncNom",
	den_folder = "em_jecUncNom"
)

# DiBoson files
VVFileMuTauFile = pltcl.single_plotline(
	name = "VVFileMuTauFile",
	#scale_factor = 1./5.234,
	num_file = "/home/jbechtel/MVAcheck/VVTo2L2Nu_RunIISummer16MiniAODv2_PUMoriond17_13TeV_MINIAOD_amcatnlo-pythia8/VVTo2L2Nu_RunIISummer16MiniAODv2_PUMoriond17_13TeV_MINIAOD_amcatnlo-pythia8.root",
	num_folder = "mt_jecUncNom_tauEsNom",
	den_folder = "mt_jecUncNom_tauEsNom",
	num_tree = "ntuple",
	label = "VV #rightarrow ll simulation",
	color = "kGreen",
	marker = "PE")

VVFileElTauFile = VVFileMuTauFile.clone(
	name = "VVFileElTauFile",
	#scale_factor = 1./1.7122,
	num_folder = "et_jecUncNom_tauEsNom",
	den_folder = "et_jecUncNom_tauEsNom"
)

VVFileTauTauFile = VVFileMuTauFile.clone(
	name = "VVFileTauTauFile",
	#scale_factor = 1./0.273551,
	num_folder = "tt_jecUncNom_tauEsNom",
	den_folder = "tt_jecUncNom_tauEsNom"
)

VVFileElMuFile = VVFileMuTauFile.clone(
	name = "VVFileElMuFile",
	#scale_factor = 1./0.887674,
	num_folder = "em_jecUncNom",
	den_folder = "em_jecUncNom"
)


# HToTauTau samples

HToTauTauMuTauFile = pltcl.single_plotline(
	name = "HToTauTauMuTauFile",
	scale_factor = 1./0.767714,
	num_file = "/portal/ekpbms1/home/akhmet/htautau_signal/*HToTauTauM125*.root",
	num_folder = "mt",
	den_folder = "mt",
	num_tree = "ntuple",
	label = "H(125)",
	color = "kBlack")

HToTauTauElTauFile = HToTauTauMuTauFile.clone(
	name = "HToTauTauElTauFile",
	scale_factor = 1./0.356839,
	num_folder = "et",
	den_folder = "et"
)

HToTauTauTauTauFile = HToTauTauMuTauFile.clone(
	name = "HToTauTauTauTauFile",
	scale_factor = 1./0.25,
	num_folder = "tt",
	den_folder = "tt"
)

HToTauTauElMuFile = HToTauTauMuTauFile.clone(
	name = "HToTauTauElMuFile",
	scale_factor = 1./0.164191,
	num_folder = "em",
	den_folder = "em"
)

#Embedding files for MuTau

EmbeddingMuTauFileNominal = DYFileMuTauFile.clone(
	name = "EmbeddingMuTauFileNominal",
<<<<<<< Updated upstream
	scale_factor = 1.04277308792,
	num_file = '/portal/ekpbms1/home/jbechtel/plotting/EmbeddingMETtest/EmbeddingMuTau.root',
	#num_file = "/home/jbechtel/plotting/0226/EmbeddingMCRunIISummer16DR80_MuTauFinalState_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_pythia8/EmbeddingMCRunIISummer16DR80_MuTauFinalState_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_pythia8.root",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue"
=======
	num_file = '/storage/c/jbechtel/Artus_2018-03-27/Embedding2016B_MuTauFinalState_imputSep16DoubleMumirrorminiAODv2_13TeV_USER/Embedding2016B_MuTauFinalState_imputSep16DoubleMumirrorminiAODv2_13TeV_USER.root',
	label = "#mu#rightarrow#tau embedded 2016",
	color = "kBlue"
)
EmbeddingMuTauFileNominal2017 = EmbeddingMuTauFileNominal.clone(
	name = "EmbeddingMuTauFileNominal2017",
	num_file = '/storage/c/jbechtel/Artus_2018-03-28/Embedding2017B_MuTauFinalState_imputDoubleMuminiAODv2_13TeV_USER/Embedding2017B_MuTauFinalState_imputDoubleMuminiAODv2_13TeV_USER.root',
	label = "#mu#rightarrow#tau embedded 2017",
	color = "kCyan"
)
EmbeddingMuTauFileNominal_all = DYFileMuTauFile.clone(
	name = "EmbeddingMuTauFileNominal_all",
	num_file = '/storage/9/sbrommer/artus_outputs/Embedding_combine/Embedding_2016_MuTauFinalState_combined.root',
	label = "#mu#rightarrow#tau embedded 2016",
	color = "kRed",
	marker = "HISTO"
)
EmbeddingMuTauFileNominal2017_all = EmbeddingMuTauFileNominal_all.clone(
	name = "EmbeddingMuTauFileNominal2017",
	num_file = '/storage/9/sbrommer/artus_outputs/comb/Embedding_2017_MuTauFinalState_combined.root',
	label = "#mu#rightarrow#tau embedded 2017",
	color = "kBlue",
	marker = "PE"
)
EmbeddingMuTauFileNominal2017v2_all = EmbeddingMuTauFileNominal_all.clone(
	name = "EmbeddingMuTauFileNominal2017v2",
	num_file = '/storage/9/sbrommer/artus_outputs/comb/Embedded_MuTau_B_D_E_merge.root',
	label = "#mu#rightarrow#tau embedded 2017",
	color = "kBlue",
	marker = "PE"
>>>>>>> Stashed changes
)

EmbeddingMuTauFileUp = EmbeddingMuTauFileNominal.clone(
	name = "EmbeddingMuTauFileUp",
	num_folder = "mt_jecUncNom_tauEsUp",
	den_folder = "mt_jecUncNom_tauEsUp",
	label = "w. #pm3% #tau_{h}-ES shifts",
	color = "kCyan+2",
	marker = "HISTO"
)

EmbeddingMuTauFileDown = EmbeddingMuTauFileNominal.clone(
	name = "EmbeddingMuTauFileDown",
	num_folder = "mt_jecUncNom_tauEsDown",
	den_folder = "mt_jecUncNom_tauEsDown",
	label = "",
	color = "kCyan+2",
	marker = "HISTO"
)


EmbeddingMuTauFileNominalMirrored = DYFileMuTauFile.clone(
	name = "EmbeddingMuTauFileNominalMirrored",
	#scale_factor = 1.62724193802,
	num_file = '/portal/ekpbms1/home/jbechtel/plotting/mirrored/RUNC/Embedding2016C_MuTauFinalState_imputSep16DoubleMumirrorminiAODv2_13TeV_USER/Embedding2016C_MuTauFinalState_imputSep16DoubleMumirrorminiAODv2_13TeV_USER.root',
	#num_file = "/home/jbechtel/plotting/0226/EmbeddingMCRunIISummer16DR80_MuTauFinalState_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_pythia8/EmbeddingMCRunIISummer16DR80_MuTauFinalState_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_pythia8.root",
	label = "#mu#rightarrow#tau emb mirrored",
	color = "kGreen"
)

EmbeddingMuTauFileUpMirrored = EmbeddingMuTauFileNominal.clone(
	name = "EmbeddingMuTauFileUpMirrored",
	num_folder = "mt_jecUncNom_tauEsUp",
	den_folder = "mt_jecUncNom_tauEsUp",
	label = "w. #pm3% #tau_{h}-ES shifts",
	color = "kCyan+2",
	marker = "HISTO"
)

EmbeddingMuTauFileDownMirrored = EmbeddingMuTauFileNominal.clone(
	name = "EmbeddingMuTauFileDownMirrored",
	num_folder = "mt_jecUncNom_tauEsDown",
	den_folder = "mt_jecUncNom_tauEsDown",
	label = "",
	color = "kCyan+2",
	marker = "HISTO"
)

#Embedding files for ElTau

EmbeddingElTauFileNominal = DYFileElTauFile.clone(
	name = "EmbeddingElTauFileNominal",
	scale_factor=1.00421186517,
	num_file ="/home/jbechtel/plotting/Jun17_EmbeddingFiles/EmbeddingElTau.root",	#'/storage/a/akhmet/htautau/artus/2017-02-09_00-10_analysis/merged/Embedding2016B_ElTauFinalState_imputSep16DoubleMumirrorminiAODv1_13TeV_USER/Embedding2016B_ElTauFinalState_imputSep16DoubleMumirrorminiAODv1_13TeV_USER.root',
	#num_file = "/home/jbechtel/plotting/output.root",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue"
)

EmbeddingElTauFileUp = EmbeddingElTauFileNominal.clone(
	name = "EmbeddingElTauFileUp",
	num_folder = "et_jecUncNom_tauEsUp",
	den_folder = "et_jecUncNom_tauEsUp",
	label = "w. #pm3% #tau_{h}-ES shifts",
	color = "kCyan+2"
)

EmbeddingElTauFileDown = EmbeddingElTauFileNominal.clone(
	name = "EmbeddingElTauFileDown",
	num_folder = "et_jecUncNom_tauEsDown",
	den_folder = "et_jecUncNom_tauEsDown",
	label = "",
	color = "kCyan+2"
)

#Embedding files for TauTau

EmbeddingTauTauFileNominal = DYFileTauTauFile.clone(
	scale_factor = 1./0.33,
	name = "EmbeddingTauTauFileNominal",
	num_file = "/home/jbechtel/plotting/tautau_controlplots/EmbeddingBCD.root",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue"
)

EmbeddingTauTauFileUp = EmbeddingTauTauFileNominal.clone(
	name = "EmbeddingTauTauFileUp",
	num_folder = "tt_jecUncNom_tauEsUp",
	den_folder = "tt_jecUncNom_tauEsUp",
	label = "w. #pm3% #tau_{h}-ES shifts",
	color = "kCyan+2"
)

EmbeddingTauTauFileDown = EmbeddingTauTauFileNominal.clone(
	name = "EmbeddingTauTauFileDown",
	num_folder = "tt_jecUncNom_tauEsDown",
	den_folder = "tt_jecUncNom_tauEsDown",
	label = "",
	color = "kCyan+2"
)

#Embedding files for ElMu

EmbeddingElMuFileNominal = DYFileElMuFile.clone(
	name = "EmbeddingElMuFileNominal",
	num_file = "/portal/ekpbms1/home/akhmet/elmuembedding/*.root",
	num_folder = "em_eleEsNom",
	den_folder = "em_eleEsNom",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue"
)

EmbeddingElMuFileUp = EmbeddingElMuFileNominal.clone(
	name = "EmbeddingElMuFileUp",
	num_folder = "em_eleEsUp",
	den_folder = "em_eleEsUp",
	label = "w. #pm2% e-ES shifts",
	color = "kCyan+2"
)

EmbeddingElMuFileDown = EmbeddingElMuFileNominal.clone(
	name = "EmbeddingElMuFileDown",
	num_folder = "em_eleEsDown",
	den_folder = "em_eleEsDown",
	label = "",
	color = "kCyan+2"
)

#EmbeddingISO files for MuTau including Iso_2 MVA Variables

EmbeddingISOMuTauFileNominal = DYFileMuTauFile.clone(
	#scale_factor = 1./4.32414,
	name = "EmbeddingMuTauFileNominal",
	num_file = "/home/jbechtel/MVAcheck/EmbeddingMCRunIISummer16DR80_MuTauFinalState_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_pythia8/EmbeddingMCRunIISummer16DR80_MuTauFinalState_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_pythia8.root",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue"
)

EmbeddingISOMuTauFileUp = EmbeddingMuTauFileNominal.clone(
	name = "EmbeddingMuTauFileUp",
	num_folder = "mt_jecUncNom_tauEsUp",
	den_folder = "mt_jecUncNom_tauEsUp",
	label = "w. #pm3% #tau_{h}-ES shifts",
	color = "kCyan+2"
)

EmbeddingISOMuTauFileDown = EmbeddingMuTauFileNominal.clone(
	name = "EmbeddingMuTauFileDown",
	num_folder = "mt_jecUncNom_tauEsDown",
	den_folder = "mt_jecUncNom_tauEsDown",
	label = "",
	color = "kCyan+2"
)


#EmbeddingISO files for ElTau including Iso_2 MVA Variables

EmbeddingISOElTauFileNominal = DYFileElTauFile.clone(
	name = "EmbeddingISOElTauFileNominal",
	num_file = "/storage/a/jbechtel/test/merged/merged/EmbeddingISO2016?_ElTau*/*.root",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue"
)

EmbeddingISOElTauFileUp = EmbeddingISOElTauFileNominal.clone(
	name = "EmbeddingISOElTauFileUp",
	num_folder = "et_jecUncNom_tauEsUp",
	den_folder = "et_jecUncNom_tauEsUp",
	label = "w. #pm3% #tau_{h}-ES shifts",
	color = "kCyan+2"
)

EmbeddingISOElTauFileDown = EmbeddingISOElTauFileNominal.clone(
	name = "EmbeddingISOElTauFileDown",
	num_folder = "et_jecUncNom_tauEsDown",
	den_folder = "et_jecUncNom_tauEsDown",
	label = "",
	color = "kCyan+2"
)

#EmbeddingISO files for TauTau including Iso_2 MVA Variables

EmbeddingISOTauTauFileNominal = DYFileTauTauFile.clone(
	scale_factor = 1./0.220103,
	name = "EmbeddingISOTauTauFileNominal",
	num_file = "/storage/a/jbechtel/janek/EmbeddingISO2016?_TauTau*/*.root",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue"
)

EmbeddingISOTauTauFileUp = EmbeddingISOTauTauFileNominal.clone(
	name = "EmbeddingISOTauTauFileUp",
	num_folder = "tt_jecUncNom_tauEsUp",
	den_folder = "tt_jecUncNom_tauEsUp",
	label = "w. #pm3% #tau_{h}-ES shifts",
	color = "kCyan+2"
)

EmbeddingISOTauTauFileDown = EmbeddingISOTauTauFileNominal.clone(
	name = "EmbeddingISOTauTauFileDown",
	num_folder = "tt_jecUncNom_tauEsDown",
	den_folder = "tt_jecUncNom_tauEsDown",
	label = "",
	color = "kCyan+2"
)

#EmbeddingISO files for ElMu including Iso_2 MVA Variables

EmbeddingISOElMuFileNominal = DYFileElMuFile.clone(
	scale_factor = 1./1.58934,
	name = "EmbeddingISOElMuFileNominal",
	num_file = "/portal/ekpbms1/home/akhmet/elmuEmbeddingISO/*.root",
	num_folder = "em_eleEsNom",
	den_folder = "em_eleEsNom",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue"
)

EmbeddingISOElMuFileUp = EmbeddingISOElMuFileNominal.clone(
	name = "EmbeddingISOElMuFileUp",
	num_folder = "em_eleEsUp",
	den_folder = "em_eleEsUp",
	label = "w. #pm2% e-ES shifts",
	color = "kCyan+2"
)

EmbeddingISOElMuFileDown = EmbeddingISOElMuFileNominal.clone(
	name = "EmbeddingISOElMuFileDown",
	num_folder = "em_eleEsDown",
	den_folder = "em_eleEsDown",
	label = "",
	color = "kCyan+2"
)


## Decay channel migration

#MuTau -> X
EmbeddingMuTauIntegralMuTauFile = pltcl.single_plotline(
	name = "EmbeddingMuTauIntegralMuTauFile",
	num_file = "/storage/a/jbechtel/test/merged/merged/Embedding2016?_MuTau*/*.root",
	num_folder = "mt_jecUncNom_tauEsNom",
	den_folder = "mt_jecUncNom_tauEsNom",
	num_tree = "ntuple")
	
EmbeddingMuTauIntegralElTauFile = EmbeddingMuTauIntegralMuTauFile.clone(
	name = "EmbeddingMuTauIntegralElTauFile",
	num_folder = "et_jecUncNom_tauEsNom",
	den_folder = "et_jecUncNom_tauEsNom")

EmbeddingMuTauIntegralTauTauFile = EmbeddingMuTauIntegralMuTauFile.clone(
	name = "EmbeddingMuTauIntegralTauTauFile",
	num_folder = "tt_jecUncNom_tauEsNom",
	den_folder = "tt_jecUncNom_tauEsNom")

EmbeddingMuTauIntegralElMuFile = EmbeddingMuTauIntegralMuTauFile.clone(
	name = "EmbeddingMuTauIntegralElMuFile",
	num_folder = "em_jecUncNom",
	den_folder = "em_jecUncNom")

#ElTau -> X

EmbeddingElTauIntegralElTauFile = pltcl.single_plotline(
	name = "EmbeddingElTauIntegralElTauFile",
	num_file = "/storage/a/jbechtel/test/merged/merged/Embedding2016?_ElTau*/*.root",
	num_folder = "et_jecUncNom_tauEsNom",
	den_folder = "et_jecUncNom_tauEsNom",
	num_tree = "ntuple")

EmbeddingElTauIntegralElMuFile = EmbeddingElTauIntegralElTauFile.clone(
	name = "EmbeddingElTauIntegralElMuFile",
	num_folder = "em_jecUncNom",
	den_folder = "em_jecUncNom")

EmbeddingElTauIntegralMuTauFile = EmbeddingElTauIntegralElTauFile.clone(
	name = "EmbeddingElTauIntegralMuTauFile",
	num_folder = "mt_jecUncNom_tauEsNom",
	den_folder = "mt_jecUncNom_tauEsNom")

EmbeddingElTauIntegralTauTauFile = EmbeddingElTauIntegralElTauFile.clone(
	name = "EmbeddingElTauIntegralTauTauFile",
	num_folder = "tt_jecUncNom_tauEsNom",
	den_folder = "tt_jecUncNom_tauEsNom")
	

#TauTau -> X

EmbeddingTauTauIntegralTauTauFile = pltcl.single_plotline(
	name = "EmbeddingTauTauIntegralTauTauFile",
	num_file = "/storage/a/jbechtel/test/merged/merged/Embedding2016?_TauTau*/*.root",
	num_folder = "tt_jecUncNom_tauEsNom",
	den_folder = "tt_jecUncNom_tauEsNom",
	num_tree = "ntuple")

EmbeddingTauTauIntegralMuTauFile = EmbeddingTauTauIntegralTauTauFile.clone(
	name = "EmbeddingTauTauIntegralMuTauFile",
	num_folder = "mt_jecUncNom_tauEsNom",
	den_folder = "mt_jecUncNom_tauEsNom")

EmbeddingTauTauIntegralElTauFile = EmbeddingTauTauIntegralTauTauFile.clone(
	name = "EmbeddingTauTauIntegralElTauFile",
	num_folder = "et_jecUncNom_tauEsNom",
	den_folder = "et_jecUncNom_tauEsNom")

EmbeddingTauTauIntegralElMuFile = EmbeddingTauTauIntegralTauTauFile.clone(
	name = "EmbeddingTauTauIntegralElMuFile",
	num_folder = "em_jecUncNom",
	den_folder = "em_jecUncNom")

#ElMu -> X

EmbeddingElMuIntegralElMuFile = pltcl.single_plotline(
	name = "EmbeddingElMuIntegralElMuFile",
	num_file = "/storage/a/jbechtel/test/merged/merged/Embedding2016?_ElMu*/*.root",
	num_folder = "em_jecUncNom",
	den_folder = "em_jecUncNom",
	num_tree = "ntuple")

EmbeddingElMuIntegralMuTauFile = EmbeddingElMuIntegralElMuFile.clone(
	name = "EmbeddingElMuIntegralMuTauFile",
	num_folder = "mt_jecUncNom_tauEsNom",
	den_folder = "mt_jecUncNom_tauEsNom")

EmbeddingElMuIntegralElTauFile = EmbeddingElMuIntegralElMuFile.clone(
	name = "EmbeddingElMuIntegralElTauFile",
	num_folder = "et_jecUncNom_tauEsNom",
	den_folder = "et_jecUncNom_tauEsNom")

EmbeddingElMuIntegralTauTauFile = EmbeddingElMuIntegralElTauFile.clone(
	name = "EmbeddingElMuIntegralTauTauFile",
	num_folder = "tt_jecUncNom_tauEsNom",
	den_folder = "tt_jecUncNom_tauEsNom")

DYFileMuMu_17 = pltcl.single_plotline(
	name = "DYFileMuMu_17",
	num_file = "/storage/b/pahrens/artus_files/DYJetsToLLM50_PhaseISpring17DR_FlatPU28to62HcalNZS_13TeV_MINIAODSIM_madgraph-pythia8_v1/merged/DYJetsToLLM50_PhaseISpring17DR_FlatPU28to62HcalNZS_13TeV_MINIAODSIM_madgraph-pythia8/DYJetsToLLM50_PhaseISpring17DR_FlatPU28to62HcalNZS_13TeV_MINIAODSIM_madgraph-pythia8.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	num_tree = "ntuple",
	label = "DY Sample",
	marker = "HISTO")

DYFileEE_17 = pltcl.single_plotline(
	name = "DYFileEE_17",
	num_file = "/storage/c/jbechtel/artus_outputs/2018_06_24/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "ee_nominal",
	den_folder = "ee_nominal",
	num_tree = "ntuple",
	label = "",
	marker = "HISTO",
	color = "kRed")
DYFileEE_17Upshift = pltcl.single_plotline(
	name = "DYFileEE_17Upshift",
	num_file = "/storage/c/jbechtel/artus_outputs/EleID/mc/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3_shifts.root",
	num_folder = "ee_eleEsUp1",
	den_folder = "ee_eleEsUp1",
	num_tree = "ntuple",
	label = "#pm 1% electron energy scale shifts",
	marker = "HISTO",
	color = "kOrange+7")
DYFileEE_17Downshift = pltcl.single_plotline(
	name = "DYFileEE_17Downshift",
	num_file = "/storage/c/jbechtel/artus_outputs/EleID/mc/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3_shifts.root",
	num_folder = "ee_eleEsDown1",
	den_folder = "ee_eleEsDown1",
	num_tree = "ntuple",
	label = "",
	marker = "HISTO",
	color = "kOrange+7")
DYFileEE_17_copy = pltcl.single_plotline(
	name = "DYFileEE_17_copy",
	num_file = "/storage/c/jbechtel/artus_outputs/2018_06_24/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3_copy.root",
	num_folder = "ee_nominal",
	den_folder = "ee_nominal",
	num_tree = "ntuple",
	label = "Z #rightarrow ee (simulation)",
	marker = "HISTO",
	color = "kRed")

EmbFileMuMu_17 = pltcl.single_plotline(
	name = "EmbFileMuMu_17",
	num_file = "/storage/b/pahrens/artus_files/EmbeddingMCPhaseISpring17DR_MuonEmbedding_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_pythia8_HybridEmbedding_v6_full/merged/EmbeddingMCPhaseISpring17DR_MuonEmbedding_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_pythia8/EmbeddingMCPhaseISpring17DR_MuonEmbedding_imputFlatPU28to62HcalNZSRAWAODSIM_13TeV_USER_pythia8.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	num_tree = "ntuple",
	label = "#mu#rightarrow#mu embedded selection 2017",
	color = "kBlue",
	marker = "PE")

EmbFileEE_17 = pltcl.single_plotline(
	name = "EmbFileEE_17",
	num_file = "/storage/c/jbechtel/artus_outputs/2018_06_24/EmbeddingMCRunIIWinter17_ElectronEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_folder = "ee_nominal",
	den_folder = "ee_nominal",
	num_tree = "ntuple",
	label = "Z #rightarrow ee (embedded)",
	color = "kBlue",
	marker = "PE")

##### MC Shape Comparison

DYFileWinter17_mt = pltcl.single_plotline(
	name = "DYFileWinter17_mt",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "mt_nominal",
	den_folder = "mt_nominal",
	num_tree = "ntuple",
	label = "Z#rightarrow#tau#tau simulation",
	color = "kRed",
	marker = "HISTO")

DYFileWinter17_mt_copy = pltcl.single_plotline(
	name = "DYFileWinter17_mt_copy",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/9/sbrommer/artus_outputs/ZmmValidation/DYJets_copy.root",
	num_folder = "mt_nominal",
	den_folder = "mt_nominal",
	label = "Simulation uncertainty",

	num_tree = "ntuple")

DYFileWinter17_mt_shift_up = pltcl.single_plotline(
	name = "DYFileWinter17_mt_shift_up",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "mt_tauEsUp",
	den_folder = "mt_tauEsUp",
	num_tree = "ntuple",
	label = "#pm 1.2% #tau_{h} energy scale",
	color = "kCyan+1",
	marker = "HISTO")

DYFileWinter17_mt_shift_down = pltcl.single_plotline(
	name = "DYFileWinter17_mt_shift_down",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "mt_tauEsDown",
	den_folder = "mt_tauEsDown",
	num_tree = "ntuple",
	label = "",
	color = "kCyan+1",
	marker = "HISTO")

DYFileWinter17_emb_mt = pltcl.single_plotline(
	name = "DYFileWinter17_emb_mt",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/EmbeddingMCRunIIWinter17_MuTauFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_MuTauFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/EmbeddingMCRunIIWinter17_MuTauFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_folder = "mt_nominal",
	den_folder = "mt_nominal",
	num_tree = "ntuple",
	label = "#mu #rightarrow #tau embedded",
	color = "kBlue",
	marker = "PE")

DYFileWinter17_mm = pltcl.single_plotline(
	name = "DYFileWinter17_mm",
#	num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file= "/storage/c/jbechtel/artus_outputs/event_matching/final/chargeOrdered/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	num_tree = "ntuple",
	color = "kRed",
	label = "Z#rightarrow#mu#mu simulation",
	marker = "HISTO")

DYFileWinter17_mm_copy = pltcl.single_plotline(
	name = "DYFileWinter17_mm_copy",
#	num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file= "/portal/ekpbms1/home/jbechtel/copy_temp_reg.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	label = "Simulation uncertainty",
	num_tree = "ntuple")

DYFileWinter17_emb_mm = pltcl.single_plotline(
	name = "DYFileWinter17_emb_mm",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	#num_file = "/storage/c/jbechtel/Artus_2018-04-26/EmbeddingMC_MuonEmbedding2/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8_newweightfile.root",
	num_file = "/storage/c/jbechtel/artus_outputs/event_matching/final/chargeOrdered/corr11/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	num_tree = "ntuple",
	label = "#mu#rightarrow#mu embedded",
	color = "kBlue",
	marker = "PE")
#### Mass Correction Files#####
DYFileWinter17_mm_corr = pltcl.single_plotline(
	name = "DYFileWinter17_mm_corr",
#	num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file= "/storage/c/jbechtel/Artus_2018-04-26/EmbeddingMC_MuonEmbedding2/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	num_tree = "ntuple",
	color = "kRed",
	label = "Z#rightarrow#mu#mu simulation",
	marker = "HISTO")

DYFileWinter17_mm_corr_copy = pltcl.single_plotline(
	name = "DYFileWinter17_mm_corr_copy",
#	num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file= "/storage/9/sbrommer/artus_outputs/ZmmValidation/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3_mass_corr_copy.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	label = "Simulation uncertainty",

	num_tree = "ntuple")

DYFileWinter17_emb_mm_uncorr = pltcl.single_plotline(
	name = "DYFileWinter17_emb_mm_uncorr",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	#num_file = "/storage/c/jbechtel/Artus_2018-04-26/EmbeddingMC_MuonEmbedding2/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8_newweightfile.root",
	num_file = "/storage/c/jbechtel/artus_outputs/event_matching/ptflow/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8_UNCORRECTED.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	num_tree = "ntuple",
	label = "#mu#rightarrow#mu embedded (uncorrected)",
	color = "kGreen+1 kWhite",
	marker = "HISTO")
	
DYFileWinter17_mm_met = pltcl.single_plotline(
	name = "DYFileWinter17_mm_met",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	#num_file = "/storage/c/jbechtel/Artus_2018-04-26/EmbeddingMC_MuonEmbedding2/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8_newweightfile.root",
	num_file = "/portal/ekpbms2/home/jbechtel/analysis/CMSSW_7_4_7/src/eventmatching_met2.root",
	num_folder = "",
	den_folder = "",
	num_tree = "common2",
	label = "Z#rightarrow#mu#mu simulation",
	color = "kRed kWhite",
	marker = "HISTO")

DYFileWinter17_mm_met_copy = pltcl.single_plotline(
	name = "DYFileWinter17_mm_met_copy",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	#num_file = "/storage/c/jbechtel/Artus_2018-04-26/EmbeddingMC_MuonEmbedding2/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8_newweightfile.root",
	num_file = "/portal/ekpbms2/home/jbechtel/analysis/CMSSW_7_4_7/src/eventmatching_met2COPY.root",
	num_folder = "",
	den_folder = "",
	num_tree = "common2",
	label = "Simulation Uncertainty",
	color = "kRed kWhite",
	marker = "HISTO")

DYFileWinter17_emb_mm_met = pltcl.single_plotline(
	name = "DYFileWinter17_emb_mm_met",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	#num_file = "/storage/c/jbechtel/Artus_2018-04-26/EmbeddingMC_MuonEmbedding2/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8_newweightfile.root",
	num_file = "/portal/ekpbms2/home/jbechtel/analysis/CMSSW_7_4_7/src/eventmatching_met2.root",
	num_folder = "",
	den_folder = "",
	num_tree = "common3",
	label = "#mu#rightarrow#mu embedded",
	color = "kBlue",
	marker = "PE")
DYFileWinter17_emb_mm_metcorr = pltcl.single_plotline(
	name = "DYFileWinter17_emb_mm_metcorr",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-04-23/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	#num_file = "/storage/c/jbechtel/Artus_2018-04-26/EmbeddingMC_MuonEmbedding2/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8_newweightfile.root",
	num_file = "/portal/ekpbms2/home/jbechtel/analysis/CMSSW_7_4_7/src/eventmatching_met2.root",
	num_folder = "",
	den_folder = "",
	num_tree = "common1",
	label = "#mu#rightarrow#mu embedded (met corr)",
	color = "kGreen+1 kWhite",
	marker = "HISTO")
	
DYFileWinter17_mm_pf = pltcl.single_plotline(
	name = "DYFileWinter17_mm_pf",
	num_file = "/storage/c/jbechtel/artus_outputs/event_matching/ptflow/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	num_tree = "ntuple",
	color = "kRed",
	label = "Z#rightarrow#mu#mu simulation",
	marker = "HISTO")

DYFileWinter17_mm_pf_copy = pltcl.single_plotline(
	name = "DYFileWinter17_mm_pf_copy",
	num_file = "/storage/c/jbechtel/artus_outputs/event_matching/ptflow/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3COPY.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	label = "Simulation uncertainty",

	num_tree = "ntuple")
DYFileWinter17_nunu_pf = pltcl.single_plotline(
	name = "DYFileWinter17_nunu_pf",
	num_file = "/portal/ekpbms2/home/jbechtel/analysis/CMSSW_7_4_7/src/eventmatching.root",
	num_folder = "",
	den_folder = "",
	num_tree = "common1",
	color = "kRed",
	label = "Z#rightarrow#mu#mu simulation",
	marker = "HISTO")

DYFileWinter17_nunu_pf_copy = pltcl.single_plotline(
	name = "DYFileWinter17_nunu_pf_copy",
	num_file = "/portal/ekpbms2/home/jbechtel/analysis/CMSSW_7_4_7/src/eventmatching2.root",
	num_folder = "",
	den_folder = "",
	num_tree = "common1",
	label = "Simulation uncertainty")


DYFileWinter17_emb_nunu_pf = pltcl.single_plotline(
	name = "DYFileWinter17_emb_nunu_pf",
	num_file = "/portal/ekpbms2/home/jbechtel/analysis/CMSSW_7_4_7/src/eventmatching.root",
	num_folder = "",
	den_folder = "",
	num_tree = "common2",
	label = "#mu#rightarrow#nu embedded",
	color = "kBlue",
	marker = "PE")

DYFileWinter17_emb_mm_pf = pltcl.single_plotline(
	name = "DYFileWinter17_emb_mm_pf",
	num_file = "/storage/c/jbechtel/artus_outputs/event_matching/ptflow/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	num_tree = "ntuple",
	label = "#mu#rightarrow#mu embedded",
	color = "kBlue",
	marker = "PE")

DYFileWinter17_emb_mm_pf = pltcl.single_plotline(
	name = "DYFileWinter17_emb_mm_pf",
	num_file = "/storage/c/jbechtel/artus_outputs/2018-05-08/9/EmbeddingMCRunIIWinter17_MuonEmbedding_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_folder = "mm_nominal",
	den_folder = "mm_nominal",
	num_tree = "ntuple",
	label = "#mu#rightarrow#mu embedded",
	color = "kBlue",
	marker = "PE")

DYFileWinter17_tt = pltcl.single_plotline(
	name = "DYFileWinter17_tt",
	#num_file= "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",	
	num_folder = "tt_nominal",
	den_folder = "tt_nominal",
	num_tree = "ntuple",
	color = "kRed",
	label = "Z#rightarrow#tau#tau simulation",
	marker = "HISTO")

DYFileWinter17_tt_copy = pltcl.single_plotline(
	name = "DYFileWinter17_tt_copy",
	#num_file= "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/9/sbrommer/artus_outputs/ZmmValidation/DYJets_copy.root",	
	num_folder = "tt_nominal",
	den_folder = "tt_nominal",
	label = "Simulation uncertainty",

	num_tree = "ntuple")

DYFileWinter17_tt_shift_up = pltcl.single_plotline(
	name = "DYFileWinter17_tt_shift_up",
	#num_file= "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",	
	num_folder = "tt_tauEsUp",
	den_folder = "tt_tauEsUp",
	num_tree = "ntuple",
	color = "kRed",
	label = "#pm 1.2% #tau_{h} energy scale",
	marker = "HISTO")

DYFileWinter17_tt_shift_down = pltcl.single_plotline(
	name = "DYFileWinter17_tt_shift_down",
	#num_file= "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",	
	num_folder = "tt_tauEsDown",
	den_folder = "tt_tauEsDown",
	num_tree = "ntuple",
	color = "kRed",
	label = "",
	marker = "HISTO")

DYFileWinter17_emb_tt = pltcl.single_plotline(
	name = "DYFileWinter17_emb_tt",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/EmbeddingMCRunIIWinter17_TauTauFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_TauTauFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/EmbeddingMCRunIIWinter17_TauTauFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_folder = "tt_nominal",
	den_folder = "tt_nominal",
	num_tree = "ntuple",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue",
	marker = "PE")

DYFileWinter17_em = pltcl.single_plotline(
	name = "DYFileWinter17_em",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "em_nominal",
	den_folder = "em_nominal",
	num_tree = "ntuple",
	label = "Z#rightarrow#tau#tau simulation",
	color = "kRed",
	marker = "HISTO")

DYFileWinter17_em_copy = pltcl.single_plotline(
	name = "DYFileWinter17_em_copy",
	#num_file= "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/9/sbrommer/artus_outputs/ZmmValidation/DYJets_copy.root",	
	num_folder = "em_nominal",
	den_folder = "em_nominal",
	label = "Simulation uncertainty",
	num_tree = "ntuple")

DYFileWinter17_em_shift_up = pltcl.single_plotline(
	name = "DYFileWinter17_em_shift_up",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "em_EleEsUp",
	den_folder = "em_EleEsUp",
	num_tree = "ntuple",
	label = "#pm 1% ele energy scale",
	color = "kRed",
	marker = "HISTO")

DYFileWinter17_em_shift_down = pltcl.single_plotline(
	name = "DYFileWinter17_em_shift_down",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "em_EleEsDown",
	den_folder = "em_EleEsDown",
	num_tree = "ntuple",
	label = "",
	color = "kRed",
	marker = "HISTO")


DYFileWinter17_emb_em = pltcl.single_plotline(
	name = "DYFileWinter17_emb_em",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/EmbeddingMCRunIIWinter17_ElMuFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_ElMuFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/EmbeddingMCRunIIWinter17_ElMuFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_folder = "em_nominal",
	den_folder = "em_nominal",
	num_tree = "ntuple",
	label = "#mu #rightarrow #tau embedded",
	color = "kBlue",
	marker = "PE")

DYFileWinter17_et = pltcl.single_plotline(
	name = "DYFileWinter17_et",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "et_nominal",
	den_folder = "et_nominal",
	num_tree = "ntuple",
	color = "kRed",
	label = "Z#rightarrow#tau#tau simulation",
	marker = "HISTO")

DYFileWinter17_et_copy = pltcl.single_plotline(
	name = "DYFileWinter17_et_copy",
	#num_file= "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/9/sbrommer/artus_outputs/ZmmValidation/DYJets_copy.root",	
	num_folder = "et_nominal",
	den_folder = "et_nominal",
	label = "Simulation uncertainty",
	num_tree = "ntuple")

DYFileWinter17_et_shift_up = pltcl.single_plotline(
	name = "DYFileWinter17_et_shift_up",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "et_tauEsUp",
	den_folder = "et_tauEsUp",
	num_tree = "ntuple",
	color = "kRed",
	label = "#pm 1.2% #tau_{h} energy scale",
	marker = "HISTO")

DYFileWinter17_et_shift_down = pltcl.single_plotline(
	name = "DYFileWinter17_et_shift_down",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/DYJetsToLLM50_RunIIWinter17MiniAOD_NZSPU40to70_13TeV_MINIAOD_madgraph-pythia8_v3.root",
	num_folder = "et_tauEsDown",
	den_folder = "et_tauEsDown",
	num_tree = "ntuple",
	color = "kRed",
	label = "",
	marker = "HISTO")

DYFileWinter17_emb_et = pltcl.single_plotline(
	name = "DYFileWinter17_emb_et",
	#num_file = "/storage/9/sbrommer/artus_outputs/2018-05-02/EmbeddingMCRunIIWinter17_ElTauFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8/EmbeddingMCRunIIWinter17_ElTauFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_file = "/storage/c/jbechtel/MCEmbedding/EmbeddingMCRunIIWinter17_ElTauFinalState_inputWinter17DRNZSPU40to70GENSIMRAW_13TeV_USER_pythia8.root",
	num_folder = "et_nominal",
	den_folder = "et_nominal",
	num_tree = "ntuple",
	label = "#mu#rightarrow#tau embedded",
	color = "kBlue",
	marker = "PE")
