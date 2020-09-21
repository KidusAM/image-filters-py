""" This is the effects module written by Kidus Mulu (km3533) It does:
    1) compiles one image out of three by removing objects
    2) converts a PPM color file to a black and white file
    3) flips an image horizontally
    """
import numpy as np
import pdb
import pandas as pd
   

def object_filter(f1, f2, f3, final):
    '''
        Filters objects from three images by taking the majority
    '''
    with open(f1) as file1, open(f2) as file2, open(f3) as file3, \
        open(final, 'w') as output_file:
        image1 = get_image(file1)
        image2 = get_image(file2)
        image3, max_value = get_image(file3, giveMax=True)
        
        file_shp = image1.shape[-2::-1]
        fin_shp = image1.shape[1]*3, image1.shape[0]
        image1 = image1.reshape(fin_shp)
        image2 = image2.reshape(fin_shp)
        image3 = image3.reshape(fin_shp)
        
        final_image = np.zeros(fin_shp, dtype='uint16')
        for i in range(fin_shp[0]):
            for j in range(fin_shp[1]):
                    if image1[i,j] == image2[i,j]: final_image[i,j] = image1[i,j]
                    elif image1[i,j] == image3[i,j]: final_image[i,j] = image1[i,j]
                    else: final_image[i,j] = image3[i,j]
                    
            
        write_image(output_file, final_image, file_shp , max_value)
    
    
def horizontal_flip(f1, output):
    '''
        Horizontally flips an image and writes it to a new file
    '''
    with open(f1) as input_file, open(output, 'w') as output_file:
        image, max_dim = get_image(input_file, giveMax=True)
        
        file_shp = image.shape[0:2][::-1]
        fin_shp = image.shape[0], image.shape[1]*3  
        
        h_image = image[:,::-1]
        h_image = h_image.reshape(fin_shp)
        
        write_image(output_file, h_image, file_shp)
    

def shades_of_grey(f1, output):
    '''
    Converts PPM image to black and white
    '''
    with open(f1) as input_file, open(output, 'w') as output_file:
        image, max_value = get_image(input_file, giveMax=True)
        output_image = np.repeat(np.average(image, axis=2,),repeats=3, axis=1)
        write_image(output_file, output_image, image.shape[-2::-1], max_value)
        
        

def get_image(input_file, giveMax=False):
    ''' returns the image file as a numpy array with correct dimentions'''
    input_file.readline();
    dim = input_file.readline().split()[::-1]
    dim = int(dim[0]), int(dim[1]), 3
    max_value = int(input_file.readline())
    image = pd.read_csv(input_file, error_bad_lines=False, header=None, \
                        comment='#', sep=r'\s+', dtype='float16').values
    image= image[~np.isnan(image)].reshape(dim)
    return (image, max_value) if giveMax else image

def write_image(output_file, image, dimentions, max_value=255):
    """Writes a numpy array to a ppm image file"""
    
    output_file.write('P3\n')
    output_file.write(str(dimentions[0]) + " " + str(dimentions[1]) + "\n")
    output_file.write(str(max_value) + "\n")
    np.savetxt(output_file,image, fmt="%d" )