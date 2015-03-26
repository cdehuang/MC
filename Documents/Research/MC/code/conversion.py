#
#	chuang
#	02.01.15
#
#	A program to convert files with the wrong format for the monte carlo into files with the right format for the monte carlo. Currently just does .csv to .dat
#

import numpy as np
import astropy.io.ascii as ascii


def make_observation_files(input_file ='../data/all_hst_surveys.csv', output_fname='file', output_loc='../data/'):
    """
        Take a .csv containing data from multiple surveys (determined by the limiting magnitudes) and separate it into different files.
        
        Inputs:
        input_file: The input .csv containing all the data
        output_fname: The formatting for the output files
        output_loc: The directory to output the files
    """
    array = np.recfromcsv(input_file)
    limiting_mag = arr['limiting_mag_5sigma_ab']
    surveys = set(limiting_mag)
    num = len(set(limiting_mag))
    print("Converting {} into {} files".format(input_file, num))
    ff = 0
    filelist = []
    for i in surveys:
        indexes = np.where(limiting_mag == i)[0]
        new_rec_array = array[indexes]
        filename = output_loc + '{}_{}.dat'.format(output_fname, i)
        ascii.write(new_rec_array, filename)
        print("Made new file {}_{}.dat".format(output_fname, i))
        filelist.append(filename)
        ff += 1
    print("Made {} new files. Saved in {}".format(ff, output_loc))
    return filelist


    
