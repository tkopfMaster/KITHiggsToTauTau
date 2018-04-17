
#pragma once

#include "Artus/Core/interface/ProducerBase.h"
#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttTypes.h"
#include "TFile.h"
#include "TGraphAsymmErrors.h"
#include "TauTriggerSFs2017/TauTriggerSFs2017/interface/TauTriggerSFs2017.h"

/**
   \brief TauTrigger2017EfficiencyProducer
   Config tags:
   - Fill me with something meaningful

*/

class TauTrigger2017EfficiencyProducer: public ProducerBase<HttTypes> {
public:

	typedef typename HttTypes::event_type event_type;
	typedef typename HttTypes::product_type product_type;
	typedef typename HttTypes::setting_type setting_type;

	std::string GetProducerId() const;

	virtual void Init(setting_type const& settings) override
	{
		ProducerBase<HttTypes>::Init(settings);
                TauSFs = new TauTriggerSFs2017(settings.GetTauTrigger2017Input(),settings.GetTauTrigger2017WorkingPoint());
                m_weightNames = Utility::ParseMapTypes<int,std::string>(Utility::ParseVectorToMap(settings.GetTauTrigger2017EfficiencyWeightNames()));
                for(auto weightNames: m_weightNames)
                {
                        for(size_t index = 0; index < weightNames.second.size(); index++)
                        {
                                MCWeight[weightNames.first].resize(weightNames.second.size());
                                MCWeight[weightNames.first].at(index) = (weightNames.second.at(index).find("MC") != std::string::npos);
                        }
                }
	}

	virtual void Produce(event_type const& event, product_type & product, 
	                     setting_type const& settings) const override;
private:
        TauTriggerSFs2017* TauSFs;
        std::map<int,std::vector<std::string>> m_weightNames;
        std::map<int,std::vector<bool>> MCWeight;
};
