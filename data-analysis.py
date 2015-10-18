# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 2015

@author: stagforyeah
"""
import pandas
import numpy

# reading input
data = pandas.read_csv('nesarc_pds.csv', low_memory=False)

print ("data loaded. summary:")
print ("number of obseravations:" + str(len(data))) #number of observations (rows)
print ("number of variables:" + str(len(data.columns))) # number of variables (columns)

# load relevant data
data['BUILDTYP'] = data['BUILDTYP'].convert_objects(convert_numeric=True)
data['NUMPERS'] = data['NUMPERS'].convert_objects(convert_numeric=True)
data['FATHERIH'] = data['FATHERIH'].convert_objects(convert_numeric=True)
data['MOTHERIH'] = data['MOTHERIH'].convert_objects(convert_numeric=True)
data['S7Q1'] = data['S7Q1'].convert_objects(convert_numeric=True)

#counts and percentages (i.e. frequency distributions) for each variable
print ("BUILDTYP:TYPE OF BUILDING FOR HOUSEHOLD")
c1 = data['BUILDTYP'].value_counts(sort=False)
print ("BUILDTYP:TYPE OF BUILDING FOR HOUSEHOLD percentages")
p1 = data['BUILDTYP'].value_counts(sort=False, normalize=True)
df1 = pandas.concat([c1, p1], axis=1, join='inner')
df1.columns = ['BUILDTYP', 'BUILDTYP %']
print df1
print ("NUMPERS:NUMBER OF PERSONS IN HOUSEHOLD")
c2 = data['NUMPERS'].value_counts(sort=False)
print ("NUMPERS:NUMBER OF PERSONS IN HOUSEHOLD percentages")
p2 = data['NUMPERS'].value_counts(sort=False, normalize=True)
df2 = pandas.concat([c2, p2], axis=1, join='inner')
df2.columns = ['NUMPERS', 'NUMPERS %']
print df2
print ("FATHERIH:FATHER OF RESPONDENT IN HOUSEHOLD")
c3 = data['FATHERIH'].value_counts(sort=False)
print ("FATHERIH:FATHER OF RESPONDENT IN HOUSEHOLD percentages")
p3 = data['FATHERIH'].value_counts(sort=False, normalize=True)
df3 = pandas.concat([c3, p3], axis=1, join='inner')
df3.columns = ['FATHERIH', 'FATHERIH %']
print df3
print ("MOTHERIH:MOTHER OF RESPONDENT IN HOUSEHOLD")
c4 = data['MOTHERIH'].value_counts(sort=False)
print ("MOTHERIH:MOTHER OF RESPONDENT IN HOUSEHOLD percentages")
p4 = data['MOTHERIH'].value_counts(sort=False, normalize=True)
df4 = pandas.concat([c4, p4], axis=1, join='inner')
df4.columns = ['MOTHERIH', 'MOTHERIH %']
print df4
print ("S7Q1:EVER HAD STRONG FEAR OR AVOIDANCE OF SOCIAL SITUATION")
c5 = data['S7Q1'].value_counts(sort=False)
print ("S7Q1:EVER HAD STRONG FEAR OR AVOIDANCE OF SOCIAL SITUATION percentages")
p5 = data['S7Q1'].value_counts(sort=False, normalize=True)
df5 = pandas.concat([c5, p5], axis=1, join='inner')
df5.columns = ['S7Q1', 'S7Q1 %']

print df5
