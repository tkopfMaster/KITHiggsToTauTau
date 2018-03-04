
#include "HiggsAnalysis/KITHiggsToTauTau/interface/Producers/TauTrigger2017EfficiencyProducer.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttEnumTypes.h"

std::string TauTrigger2017EfficiencyProducer::GetProducerId() const
{
	return "TauTrigger2017EfficiencyProducer";
}

void TauTrigger2017EfficiencyProducer::Produce( event_type const& event, product_type & product, 
												setting_type const& settings) const
{
	for(auto weightNames: m_weightNames)
	{
		KLepton* lepton = product.m_flavourOrderedLeptons[weightNames.first];
		for(size_t index = 0; index < weightNames.second.size(); index++)
		{
                    bool mc_weight = MCWeight.at(weightNames.first).at(index);
                    if(mc_weight)
                    {
                            //std::cout << "MC: " << TauSFs->getETauEfficiencyMC(lepton->p4.Pt(),lepton->p4.Eta(),lepton->p4.Phi()) << std::endl;
                            product.m_weights[weightNames.second.at(index)+"_"+std::to_string(weightNames.first+1)] = TauSFs->getETauEfficiencyMC(lepton->p4.Pt(),lepton->p4.Eta(),lepton->p4.Phi());
                    }
                    else
                    {
                            //std::cout << "Data: " <<  TauSFs->getETauEfficiencyData(lepton->p4.Pt(),lepton->p4.Eta(),lepton->p4.Phi()) << std::endl;
                            product.m_weights[weightNames.second.at(index)+"_"+std::to_string(weightNames.first+1)] = TauSFs->getETauEfficiencyData(lepton->p4.Pt(),lepton->p4.Eta(),lepton->p4.Phi());
                    }
		}
	}
}
