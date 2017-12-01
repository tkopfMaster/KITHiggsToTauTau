
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Utility/SvfitTools.h"

#include "Artus/Utility/interface/DefaultValues.h"
#include "Artus/Utility/interface/Utility.h"
#include "Artus/Utility/interface/SafeMap.h"

#include "Kappa/DataFormats/interface/Hash.h"


TauSVfitQuantity::TauSVfitQuantity(size_t tauIndex) :	
	classic_svFit::SVfitQuantity(),
	m_tauIndex(tauIndex),
	m_tauLabel("Tau"+std::to_string(tauIndex+1))
{
}

TauESVfitQuantity::TauESVfitQuantity(size_t tauIndex) : TauSVfitQuantity(tauIndex)
{
}
TH1* TauESVfitQuantity::createHistogram(const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	double E;
	if (m_tauIndex == 0) E = vis1P4.E();
	else E = vis2P4.E();
	return classic_svFit::HistogramTools::makeHistogram(std::string("SVfitAlgorithm_histogram"+m_tauLabel+"E").c_str(), E/1.025, TMath::Max(1.e+3, 1.e+1*E/1.025), 1.025);
}
double TauESVfitQuantity::fitFunction(const classic_svFit::LorentzVector& tau1P4, const classic_svFit::LorentzVector& tau2P4, const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	if (m_tauIndex == 0) return tau1P4.E();
	else return tau2P4.E();
}

TauERatioSVfitQuantity::TauERatioSVfitQuantity(size_t tauIndex) : TauSVfitQuantity(tauIndex)
{
}
TH1* TauERatioSVfitQuantity::createHistogram(const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	return new TH1D(std::string("SVfitAlgorithm_histogram"+m_tauLabel+"ERatio").c_str(), std::string("SVfitAlgorithm_histogram"+m_tauLabel+"ERatio").c_str(), 200, 0.0, 1.0);
}
double TauERatioSVfitQuantity::fitFunction(const classic_svFit::LorentzVector& tau1P4, const classic_svFit::LorentzVector& tau2P4, const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	if (m_tauIndex == 0) return vis1P4.E() / tau1P4.E();
	else return vis2P4.E() / tau2P4.E();
}

TauPtSVfitQuantity::TauPtSVfitQuantity(size_t tauIndex) : TauSVfitQuantity(tauIndex)
{
}
TH1* TauPtSVfitQuantity::createHistogram(const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	return classic_svFit::HistogramTools::makeHistogram(std::string("SVfitAlgorithm_histogram"+m_tauLabel+"Pt").c_str(), 1., 1.e+3, 1.025);
}
double TauPtSVfitQuantity::fitFunction(const classic_svFit::LorentzVector& tau1P4, const classic_svFit::LorentzVector& tau2P4, const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	if (m_tauIndex == 0) return tau1P4.pt();
	else return tau2P4.pt();
}

TauEtaSVfitQuantity::TauEtaSVfitQuantity(size_t tauIndex) : TauSVfitQuantity(tauIndex)
{
}
TH1* TauEtaSVfitQuantity::createHistogram(const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	return new TH1D(std::string("SVfitAlgorithm_histogram"+m_tauLabel+"Eta").c_str(), std::string("SVfitAlgorithm_histogram"+m_tauLabel+"Eta").c_str(), 198, -9.9, +9.9);
}
double TauEtaSVfitQuantity::fitFunction(const classic_svFit::LorentzVector& tau1P4, const classic_svFit::LorentzVector& tau2P4, const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	if (m_tauIndex == 0) return tau1P4.eta();
	else return tau2P4.eta();
}

TauPhiSVfitQuantity::TauPhiSVfitQuantity(size_t tauIndex) : TauSVfitQuantity(tauIndex)
{
}
TH1* TauPhiSVfitQuantity::createHistogram(const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	return new TH1D(std::string("SVfitAlgorithm_histogram"+m_tauLabel+"Phi").c_str(), std::string("SVfitAlgorithm_histogram"+m_tauLabel+"Phi").c_str(), 180, -TMath::Pi(), +TMath::Pi());
}
double TauPhiSVfitQuantity::fitFunction(const classic_svFit::LorentzVector& tau1P4, const classic_svFit::LorentzVector& tau2P4, const classic_svFit::LorentzVector& vis1P4, const classic_svFit::LorentzVector& vis2P4, classic_svFit::Vector const& measuredMET) const
{
	if (m_tauIndex == 0) return tau1P4.phi();
	else return tau2P4.phi();
}

