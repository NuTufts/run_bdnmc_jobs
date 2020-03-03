import os,sys
from math import sqrt

"""
Generate list of points in (Y,m_chi)-space.
"""


def generate_param_file( param_file, alpha_d=0.5, Mv_scale=3.0 ):
    """ generate parameter values to calculate event rate 
    generates Y, the relic abundance, and M, the mass of the DM particle.
    In the file is also epsilon, the coupling parameter put into the run config file.
    """
    
    Y_base_list = [1.0,5.0]
    Y_expo_list = [-11,-10,-9,-8,-7]
    M_base_list = [1.0,5.0]
    M_expo_list = [-3,-2,-1,0]

    Y_val_list = []
    for b in Y_base_list:
        for ex in Y_expo_list:
            Y = b*pow(10,ex)
            Y_val_list.append(Y)

    M_val_list = []
    for b in M_base_list:
        for ex in M_expo_list:
            M = b*pow(10,ex)
            M_val_list.append(M)

    
    parfile = open(param_file,'w')
    print>>parfile,"epsilon",'\t',"Y",'\t',"M_chi",'\t',"M_v",'\t',"a_D"
    pars = []
    for Y in Y_val_list:
        for M in M_val_list:
            # convert to epsilon, the coupling parameter
            eps = sqrt(Y*pow(Mv_scale,4)*alpha_d)
            pars.append( (eps,Y,M) )
            print>>parfile,"%.2e"%(eps),'\t',"%.2e"%(Y),'\t',M,'\t',M*Mv_scale,'\t',alpha_d
    print "generated ",len(pars)," parameters into ",param_file
    parfile.close()


if __name__ == "__main__":

    generate_param_file( sys.argv[1] )


