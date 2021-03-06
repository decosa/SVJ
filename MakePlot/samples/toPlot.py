import ROOT
import collections
import os, commands

from TTJets import *
from ZJets import *
from WJets import *
from QCD import *
from Data import *
from SVJ_mZprime1000_mDark20_rinv03_alpha02 import *
from SVJ_mZprime2000_mDark20_rinv03_alpha02 import *
from SVJ_mZprime3000_mDark20_rinv03_alpha02 import *
from SVJ_mZprime4000_mDark20_rinv03_alpha02 import *
from SVJ_mZprime3000_mDark1_rinv03_alpha02 import *
from SVJ_mZprime3000_mDark50_rinv03_alpha02 import *
from SVJ_mZprime3000_mDark100_rinv03_alpha02 import *
from SVJ_mZprime3000_mDark20_rinv01_alpha02 import *
from SVJ_mZprime3000_mDark20_rinv05_alpha02 import *
from SVJ_mZprime3000_mDark20_rinv07_alpha02 import *
from SVJ_mZprime3000_mDark20_rinv03_alpha01 import *
from SVJ_mZprime3000_mDark20_rinv03_alpha05 import *
from SVJ_mZprime3000_mDark20_rinv03_alpha1 import *

samples = collections.OrderedDict()

#samples["SVJ_mZprime1000_mDark20_rinv03_alpha02"] = SVJ_mZprime1000_mDark20_rinv03_alpha02
#samples["SVJ_mZprime2000_mDark20_rinv03_alpha02"] = SVJ_mZprime2000_mDark20_rinv03_alpha02
samples["SVJ_mZprime3000_mDark20_rinv03_alpha02"] = SVJ_mZprime3000_mDark20_rinv03_alpha02
#samples["SVJ_mZprime4000_mDark20_rinv03_alpha02"] = SVJ_mZprime4000_mDark20_rinv03_alpha02

#samples["SVJ_mZprime3000_mDark1_rinv03_alpha02"] = SVJ_mZprime3000_mDark1_rinv03_alpha02
#samples["SVJ_mZprime3000_mDark50_rinv03_alpha02"] = SVJ_mZprime3000_mDark50_rinv03_alpha02
#samples["SVJ_mZprime3000_mDark100_rinv03_alpha02"] = SVJ_mZprime3000_mDark100_rinv03_alpha02

#samples["SVJ_mZprime3000_mDark20_rinv01_alpha02"] = SVJ_mZprime3000_mDark20_rinv01_alpha02
#samples["SVJ_mZprime3000_mDark20_rinv05_alpha02"] = SVJ_mZprime3000_mDark20_rinv05_alpha02
#samples["SVJ_mZprime3000_mDark20_rinv07_alpha02"] = SVJ_mZprime3000_mDark20_rinv07_alpha02

#samples["SVJ_mZprime3000_mDark20_rinv03_alpha01"] = SVJ_mZprime3000_mDark20_rinv03_alpha01
#samples["SVJ_mZprime3000_mDark20_rinv03_alpha05"] = SVJ_mZprime3000_mDark20_rinv03_alpha05
#samples["SVJ_mZprime3000_mDark20_rinv03_alpha1"] = SVJ_mZprime3000_mDark20_rinv03_alpha1


samples["WJets"] = WJets
samples["ZJets"] = ZJets
samples["TTJets"]=TTJets
samples["QCD"] = QCD
samples["Data"] = Data

