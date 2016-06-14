# compute parts of the carbonate system
import numpy as np
import pdb
def carbonate(**kwargs):
    '''
    phase='pH','temperature','oxygen'
    phase='Omega_arg','temperature','oxygen'
    phase='Omega_cal','temperature','oxygen'
    phase='total_alk','temperature','salinity'
    phase='dic','oxygen','potential density'
    phase='carbonate','temperature','oxygen'
    example ph=carbonate(phase="pH",temperature=[10],oxygen=[200])
    REFERENCE----------------------------------------------------------
    "Robust empirical relationships for estimating the carbonate system
    in the southern California Current System and application to CalCOFI
    hydrographic cruise data (2005-2011)" Simone R. Alin et. al.
    JGR 117 C05033 doi:10.1029/2011JC007511,2012
    -------------------------------------------------------------------'''
    #i=-1
    if kwargs.has_key("temperature") and kwargs.has_key("oxygen"):
        data1=kwargs["temperature"]
        data2=kwargs["oxygen"]
        if kwargs["phase"] == "pH":
            i=0
        else:
            if kwargs["phase"]== "Omega_arg":
                i=1
            else:
                if kwargs["phase"]== "Omega_cal":
                    i=2
                else:
                    if kwargs["phase"]=="carbonate":
                        i=5
                    else:
                        print "Wrong parameters for "+kwargs["phase"]
                        return -1
    if kwargs.has_key("temperature") and kwargs.has_key("salinity"):
        data1=kwargs["temperature"]
        data2=kwargs["salinity"]
        if kwargs["phase"] == "total_alk":
            i=3
        else:
            print "Wrong parameters for "+kwargs["phase"]
            return -1
    if kwargs.has_key("oxygen") and kwargs.has_key("density"):
        data1=kwargs["density"]
        data2=kwargs["oxygen"]
        if kwargs["phase"]=="dic":
            i=4
        else:
            print "Wrong parameters for "+kargs["phase"]
            return -1
    data1=np.array(data1)
    data2=np.array(data2)
    #len1=len(data1)
    #len2=len(data2)
    if data1.shape != data2.shape:
        print "The two data sets need to be the same size"
        return -1
    Tref=10.28 # degrees C
    Sref=33.889 # salinity
    Dref=26.01  # kg/m^3 potential density
    O2ref=138.46 # umol/kg oxygen concentration
    if i < 3:
        d1offset=Tref
        d2offset=O2ref
    if i==5:
        d1offset=Tref
        d2offset=O2ref
    if i==3:
        d1offset=Tref
        d2offset=Sref
    if i==4:
        d1offset=Dref
        d2offset=O2ref
    coef=np.zeros((6,4))
    coef[0,:]=[7.758, 1.42e-2, 1.62e-3, 4.24e-5]
    coef[1,:]=[1.112, 9.59e-2, 3.54e-3, 5.91e-4]
    coef[2,:]=[1.749, 0.147, 5.61e-3, 8.02e-4]
    coef[3,:]=[2246.67, -3.70, 67.79, -013.28]
    coef[4,:]=[2165.76, 80.75, -0.45, -0.052]
    coef[5,:]=[73.94, 5.85, 0.23, 0.040]
    #pdb.set_trace()
    value=coef[i,0]+coef[i,1]*(data1-d1offset)+coef[i,2]*(data2-d2offset)+coef[i,3]*(data1-d1offset)*(data2-d2offset)
    return value
