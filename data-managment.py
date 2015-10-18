# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 2015
@author: stagforyeah
"""
import pandas
import numpy

# reading input
data = pandas.read_csv('nesarc_pds.csv', low_memory=False)

print ("data loaded. summary:")
print ("number of observations:" + str(len(data))) #number of observations (rows)
print ("number of variables:" + str(len(data.columns))) # number of variables (columns)

# load relevant data
data['BUILDTYP'] = data['BUILDTYP'].convert_objects(convert_numeric=True)
data['NUMPERS'] = data['NUMPERS'].convert_objects(convert_numeric=True)
data['FATHERIH'] = data['FATHERIH'].convert_objects(convert_numeric=True)
data['MOTHERIH'] = data['MOTHERIH'].convert_objects(convert_numeric=True)
data['S7Q1'] = data['S7Q1'].convert_objects(convert_numeric=True)

sub=data.copy()

# recode missing values to python missing (NaN)
sub['BUILDTYP']=sub['BUILDTYP'].replace(99, numpy.nan)
sub['S7Q1']=sub['S7Q1'].replace(9, numpy.nan)

print 'counts for BUILDTYP with 99 set to NAN and number of missing requested'
c1 = sub['BUILDTYP'].value_counts(sort=False, dropna=False)
p1 = sub['BUILDTYP'].value_counts(sort=False, normalize=True)
df1 = pandas.concat([c1, p1], axis=1, join='inner')
df1.columns = ['BUILDTYP', 'BUILDTYP %']
print df1
print 'counts for S7Q1 with 9 set to NAN and number of missing requested'
c2 = sub['S7Q1'].value_counts(sort=False, dropna=False)
p2 = sub['S7Q1'].value_counts(sort=False, normalize=True)
df2 = pandas.concat([c2, p2], axis=1, join='inner')
df2.columns = ['S7Q1', 'S7Q1 %']
print df2

#new PARENTHH variable, categorical 1 through 6
def PARENTHH (row):
   if row['FATHERIH'] == 1 and row['MOTHERIH'] == 1:
      return 3
   if row['FATHERIH'] == 1 :
      return 2
   if row['MOTHERIH'] == 2:
      return 1
   else:
      return 0
sub['PARENTHH'] = sub.apply (lambda row: PARENTHH (row),axis=1)

print 'counts for each household parent group'
c3 = sub['PARENTHH'].value_counts(sort=False)
print 'percentages for each household parent group'
p3 = sub['PARENTHH'].value_counts(sort=False, normalize=True)
df3 = pandas.concat([c3, p3], axis=1, join='inner')
df3.columns = ['PARENTHH', 'PARENTHH %']
print df2
# quartile split
print 'NUMPERS - 3 categories - tertile'
sub['NUMPERS4GR']=pandas.qcut(sub.NUMPERS, 3)
c4 = sub['NUMPERS4GR'].value_counts(sort=False, dropna=True)
print(c4)
#crosstabs evaluating which ages were put into which AGEGROUP3
print (pandas.crosstab(sub['NUMPERS4GR'], sub['NUMPERS']))
#frequency distribution for NUMPERS4GR
print 'counts for NUMPERS4GR'
c10 = sub['NUMPERS4GR'].value_counts(sort=False)
print 'percentages for NUMPERS4GR'
p10 = sub['NUMPERS4GR'].value_counts(sort=False, normalize=True)
df4 = pandas.concat([c10, p10], axis=1, join='inner')
df4.columns = ['NUMPERS4GR', 'NUMPERS4GR %']
print df3