
from Centella import centella

from exirene import *

vlevel=1 # verbosity

algos, idsts = [], [] # algorithms, input data

idsts.append("~/Physics/NEXT/DATA/Next100.Bi214.ICS.0.next")

algos.append( exirene(False,vlevel,'exirene') )

c= centella.centella(algos,idsts,reader="ireneReader",level=vlevel)

#------------- Histogram declaration -------------#

# Line below only needed if user wants to set the histos here.
# Histograms can also be declared in initialize method of algorithms

c.hman.h1("EventID","Event ID; Number;",100,0,1000)

#-------------------------------------------------#

c.run()


