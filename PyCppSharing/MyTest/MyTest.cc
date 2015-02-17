
#include<MyTest.h>

ClassImp(MyTest)

//==========================================================================
MyTest::MyTest(gate::VLEVEL vl, std::string label) : 
IAlgo(vl,"MyTest",0,label){
//==========================================================================


}

//==========================================================================
MyTest::MyTest(const gate::ParamStore& gs, 
			   gate::VLEVEL vl, std::string label) :
  IAlgo(gs,vl,"MyTest",0,label){
//==========================================================================


}

//==========================================================================
bool MyTest::initialize(){
//==========================================================================

  _m.message("Intializing algorithm",this->getAlgoLabel(),gate::NORMAL);
  
  gate::Centella::instance()
    ->hman()->h1("MyC++Histo","MyC++Histo",10,0,100);

  this->store("MyC++Var","ou");
    
  return true;

}

//==========================================================================
bool MyTest::execute(gate::Event& evt){
//==========================================================================

  _m.message("Executing algorithm",this->getAlgoLabel(),gate::VERBOSE);
  
  _m.message("Event number:",evt.GetEventID(),gate::VERBOSE);
  
  _m.message("This is a histogram from PyAlgo:",gate::NORMAL);

  gate::Centella::instance()
    ->hman()->fetch("MyPyHisto")->Print();
  
  return true;

}

//==========================================================================
bool MyTest::finalize(){
//==========================================================================

  _m.message("Finalising algorithm",this->getAlgoLabel(),gate::NORMAL);
  
  std::string var = gate::Centella::instance()
    ->logman().getLogs("USER").fetch_sstore("MyPythonVar2");

  _m.message("This is a parameter from PyAlgo:",var,gate::NORMAL);

  return true;

}