MCTauTauQuantitiesAdapter::MCTauTauQuantitiesAdapter() : classic_svFit::DiTauSystemHistogramAdapter()
{
	quantities_.push_back(new TauERatioSVfitQuantity(0));
	quantities_.push_back(new TauPtSVfitQuantity(0));
	quantities_.push_back(new TauEtaSVfitQuantity(0));
	quantities_.push_back(new TauPhiSVfitQuantity(0));
	quantities_.push_back(new TauERatioSVfitQuantity(1));
	quantities_.push_back(new TauPtSVfitQuantity(1));
	quantities_.push_back(new TauEtaSVfitQuantity(1));
	quantities_.push_back(new TauPhiSVfitQuantity(1));
}

RMFLV MCTauTauQuantitiesAdapter::GetFittedHiggsLV() const
{
	RMFLV momentum;
	momentum.SetPt(getPt());
	momentum.SetEta(getEta());
	momentum.SetPhi(getPhi());
	momentum.SetM(getMass());
	return momentum;
}

float MCTauTauQuantitiesAdapter::GetFittedTau1ERatio() const
{
	return extractValue(5);
}

RMFLV MCTauTauQuantitiesAdapter::GetFittedTau1LV() const
{
	RMFLV momentum;
	momentum.SetPt(extractValue(6));
	momentum.SetEta(extractValue(7));
	momentum.SetPhi(extractValue(8));
	momentum.SetM(DefaultValues::TauMassGeV);
	return momentum;
}

float MCTauTauQuantitiesAdapter::GetFittedTau2ERatio() const
{
	return extractValue(9);
}

RMFLV MCTauTauQuantitiesAdapter::GetFittedTau2LV() const
{
	RMFLV momentum;
	momentum.SetPt(extractValue(10));
	momentum.SetEta(extractValue(11));
	momentum.SetPhi(extractValue(12));
	momentum.SetM(DefaultValues::TauMassGeV);
	return momentum;
}


SvfitEventKey::SvfitEventKey(ULong64_t const& runLumiEvent,
                             classic_svFit::MeasuredTauLepton::kDecayType const& decayType1, classic_svFit::MeasuredTauLepton::kDecayType const& decayType2,
                             HttEnumTypes::SystematicShift const& systematicShift,
                             float const& systematicShiftSigma, IntegrationMethod const& integrationMethod, ULong64_t const& hash)
{
	Set(runLumiEvent, decayType1, decayType2, systematicShift, systematicShiftSigma, integrationMethod, hash);
}

void SvfitEventKey::Set(ULong64_t const& runLumiEvent,
                        classic_svFit::MeasuredTauLepton::kDecayType const& decayType1, classic_svFit::MeasuredTauLepton::kDecayType const& decayType2,
                        HttEnumTypes::SystematicShift const& systematicShift,
                        float const& systematicShiftSigma, IntegrationMethod const& integrationMethod, ULong64_t const& hash)
{
	this->runLumiEvent = runLumiEvent;
	this->decayType1 = Utility::ToUnderlyingValue(decayType1);
	this->decayType2 = Utility::ToUnderlyingValue(decayType2);
	this->systematicShift = Utility::ToUnderlyingValue<HttEnumTypes::SystematicShift>(systematicShift);
	this->systematicShiftSigma = systematicShiftSigma;
	this->integrationMethod = Utility::ToUnderlyingValue<IntegrationMethod>(integrationMethod);
	this->hash = hash;
}

HttEnumTypes::SystematicShift SvfitEventKey::GetSystematicShift() const
{
	return Utility::ToEnum<HttEnumTypes::SystematicShift>(systematicShift);
}

SvfitEventKey::IntegrationMethod SvfitEventKey::GetIntegrationMethod() const
{
	return Utility::ToEnum<IntegrationMethod>(integrationMethod);
}

