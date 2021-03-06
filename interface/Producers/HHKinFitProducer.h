
#pragma once

#include <TLorentzVector.h>
#include <TVector2.h>
#include <TMatrixD.h>

#include "HiggsAnalysis/KITHiggsToTauTau/interface/HttTypes.h"


/** Producer for the HHKinFit
 *
 *  Required config tags:
 *  - ...
 *
 *  Required packages:
 *  git clone https://github.com/bvormwald/HHKinFit2
 *  cd HHKinFit2
 *  source compile.sh
 *
 *  Documentation:
 *  https://twiki.cern.ch/twiki/bin/viewauth/CMS/HHKinFit2
 */
class HHKinFitProducer: public ProducerBase<HttTypes> {
public:

	typedef typename HttTypes::event_type event_type;
	typedef typename HttTypes::product_type product_type;
	typedef typename HttTypes::setting_type setting_type;

	virtual std::string GetProducerId() const override;
	
	virtual void Init(setting_type const& settings) override;

	virtual void Produce(event_type const& event, product_type& product,
	                     setting_type const& settings) const override;

};

