"""
Created on Thu Apr  9 15:18:58 2020

@author: Kidus Mulu km3533
Effects module tester
"""
from effects import object_filter, shades_of_grey, horizontal_flip
def main():
    ''' This tests the effects module'''
    print("Portable Pixmap (PPM) Image Editor!")
    print("Choose the effect you would like to try:")
    print("1) object_filter")
    print("2) shades_of_grey")
    print("3) horizontal_flip")
    
    choice = int(input("Input a number: "))
    
    if choice == 1:
        f1_name = input("Enter an input file name (1 of 3): ")
        f2_name = input("Enter an input file name (2 of 3): ")
        f3_name = input("Enter an input file name (3 of 3): ")

        if f1_name[-3:] != 'ppm': f1_name += '.ppm'
        if f2_name[-3:] != 'ppm': f2_name += '.ppm'
        if f3_name[-3:] != 'ppm': f3_name += '.ppm'

        o_file = input("Enter name of output file: ")
        if o_file[-3:] != 'ppm': o_file += '.ppm'
        
        object_filter(f1_name, f2_name, f3_name, o_file)
        print(o_file, "created!")
        
    elif choice == 2:
        f_name = input("Enter an input file name: ")
        if f_name[-3:] != 'ppm': f_name += '.ppm'
        
        o_file = input("Enter name of output file: ")
        if o_file[-3:] != 'ppm': o_file += '.ppm'
        
        shades_of_grey(f_name, o_file)
        print(o_file, "created!")

    elif choice == 3:
        f_name = input("Enter an input file name: ")
        if f_name[-3:] != 'ppm': f_name += '.ppm'
        
        o_file = input("Enter name of output file: ")
        if o_file[-3:] != 'ppm': o_file += '.ppm'
        
        horizontal_flip(f_name, o_file)
        print(o_file, "created!")
        
main()