void SvfitEventKey::CreateBranches(TTree* tree)
{
	tree->Branch("runLumiEvent", &runLumiEvent, "runLumiEvent/l");
	tree->Branch("decayType1", &decayType1);
	tree->Branch("decayType2", &decayType2);
	tree->Branch("systematicShift", &systematicShift);
	tree->Branch("systematicShiftSigma", &systematicShiftSigma);
	tree->Branch("integrationMethod", &integrationMethod);
	tree->Branch("hash", &hash, "hash/l");
}

void SvfitEventKey::SetBranchAddresses(TTree* tree)
{
	tree->SetBranchAddress("runLumiEvent", &runLumiEvent);
	tree->SetBranchAddress("decayType1", &decayType1);
	tree->SetBranchAddress("decayType2", &decayType2);
	tree->SetBranchAddress("systematicShift", &systematicShift);
	tree->SetBranchAddress("systematicShiftSigma", &systematicShiftSigma);
	tree->SetBranchAddress("integrationMethod", &integrationMethod);
	tree->SetBranchAddress("hash", &hash);
	ActivateBranches(tree, true);
}

void SvfitEventKey::ActivateBranches(TTree* tree, bool activate)
{
	tree->SetBranchStatus("runLumiEvent", activate);
	tree->SetBranchStatus("decayType1", activate);
	tree->SetBranchStatus("decayType2", activate);
	tree->SetBranchStatus("systematicShift", activate);
	tree->SetBranchStatus("systematicShiftSigma", activate);
	tree->SetBranchStatus("integrationMethod", activate);
	tree->SetBranchStatus("hash", activate);
}

bool SvfitEventKey::operator<(SvfitEventKey const& rhs) const
{
	if (runLumiEvent == rhs.runLumiEvent)
	{
		if (decayType1 == rhs.decayType1)
		{
			if (decayType2 == rhs.decayType2)
			{
				if (integrationMethod == rhs.integrationMethod)
				{
					if (systematicShift == rhs.systematicShift)
					{
						if (hash == rhs.hash)
						{
							return (systematicShiftSigma < rhs.systematicShiftSigma);
						}
						else
						{
							return (hash < rhs.hash);
						}
					}
					else
					{
						return (systematicShift < rhs.systematicShift);
					}
				}
				else
				{
					return (integrationMethod < rhs.integrationMethod);
				}
			}
			else
			{
				return (decayType2 < rhs.decayType2);
			}
		}
		else
		{
			return (decayType1 < rhs.decayType1);
		}
	}
	else {
		return (runLumiEvent < rhs.runLumiEvent);
	}
}

bool SvfitEventKey::operator==(SvfitEventKey const& rhs) const
{
	return ((runLumiEvent == rhs.runLumiEvent) &&
	        (decayType1 == rhs.decayType1) &&
	        (decayType2 == rhs.decayType2) &&
	        (integrationMethod == rhs.integrationMethod) &&
	        (systematicShift == rhs.systematicShift) &&
	        (hash == rhs.hash) &&
	        Utility::ApproxEqual(systematicShiftSigma, rhs.systematicShiftSigma));
}

bool SvfitEventKey::operator!=(SvfitEventKey const& rhs) const
{
	return (! (*this == rhs));
}

std::string std::to_string(SvfitEventKey const& svfitEventKey)
{
	return std::string("SvfitEventKey(") +
			"runLumiEvent=" + std::to_string(svfitEventKey.runLumiEvent) + ", " +
			"decayType1=" + std::to_string(svfitEventKey.decayType1) + ", " +
			"decayType2=" + std::to_string(svfitEventKey.decayType2) + ", " +
			"systematicShift=" + std::to_string(svfitEventKey.systematicShift) + ", " +
			"systematicShiftSigma=" + std::to_string(svfitEventKey.systematicShiftSigma) + ", " +
			"integrationMethod=" + std::to_string(svfitEventKey.integrationMethod) + "," +
			"hash=" + std::to_string(svfitEventKey.hash) + ")";
}

std::ostream& operator<<(std::ostream& os, SvfitEventKey const& svfitEventKey)
{
	return os << std::to_string(svfitEventKey);
}

SvfitInputs::SvfitInputs(RMFLV const& leptonMomentum1, RMFLV const& leptonMomentum2,
                         RMDataV const& metMomentum, RMSM2x2 const& metCovariance,
                         int const& decayMode1, int const& decayMode2)
	: SvfitInputs()
{
	Set(leptonMomentum1, leptonMomentum2, metMomentum, metCovariance, decayMode1, decayMode2);
}

