#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc630
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh

# set up CMSSW release area
scramv1 project CMSSW_9_4_4; pushd CMSSW_9_4_4/src 
eval `scramv1 runtime -sh`

# JEC
git cms-addpkg CondFormats/JetMETObjects

# From Kappa, only the DataFormats are needed
# Mind that for certain skims, you need exactly the Kappa git tag that has been used for the production
git clone https://github.com/KIT-CMS/Kappa.git
pushd Kappa
echo docs/ >> .git/info/sparse-checkout
echo DataFormats/ >> .git/info/sparse-checkout
echo Skimming/ >> .git/info/sparse-checkout
git config core.sparsecheckout true
git read-tree -mu HEAD
popd

git clone https://github.com/KIT-CMS/KappaTools.git -b master

git clone https://github.com/KIT-CMS/Artus.git

# checkout KITHiggsToTauTau CMSSW analysis package
git clone https://github.com/KIT-CMS/KITHiggsToTauTau HiggsAnalysis/KITHiggsToTauTau
#  git clone https://github.com/KIT-CMS/HiggsAnalysis-KITHiggsToTauTau.wiki.git HiggsAnalysis/KITHiggsToTauTau/doc/wiki

# Svfit and HHKinFit
git clone https://github.com/svfit/ClassicSVfit TauAnalysis/ClassicSVfit
cd TauAnalysis/ClassicSVfit
git checkout c78af4dc0f54cdc1c0d4b4fc4879918cfa2527c9
cd ../..
git clone https://github.com/svfit/SVfitTF TauAnalysis/SVfitTF
#git clone https://github.com/artus-analysis/HHKinFit2.git -b artus

# Jet2Tau Fakes
git clone https://github.com/CMS-HTT/Jet2TauFakes.git HTTutilities/Jet2TauFakes

# EmuQCD Method
git clone https://github.com/CMS-HTT/QCDModelingEMu.git HTT-utilities/QCDModelingEMu

# Fit Package for tau polarisation
#git clone https://github.com/CMSAachen3B/SimpleFits.git -b artus_master

sed '/CombineHarvester/d' ${CMSSW_BASE}/src/HiggsAnalysis/KITHiggsToTauTau/BuildFile.xml -i

# needed for error propagation e.g. in the background estimations
git clone https://github.com/lebigot/uncertainties.git -b 2.4.6.1 HiggsAnalysis/KITHiggsToTauTau/python/uncertainties

sed 's/cms2/ikhhed3/g' ${CMSSW_BASE}/src/HiggsAnalysis/KITHiggsToTauTau/data/tauspinner.xml -i

# TauTriggerSFs2017 tool
mkdir TauTriggerSFs2017
cd TauTriggerSFs2017
git clone https://github.com/truggles/TauTriggerSFs2017.git -b tauTriggers2017_MCv2_PreReMiniaod
cd ..

# Grid-Control
git clone https://github.com/janekbechtel/grid-control.git
# source ini script, needs to be done in every new shell
source HiggsAnalysis/KITHiggsToTauTau/scripts/ini_KITHiggsToTauTauAnalysis.sh

# compile everything
scram b -j 4
popd
