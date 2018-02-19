import numpy as np
import pandas as pd

import time
Niswanob1=None
fuscat1=None
class Chri1:
 def __init__(Chri2,input):
  Chri2.input=input

 def bitboostdotcom2(Niswanob2,input,fuscat2,bitboostdotcom1,Chri4):
  global fuscat1
  if (fuscat2==bitboostdotcom1):
   fuscat1[Chri4]=input[fuscat2]
   return

  fuscat3=(fuscat2 + ((bitboostdotcom1 - fuscat2) / 2))
  Niswanob2.bitboostdotcom2(input,fuscat2,fuscat3,((2*    Chri4) + 1))
  Niswanob2.bitboostdotcom2(input,(fuscat3 + 1),bitboostdotcom1,((2*    Chri4) + 2))
  fuscat1[Chri4]=(fuscat1[((2*    Chri4) + 1)] + fuscat1[((2*    Chri4) + 2)])
  return

 def ordemo2(ordemo1,bitboostdotcom3,Chri3,fuscat5,ordemo3,bitboostdotcom4):
  global fuscat1
  if ((bitboostdotcom3<=fuscat5) and (Chri3>=ordemo3)):
   return fuscat1[bitboostdotcom4]
  elif ((bitboostdotcom3>ordemo3) or (Chri3<fuscat5)):
   return 0

  bitboostdotcom5=(fuscat5 + ((ordemo3 - fuscat5) / 2))
  bitboostdotcom7=ordemo1.ordemo2(bitboostdotcom3,Chri3,fuscat5,bitboostdotcom5,((2*    bitboostdotcom4) + 1))
  Niswanob4=ordemo1.ordemo2(bitboostdotcom3,Chri3,(bitboostdotcom5 + 1),ordemo3,((2*    bitboostdotcom4) + 2))
  return (bitboostdotcom7 + Niswanob4)


def Niswanob8():
 global Niswanob1
 global fuscat1
 global bitboostdotcom6
 global Niswanob3
 Chri5='final.csv'
 Chri6=pd.read_csv(Chri5)
 fuscat4=Chri6.iloc[:,6]
 input=list(fuscat4)
 Niswanob1=Chri1(input)
 bitboostdotcom6=0
 Niswanob3=(len(input) - 1)
 fuscat6=len(input)
 Niswanob5=int(np.ceil(np.log2(fuscat6)))
 bitboostdotcomA=((2*    int(np.power(2,Niswanob5))) - 1)
 fuscat1=[0 for bitboostdotcomB in       range(0,bitboostdotcomA)]
 Niswanob1.bitboostdotcom2(input,bitboostdotcom6,Niswanob3,0)

Niswanob8()
def ordemo6():
 global fuscat1
 global Niswanob1
 global bitboostdotcom6
 global Niswanob3
 start=10
 bitboostdotcomC=100
 sum=Niswanob1.ordemo2(start,bitboostdotcomC,bitboostdotcom6,Niswanob3,0)
 ordemo4=(sum / ((bitboostdotcomC - start) + 1))
 return ordemo4