SvfitInputs::~SvfitInputs()
{
	/* TODO: freeing memory here creates segmentation faults
	if (leptonMomentum1)
	{
		delete leptonMomentum1;
	}
	if (leptonMomentum2)
	{
		delete leptonMomentum2;
	}
	if (metMomentum)
	{
		delete metMomentum;
	}
	if (metCovariance)
	{
		delete metCovariance;
	}
	*/
}

void SvfitInputs::Set(RMFLV const& leptonMomentum1, RMFLV const& leptonMomentum2,
                      RMDataV const& metMomentum, RMSM2x2 const& metCovariance,
                      int const& decayMode1, int const& decayMode2)
{
	if (! this->leptonMomentum1)
	{
		this->leptonMomentum1 = new RMFLV();
	}
	if (! this->leptonMomentum2)
	{
		this->leptonMomentum2 = new RMFLV();
	}
	if (! this->metMomentum)
	{
		this->metMomentum = new RMDataV();
	}
	if (! this->metCovariance)
	{
		this->metCovariance = new RMSM2x2();
	}
	
	*(this->leptonMomentum1) = leptonMomentum1;
	*(this->leptonMomentum2) = leptonMomentum2;
	*(this->metMomentum) = metMomentum;
	*(this->metCovariance) = metCovariance;
	this->decayMode1 = decayMode1;
	this->decayMode2 = decayMode2;
}

void SvfitInputs::CreateBranches(TTree* tree)
{
	tree->Branch("leptonMomentum1", "RMFLV", &leptonMomentum1);
	tree->Branch("leptonMomentum2", "RMFLV", &leptonMomentum2);
	tree->Branch("metMomentum", "ROOT::Math::DisplacementVector3D<ROOT::Math::Cartesian3D<float>,ROOT::Math::DefaultCoordinateSystemTag>", &metMomentum);
	tree->Branch("metCovariance", "ROOT::Math::SMatrix<double, 2, 2, ROOT::Math::MatRepSym<double, 2> >", &metCovariance);
	tree->Branch("decayMode1", &decayMode1);
	tree->Branch("decayMode2", &decayMode2);
}

void SvfitInputs::SetBranchAddresses(TTree* tree)
{
	tree->SetBranchAddress("leptonMomentum1", &leptonMomentum1);
	tree->SetBranchAddress("leptonMomentum2", &leptonMomentum2);
	tree->SetBranchAddress("metMomentum", &metMomentum);
	tree->SetBranchAddress("metCovariance", &metCovariance);
	tree->SetBranchAddress("decayMode1", &decayMode1);
	tree->SetBranchAddress("decayMode2", &decayMode2);
	ActivateBranches(tree, true);
}

void SvfitInputs::ActivateBranches(TTree* tree, bool activate)
{
	tree->SetBranchStatus("leptonMomentum1", activate);
	tree->SetBranchStatus("leptonMomentum2", activate);
	tree->SetBranchStatus("metMomentum", activate);
	tree->SetBranchStatus("metCovariance", activate);
	tree->SetBranchStatus("decayMode1", activate);
	tree->SetBranchStatus("decayMode2", activate);
}

bool SvfitInputs::operator==(SvfitInputs const& rhs) const
{
	return (Utility::ApproxEqual(*leptonMomentum1, *(rhs.leptonMomentum1)) &&
	        Utility::ApproxEqual(*leptonMomentum2, *(rhs.leptonMomentum2)) &&
	        Utility::ApproxEqual(*metMomentum, *(rhs.metMomentum)) &&
	        Utility::ApproxEqual(*metCovariance, *(rhs.metCovariance)) &&
	        (decayMode1 == rhs.decayMode1) &&
	        (decayMode2 == rhs.decayMode2));
}

bool SvfitInputs::operator!=(SvfitInputs const& rhs) const
{
	return (! (*this == rhs));
}

