#ifndef _MyTest__
#define _MyTest__

#include <TSystem.h>

#include <Centella.h>

class MyTest : public gate::IAlgo {

 public:
  
  //! default contructor
  MyTest(gate::VLEVEL=gate::NORMAL,
	       std::string label="MyTestInstance");
  
  //! constructor with store with input parameters 
  MyTest(const gate::ParamStore& gs,
	       gate::VLEVEL=gate::NORMAL,
	       std::string label="MyTestInstance");
  
  //! destructor
  virtual ~MyTest(){};
  
  //! initialize algorithm
  bool initialize();        
  
  //! execute algorithm: process current event
  bool execute(gate::Event& evt);  
  
  //! finalize algorithm
  bool finalize();          
  
 private:
  
  ClassDef(MyTest,0)
    
};

#endif
