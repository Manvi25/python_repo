import numpy as np
import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')
def floor_ceil():

    np.set_printoptions(legacy='1.13')
    n="1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"

    new_arr=list(float(i) for i in n.split(' '))

    n_f=np.floor(new_arr)
    n_c=np.ceil(new_arr)
    n_r=np.rint(new_arr)

    logging.info("%s \n%s \n%s \n",n_f,n_c,n_r)
    return n_f,n_c,n_r