ClassicSVfit SvfitInputs::GetSvfitAlgorithm(int verbosity, SvfitEventKey const& svfitEventKey, bool addLogM) const
{
	ClassicSVfit svfitAlgorithm = ClassicSVfit(verbosity);
	
	svfitAlgorithm.setHistogramAdapter(new MCTauTauQuantitiesAdapter());
	
	
	double kappa = 3.;
	if (svfitEventKey.decayType1==1) kappa += 1.;
	if (svfitEventKey.decayType1==2) kappa += 1.;
	svfitAlgorithm.addLogM_fixed(addLogM, kappa);
	/*if (visPtResolutionFile == 0)
	{
		TDirectory *savedir(gDirectory);
		TFile *savefile(gFile);
		TString cmsswBase = TString( getenv ("CMSSW_BASE") );
		visPtResolutionFile = new TFile(cmsswBase+"/src/TauAnalysis/SVfitStandalone/data/svFitVisMassAndPtResolutionPDF.root");
		gDirectory = savedir;
		gFile = savefile;
	}
	svfitAlgorithm.shiftVisPt(true, visPtResolutionFile);*/
	
	return svfitAlgorithm;
}

std::vector<classic_svFit::MeasuredTauLepton> SvfitInputs::GetMeasuredTauLeptons(SvfitEventKey const& svfitEventKey) const
{
	double leptonMass1, leptonMass2;
	if(svfitEventKey.decayType1 == 2)
	{
		leptonMass1 = 0.51100e-3;
	}
	else if(svfitEventKey.decayType1 == 3)
	{
		leptonMass1 = 105.658e-3;
	}
	else
	{
		leptonMass1 = leptonMomentum1->M();
	}
	if(svfitEventKey.decayType2 == 2)
	{
		leptonMass2 = 0.51100e-3;
	}
	else if(svfitEventKey.decayType2 == 3)
	{
		leptonMass2 = 105.658e-3;
	}
	else
	{
		leptonMass2 = leptonMomentum2->M();
	}
	std::vector<classic_svFit::MeasuredTauLepton> measuredTauLeptons {
		classic_svFit::MeasuredTauLepton(Utility::ToEnum<classic_svFit::MeasuredTauLepton::kDecayType>(svfitEventKey.decayType1), leptonMomentum1->pt(), leptonMomentum1->eta(), leptonMomentum1->phi(), leptonMass1, decayMode1),
		classic_svFit::MeasuredTauLepton(Utility::ToEnum<classic_svFit::MeasuredTauLepton::kDecayType>(svfitEventKey.decayType2), leptonMomentum2->pt(), leptonMomentum2->eta(), leptonMomentum2->phi(), leptonMass2, decayMode2)
	};
	return measuredTauLeptons;
}

TMatrixD SvfitInputs::GetMetCovarianceMatrix() const
{
	TMatrixD metCovarianceMatrix(2, 2);
	metCovarianceMatrix[0][0] = metCovariance->At(0, 0);
	metCovarianceMatrix[1][0] = metCovariance->At(1, 0);
	metCovarianceMatrix[0][1] = metCovariance->At(0, 1);
	metCovarianceMatrix[1][1] = metCovariance->At(1, 1);
	return metCovarianceMatrix;
}

SvfitResults::SvfitResults(double fittedTransverseMass, RMFLV const& fittedHiggsLV, float fittedTau1ERatio, RMFLV const& fittedTau1LV, float fittedTau2ERatio, RMFLV const& fittedTau2LV) :
	SvfitResults()
{
	Set(fittedTransverseMass, fittedHiggsLV, fittedTau1ERatio, fittedTau1LV, fittedTau2ERatio, fittedTau2LV);
	recalculated = false;
}

SvfitResults::SvfitResults(ClassicSVfit const& svfitAlgorithm) :
	SvfitResults()
{
	Set(svfitAlgorithm);
}

SvfitResults::~SvfitResults()
{
	/* TODO: freeing memory here creates segmentation faults
	if (fittedHiggsLV)
	{
		delete fittedHiggsLV;
	}
	if (fittedTau1LV)
	{
		delete fittedTau1LV;
	}
	if (fittedTau2LV)
	{
		delete fittedTau2LV;
	}
	*/
}

