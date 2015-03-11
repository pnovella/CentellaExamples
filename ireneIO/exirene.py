
from Centella.AAlgo import AAlgo
from Centella.physical_constants import *

class exirene(AAlgo):

    def __init__(self,param=False,level = 1,label="",**kargs):

        """
        
        Deal here with your parameters in param and kargs.
        If param is an instace of ParamManager, parameters
        will be set as algorithm parameters by AAlgo.
            
        """
        
        self.name='exirene'
        
        AAlgo.__init__(self,param,level,self.name,0,label,kargs)

        # your stuff here...


    def initialize(self):

        """

        You can use here:

            self.hman     -----> histoManager instance
            self.tman     -----> treeManager instance
            self.logman   -----> logManager instance
            self.autoDoc  -----> latex_gen instance
        
        """
        
        self.m.log(1,'+++Init method of exirene algorithm+++')
        
        self.hman.h1("EventID","Event ID; Number;",100,0,10000)

        return

    def execute(self,event=""):

        """
        
        You can also use here:

            self.event ----> current event from the input data 
            
        """
        
        self.hman.fill("EventID",event.GetID())
        
        return True 

    def finalize(self):

        self.m.log(1,'+++End method of exirene algorithm+++')

        return

    
