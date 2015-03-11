from Centella import centella

import sys

sys.path.append('./')

from PyAlgo import *

from ROOT import gSystem
gSystem.Load('$GATE_DIR/lib/libGATE')
gSystem.Load('$GATE_DIR/lib/libGATEIO')
gSystem.Load('$GATE_DIR/lib/libGATEUtils')
gSystem.Load("MyTest/lib/libMyTest.so")
from ROOT import gate
from ROOT import MyTest

algos,idsts = [],[]

idsts.append("/home/pnovella/Physics/NEXT/DATA/myOutputDST.root")

st = gate.ParamStore()

algos.append(MyTest(st,gate.NORMAL,'C++Algo'))

algos.append(PyAlgo(False,1,'PyAlgo'))

c= centella.centella(algos,idsts,level=1,max_evt=1,
                     histos=True,hfile="PyCppSharing.log",
                     log=True,logFile="PyCppSharing.log",
                     reader="gateReader")

c.run()