void SvfitResults::Set(double fittedTransverseMass, RMFLV const& fittedHiggsLV, float fittedTau1ERatio, RMFLV const& fittedTau1LV, float fittedTau2ERatio, RMFLV const& fittedTau2LV)
{
	if (! this->fittedHiggsLV)
	{
		this->fittedHiggsLV = new RMFLV();
	}
	if (! this->fittedTau1LV)
	{
		this->fittedTau1LV = new RMFLV();
	}
	if (! this->fittedTau2LV)
	{
		this->fittedTau2LV = new RMFLV();
	}
	
	this->fittedTransverseMass = fittedTransverseMass;
	*(this->fittedHiggsLV) = fittedHiggsLV;
	this->fittedTau1ERatio = fittedTau1ERatio;
	*(this->fittedTau1LV) = fittedTau1LV;
	this->fittedTau2ERatio = fittedTau2ERatio;
	*(this->fittedTau2LV) = fittedTau2LV;
}

void SvfitResults::Set(ClassicSVfit const& svfitAlgorithm)
{
	if (svfitAlgorithm.isValidSolution())
	{
		Set(GetFittedTransverseMass(svfitAlgorithm),
		    GetFittedHiggsLV(svfitAlgorithm),
		    GetFittedTau1ERatio(svfitAlgorithm),
		    GetFittedTau1LV(svfitAlgorithm),
		    GetFittedTau2ERatio(svfitAlgorithm),
		    GetFittedTau2LV(svfitAlgorithm));
	}
	else
	{
		Set(DefaultValues::UndefinedDouble,
		    DefaultValues::UndefinedRMFLV,
		    DefaultValues::UndefinedDouble,
		    DefaultValues::UndefinedRMFLV,
		    DefaultValues::UndefinedDouble,
		    DefaultValues::UndefinedRMFLV);
	}
}

void SvfitResults::CreateBranches(TTree* tree)
{
	tree->Branch("svfitTransverseMass", &fittedTransverseMass, "svfitTransverseMass/D");
	tree->Branch("svfitHiggsLV", &fittedHiggsLV);
	tree->Branch("svfitTau1ERatio", &fittedTau1ERatio, "svfitTau1ERatio/F");
	tree->Branch("svfitTau1LV", &fittedTau1LV);
	tree->Branch("svfitTau2ERatio", &fittedTau2ERatio, "svfitTau2ERatio/F");
	tree->Branch("svfitTau2LV", &fittedTau2LV);
}

void SvfitResults::SetBranchAddresses(TTree* tree)
{
	tree->SetBranchAddress("svfitTransverseMass", &fittedTransverseMass);
	tree->SetBranchAddress("svfitHiggsLV", &fittedHiggsLV);
	tree->SetBranchAddress("svfitTau1ERatio", &fittedTau1ERatio);
	tree->SetBranchAddress("svfitTau1LV", &fittedTau1LV);
	tree->SetBranchAddress("svfitTau2ERatio", &fittedTau2ERatio);
	tree->SetBranchAddress("svfitTau2LV", &fittedTau2LV);
	ActivateBranches(tree, true);
}

void SvfitResults::ActivateBranches(TTree* tree, bool activate)
{
	tree->SetBranchStatus("svfitTransverseMass", activate);
	tree->SetBranchStatus("svfitHiggsLV", activate);
	tree->SetBranchStatus("svfitTau1ERatio", activate);
	tree->SetBranchStatus("svfitTau1LV", activate);
	tree->SetBranchStatus("svfitTau2ERatio", activate);
	tree->SetBranchStatus("svfitTau2LV", activate);
}

bool SvfitResults::operator==(SvfitResults const& rhs) const
{
	return (Utility::ApproxEqual(fittedTransverseMass, rhs.fittedTransverseMass) &&
	        Utility::ApproxEqual(*fittedHiggsLV, *(rhs.fittedHiggsLV)) &&
	        Utility::ApproxEqual(fittedTau1ERatio, rhs.fittedTau1ERatio) &&
	        Utility::ApproxEqual(*fittedTau1LV, *(rhs.fittedTau1LV)) &&
	        Utility::ApproxEqual(fittedTau2ERatio, rhs.fittedTau2ERatio) &&
	        Utility::ApproxEqual(*fittedTau2LV, *(rhs.fittedTau2LV)));
}

bool SvfitResults::operator!=(SvfitResults const& rhs) const
{
	return (! (*this == rhs));
}

