
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/NewValidDiTauPairCandidatesProducers.h"


NewValidTTPairCandidatesProducer::NewValidTTPairCandidatesProducer() :
	NewValidDiTauPairCandidatesProducerBase<KTau, KTau>(
			&HttTypes::product_type::m_validTaus,
			&HttTypes::product_type::m_validTaus
	)
{
}

std::string NewValidTTPairCandidatesProducer::GetProducerId() const
{
	return "NewValidTTPairCandidatesProducer";
}

bool NewValidTTPairCandidatesProducer::AdditionalCriteria(DiTauPair const& diTauPair, event_type const& event,
	                                product_type& product, setting_type const& settings) const
	{
		bool validDiTauPair = true;
                if(!(diTauPair.first->p4.Pt() >= diTauPair.second->p4.Pt() && static_cast<DiTauPair>(diTauPair).GetDeltaR() != 0.0)) validDiTauPair = false;
		return validDiTauPair;
	}

NewValidMTPairCandidatesProducer::NewValidMTPairCandidatesProducer() :
	NewValidDiTauPairCandidatesProducerBase<KMuon, KTau>(
			&HttTypes::product_type::m_validMuons,
			&HttTypes::product_type::m_validTaus
	)
{
}

std::string NewValidMTPairCandidatesProducer::GetProducerId() const
{
	return "NewValidMTPairCandidatesProducer";
}


NewValidETPairCandidatesProducer::NewValidETPairCandidatesProducer() :
	NewValidDiTauPairCandidatesProducerBase<KElectron, KTau>(
			&HttTypes::product_type::m_validElectrons,
			&HttTypes::product_type::m_validTaus
	)
{
}

std::string NewValidETPairCandidatesProducer::GetProducerId() const
{
	return "NewValidETPairCandidatesProducer";
}


NewValidEMPairCandidatesProducer::NewValidEMPairCandidatesProducer() :
	NewValidDiTauPairCandidatesProducerBase<KMuon, KElectron>(
			&HttTypes::product_type::m_validMuons,
			&HttTypes::product_type::m_validElectrons
	)
{
}

std::string NewValidEMPairCandidatesProducer::GetProducerId() const
{
	return "NewValidEMPairCandidatesProducer";
}


NewValidMMPairCandidatesProducer::NewValidMMPairCandidatesProducer() :
	NewValidDiTauPairCandidatesProducerBase<KMuon, KMuon>(
			&HttTypes::product_type::m_validMuons,
			&HttTypes::product_type::m_validMuons
	)
{
}

std::string NewValidMMPairCandidatesProducer::GetProducerId() const
{
	return "NewValidMMPairCandidatesProducer";
}

bool NewValidMMPairCandidatesProducer::AdditionalCriteria(DiTauPair const& diTauPair, event_type const& event,
	                                product_type& product, setting_type const& settings) const
	{
		bool validDiTauPair = true;
                if(!(diTauPair.first->p4.Pt() >= diTauPair.second->p4.Pt() && static_cast<DiTauPair>(diTauPair).GetDeltaR() != 0.0)) validDiTauPair = false;
		return validDiTauPair;
	}

NewValidEEPairCandidatesProducer::NewValidEEPairCandidatesProducer() :
	NewValidDiTauPairCandidatesProducerBase<KElectron, KElectron>(
			&HttTypes::product_type::m_validElectrons,
			&HttTypes::product_type::m_validElectrons
	)
{
}

std::string NewValidEEPairCandidatesProducer::GetProducerId() const
{
	return "NewValidEEPairCandidatesProducer";
}

bool NewValidEEPairCandidatesProducer::AdditionalCriteria(DiTauPair const& diTauPair, event_type const& event,
	                                product_type& product, setting_type const& settings) const
	{
		bool validDiTauPair = true;
                if(!(diTauPair.first->p4.Pt() >= diTauPair.second->p4.Pt() && static_cast<DiTauPair>(diTauPair).GetDeltaR() != 0.0)) validDiTauPair = false;
		return validDiTauPair;
	}

