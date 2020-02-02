#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:12:56 2020

@author: fatimaal-hussein
"""


'''
###
Assignment 1 - File sorting
###

For this assignment, you will categorize all files
in the pertaining folders.

Files with axxxxxxx.txt will go in folder A
Files with bxxxxxxx.txt will go in folder b
Files with cxxxxxxx.txt will go in folder c
Files with dxxxxxxx.txt will go in folder d

You first will need to make these folders and then
have python sort through the different files and move
them into the their corresponding folders.

'''

# Instructions for File Sorting Project

#%% Create Folders
import os

path_a = '/Users/fatimaal-hussein/Desktop/Timas_homework/1_file_sorting/data/A Folder'
path_b = '/Users/fatimaal-hussein/Desktop/Timas_homework/1_file_sorting/data/B Folder'
path_c = '/Users/fatimaal-hussein/Desktop/Timas_homework/1_file_sorting/data/C Folder'
path_d = '/Users/fatimaal-hussein/Desktop/Timas_homework/1_file_sorting/data/D Folder'



if os.path.isdir(path_a) is False:
    os.mkdir(path_a)

if os.path.isdir(path_b) is False:
    os.mkdir(path_b)
    
if os.path.isdir(path_c) is False:
   os.mkdir(path_c)
    
if os.path.isdir(path_d) is False:
    os.mkdir(path_d)
    
   




#%% Tell python the directory/location of the files

path = '/Users/fatimaal-hussein/Desktop/Timas_homework/1_file_sorting/data/'
file_list = os.listdir(path)



#%% Sort by the first letter for each file
# Move all the same letters in the correct folder

'''
for each file in this file list, 
    check the first letter of each file 
        if the first letter is a 
            then put it in a folder 
        if the first letter is b 
            then put it in the b folder 
        if the first letter is c
            then put in the c folder 
        if first letter of file is d 
            then put in d folder
'''
#%%

import shutil


for counter, file_name in enumerate(file_list):    
    print(file_name)
    if file_name[0] is 'a':
        print('hey this file_name is a')
        
        shutil.copy(path + file_name, path + 'A Folder/' + file_name)
    
        
        
    elif file_name[0] is 'b':
        print('hey this file_name is b')
        
        shutil.copy(path + file_name, path + 'B Folder/' + file_name)
        
    elif file_name[0] is 'c':
        print('hey this file_name is c')
        
        shutil.copy(path + file_name, path + 'C Folder/' + file_name)
        
    elif file_name[0] is 'd':
        print('hey this file_name is d')
        
        shutil.copy(path + file_name, path + 'D Folder/' + file_name)
        
#%%
    
        




   #print(file_list[counter])
    #print(counter, file_name)


''' IF (file has an a)
    THEN move to a folder
    If(file has b)
    THEN move to b folder
    If(file has c)
    Then move to c folder
    if (file  has d)
    Then move to d folder
    '''
    