double SvfitResults::GetFittedTransverseMass(ClassicSVfit const& svfitAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitAlgorithm.getHistogramAdapter())->getTransverseMass();
}
RMFLV SvfitResults::GetFittedHiggsLV(ClassicSVfit const& svfitAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitAlgorithm.getHistogramAdapter())->GetFittedHiggsLV();
}
float SvfitResults::GetFittedTau1ERatio(ClassicSVfit const& svfitAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitAlgorithm.getHistogramAdapter())->GetFittedTau1ERatio();
}
RMFLV SvfitResults::GetFittedTau1LV(ClassicSVfit const& svfitAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitAlgorithm.getHistogramAdapter())->GetFittedTau1LV();
}
float SvfitResults::GetFittedTau2ERatio(ClassicSVfit const& svfitAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitAlgorithm.getHistogramAdapter())->GetFittedTau2ERatio();
}
RMFLV SvfitResults::GetFittedTau2LV(ClassicSVfit const& svfitAlgorithm) const
{
	return static_cast<MCTauTauQuantitiesAdapter*>(svfitAlgorithm.getHistogramAdapter())->GetFittedTau2LV();
}


std::map<std::string, TFile*> SvfitTools::svfitCacheInputFiles;
std::map<std::string, TTree*> SvfitTools::svfitCacheInputTrees;
std::map<std::string, std::map<SvfitEventKey, uint64_t>> SvfitTools::svfitCacheInputTreeIndices;

void SvfitTools::Init(std::string const& cacheFileName, std::string const& cacheTreeName)
{
	this->cacheFileName = cacheFileName;
	this->cacheFileTreeName = cacheFileName+"/"+cacheTreeName;
	
	if (! Utility::Contains(SvfitTools::svfitCacheInputTreeIndices, cacheFileTreeName))
	{
		TDirectory* savedir(gDirectory);
		TFile* savefile(gFile);
		
		TFile* svfitCacheInputFile = nullptr;
		if (! Utility::Contains(SvfitTools::svfitCacheInputFiles, cacheFileName))
		{
			svfitCacheInputFile = TFile::Open(cacheFileName.c_str(), "READ", cacheFileName.c_str());
		}
		else
		{
			svfitCacheInputFile = SafeMap::Get(SvfitTools::svfitCacheInputFiles, cacheFileName);
		}
		
		if (svfitCacheInputFile)
		{
			TTree* svfitCacheInputTree = dynamic_cast<TTree*>(svfitCacheInputFile->Get(cacheTreeName.c_str()));
			if (svfitCacheInputTree)
			{
				LOG(DEBUG) << "\tLoaded SVfit cache trees from file...";
				LOG(DEBUG) << "\t\t" << cacheFileTreeName << " with " << svfitCacheInputTree->GetEntries() << " Entries";

				svfitEventKey.SetBranchAddresses(svfitCacheInputTree);
				std::map<SvfitEventKey, uint64_t> svfitCacheInputTreeIndices;
				for (uint64_t svfitCacheInputTreeIndex = 0;
					 svfitCacheInputTreeIndex < uint64_t(svfitCacheInputTree->GetEntries());
					 ++svfitCacheInputTreeIndex)
				{
					svfitCacheInputTree->GetEntry(svfitCacheInputTreeIndex);

					svfitCacheInputTreeIndices[svfitEventKey] = svfitCacheInputTreeIndex;
					LOG_N_TIMES(10, DEBUG) << std::to_string(svfitEventKey) << " --> " << svfitCacheInputTreeIndex;
					LOG_N_TIMES(10, DEBUG) << svfitEventKey << " --> " << svfitCacheInputTreeIndex;
				}
				svfitEventKey.ActivateBranches(svfitCacheInputTree, false);
				LOG(DEBUG) << "\t\t" << svfitCacheInputTreeIndices.size() << " entries found.";
		
				svfitResults.SetBranchAddresses(svfitCacheInputTree);
			
				SvfitTools::svfitCacheInputTrees[cacheFileTreeName] = svfitCacheInputTree;
				SvfitTools::svfitCacheInputTreeIndices[cacheFileTreeName] = svfitCacheInputTreeIndices;
			}
			else
			{
				LOG(WARNING) << "Could not read SVfit cache tree from \"" << cacheFileTreeName << "\"!";
			}
			
			SvfitTools::svfitCacheInputFiles[cacheFileName] = svfitCacheInputFile;
		}
		else
		{
			LOG(WARNING) << "Could not open SVfit cache file \"" << cacheFileName << "\"!";
		}

		gDirectory = savedir;
		gFile = savefile;
	}
	else 
	{
		LOG(DEBUG) << "\tSVfit cache trees from file " << cacheFileName << " already loaded.";
	}
}

SvfitResults SvfitTools::GetResults(SvfitEventKey const& svfitEventKey,
                                    SvfitInputs const& svfitInputs,
                                    bool& neededRecalculation,
                                    HttEnumTypes::SvfitCacheMissBehaviour svfitCacheMissBehaviour)
{
	neededRecalculation = true;
	if (Utility::Contains(SvfitTools::svfitCacheInputTrees, cacheFileTreeName) && Utility::Contains(SvfitTools::svfitCacheInputTreeIndices, cacheFileTreeName))
	{
		if (Utility::Contains(SafeMap::Get(SvfitTools::svfitCacheInputTreeIndices, cacheFileTreeName), svfitEventKey))
		{
			SafeMap::Get(SvfitTools::svfitCacheInputTrees, cacheFileTreeName)->GetEntry(SafeMap::Get(SafeMap::Get(SvfitTools::svfitCacheInputTreeIndices, cacheFileTreeName), svfitEventKey));
			svfitResults.FromCache();
			neededRecalculation = false;
		}
	}
	if (neededRecalculation)
	{
		if(svfitCacheMissBehaviour == HttEnumTypes::SvfitCacheMissBehaviour::recalculate)
		{
			LOG_N_TIMES(30, INFO) << "SvfitCache miss: No corresponding entry to the current inputs found in SvfitCache file. Re-Running SvFit. Did your inputs change?" 
			                      << std::endl << "Cache searched in tree: \"" << cacheFileTreeName << "\".";
		}
		if(svfitCacheMissBehaviour == HttEnumTypes::SvfitCacheMissBehaviour::assert)
		{
			LOG(FATAL) << "SvfitCache miss: No corresponding entry to the current inputs found in SvfitCache file. Did your inputs change?";
		}
		if(svfitCacheMissBehaviour == HttEnumTypes::SvfitCacheMissBehaviour::undefined)
		{
			svfitResults.FromRecalculation();
			return svfitResults;
		}
		
		// construct algorithm
		ClassicSVfit svfitAlgorithm = svfitInputs.GetSvfitAlgorithm(0, svfitEventKey, true);
	
		// execute integration
		if (svfitEventKey.GetIntegrationMethod() == SvfitEventKey::IntegrationMethod::VEGAS)
		{
			LOG(FATAL) << "SVfit integration of type " << svfitEventKey.integrationMethod << " not yet implemented!";
		}
		else if (svfitEventKey.GetIntegrationMethod() == SvfitEventKey::IntegrationMethod::MARKOV_CHAIN)
		{
			svfitAlgorithm.integrate(svfitInputs.GetMeasuredTauLeptons(svfitEventKey),
	                                                                             svfitInputs.metMomentum->x(),
	                                                                             svfitInputs.metMomentum->y(),
	                                                                             svfitInputs.GetMetCovarianceMatrix());
		}
		else if (svfitEventKey.GetIntegrationMethod() == SvfitEventKey::IntegrationMethod::FIT)
		{
			LOG(FATAL) << "SVfit integration of type " << svfitEventKey.integrationMethod << " not yet implemented!";
		}
		else
		{
			LOG(FATAL) << "SVfit integration of type " << svfitEventKey.integrationMethod << " not yet implemented!";
		}
	
		// retrieve results
		svfitResults.Set(svfitAlgorithm);
		svfitResults.FromRecalculation();
	}
	
	return svfitResults;
}

SvfitTools::~SvfitTools()
{
	/*if (m_visPtResolutionFile)
	{
		m_visPtResolutionFile->Close();
	}*/
	
	if (Utility::Contains(SvfitTools::svfitCacheInputFiles, cacheFileName) && SafeMap::Get(SvfitTools::svfitCacheInputFiles, cacheFileName)->IsOpen())
	{
		SafeMap::Get(SvfitTools::svfitCacheInputFiles, cacheFileName)->Close();
		SvfitTools::svfitCacheInputFiles.erase(cacheFileName);
	}
	
	// do NOT call destructor for TTree and TFile here. They are static and the destructor is called several times when running the factory
	// We have to trust the OS does handle freeing the memory properly
}
