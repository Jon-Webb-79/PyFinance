#!usr/bin/python

# Main program
# Author:  Jonathan A. Webb
#---------   Revisions   ----------
# Date:    March 02, 2015
#          - Updated to include more advanced features of numpy
#            scipy and pandas
#          December 28, 2015
#          - Original version drafted in traditional Python 2.6.9
#
# Purpose: This is hte framework program that integrates all of the subprograms necessary
#          to run the Python version of the Monte-Economix software package.  This program
#          reads in a users hisotrical variable expenses and makes a stochastic prediction
#          for th efuture of that persons personal bank account value
#==========================================================================================
# - This section of the code reads in all of the account and paycheck variables that are
#   necessary for determining the time dependent value of someones bank account.  The
#   Read_Line and Read_Two_Data_Points functions are found in the file Data_Parser.py
import Data_Parser
import pandas as pd
import numpy as np

input_file = '../Files.d/Input.txt'
inp = open(input_file,'r')

MTH=[]; DY1=[]; YER=[]; EXP=[]
sample_size     = Data_Parser.Read_Line(inp,1,'integer')
BEG_DAY         = Data_Parser.Read_Line(inp,1,'integer')
BEG_MONTH       = Data_Parser.Read_Line(inp,1,'integer')
BEG_YR          = Data_Parser.Read_Line(inp,1,'integer')
END_DAY         = Data_Parser.Read_Line(inp,1,'integer')
END_MONTH       = Data_Parser.Read_Line(inp,1,'integer')
END_YR          = Data_Parser.Read_Line(inp,1,'integer')
PAY_MONTH       = Data_Parser.Read_Line(inp,1,'integer')
PAY_DAY         = Data_Parser.Read_Line(inp,1,'integer')
PAY_YR          = Data_Parser.Read_Line(inp,1,'integer')
CHECKING        = Data_Parser.Read_Line(inp,1,'float')
SAVINGS         = Data_Parser.Read_Line(inp,1,'float')
FONEK           = Data_Parser.Read_Line(inp,1,'float')
SALLARY         = Data_Parser.Read_Line(inp,1,'float')
dispersement    = Data_Parser.Read_Line(inp,1,'string')
Krate           = Data_Parser.Read_Line(inp,1,'float')
FED_TAX         = Data_Parser.Read_Line(inp,1,'float')
STATE_TAX       = Data_Parser.Read_Line(inp,1,'float')
SOCIAL_SECURITY = Data_Parser.Read_Line(inp,1,'float')
MEDICARE        = Data_Parser.Read_Line(inp,1,'float')
DENTAL          = Data_Parser.Read_Line(inp,1,'float')
HEALTH          = Data_Parser.Read_Line(inp,1,'float')
W2GRP           = Data_Parser.Read_Line(inp,1,'float')

Data_Parser.Skip_Line(inp)

RENT,Rent_Pay_Date   = Data_Parser.Read_Two_Data_Points(inp,1,'float',2,
                                                        'integer')
CAR,Car_Pay_Date     = Data_Parser.Read_Two_Data_Points(inp,1,'float',2,
                                                        'integer')
PHONE,Phone_Pay_Date = Data_Parser.Read_Two_Data_Points(inp,1,'float',2,
                                                        'integer')
LOANS,Loan_Pay_Date  = Data_Parser.Read_Two_Data_Points(inp,1,'float',2,
                                                        'integer')
AINS,Ains_Pay_Date   = Data_Parser.Read_Two_Data_Points(inp,1,'float',2,
                                                        'integer')
INTERNET,Internet_Pay_Date = Data_Parser.Read_Two_Data_Points(inp,1,'float',2,
                                                              'integer')
UTILITY,Utility_Pay_Date = Data_Parser.Read_Two_Data_Points(inp,1,'float',2,
                                                            'integer')
Transfer_to_Savings,Transfer_Date = Data_Parser.Read_Two_Data_Points(inp,1,'float',2,
                                                                     'integer')

Data_Parser.Skip_Line(inp)
Data_Parser.Skip_Line(inp)

counter = 0
for line in inp:
    Read_Line = line.split()
    Column1 = int(Read_Line[0]); Column2 = int(Read_Line[1])
    Column3 = int(Read_Line[2]); Column4 = float(Read_Line[3])
    MTH.append(Column1); DY1.append(Column2)
    YER.append(Column3); EXP.append(Column4)
    counter = counter + 1
inp.close()

MT = np.array(MTH); DY = np.array(DY1)
YR = np.array(YER); EX = np.array(EXP)

#=======================================================================================###
#=======================================================================================###
#=========================                                    ==========================###
#=========================        EXPENSE READER BLOCK        ==========================###
#=========================                                    ==========================###
#=======================================================================================###
#=======================================================================================###
# - This section reads in data from all of the variable expense sheets.

File1 = '../Files.d/Misc.txt'
MISC_DATA = pd.read_table(File1,header=None,names = ['expense','month','day','year'],sep = '\s+')

File2 = '../Files.d/Groceries.txt'
GROC_DATA = pd.read_table(File2,header=None,names = ['expense','month','day','year'],sep = '\s+')

File3 = '../Files.d/Rest.txt'
REST_DATA = pd.read_table(File3,header=None,names = ['expense','month','day','year'],sep = '\s+')

File4 = '../Files.d/Bar.txt'
BAR_DATA = pd.read_table(File4,header=None,names = ['expense','month','day','year'],sep = '\s+')

File5 = '../Files.d/Gas.txt'
GAS_DATA = pd.read_table(File5,header=None,names = ['expense','month','day','year'],sep = '\s+')

#=======================================================================================###
#=======================================================================================###
#=========================                                    ==========================###
#=========================             PDF AND CDF            ==========================###
#=========================            CREATION BLOCK          ==========================###
#=========================                                    ==========================###
#=======================================================================================###
#=======================================================================================###
# - This section transforms the arrays of data from variable spending items into
#   a probability density function and then into a cummulative density function.

# - This block of code creates a CDF for each of the variable spending items and also
#   determines the center of each CDF histogram bin
Misc_hist, Misc_bin_edges = np.histogram(MISC_DATA['expense'],bins=60,normed=True)
Misc = np.cumsum(Misc_hist*np.diff(Misc_bin_edges))   # CDF
Misc_Center = (Misc_bin_edges[:-1] + Misc_bin_edges[1:])/2
Misc        = np.concatenate((np.array([0]),np.array(Misc)),axis=0)
Misc_Center = np.concatenate((np.array([0]),np.array(Misc_Center)),axis=0)

Groc_hist, Groc_bin_edges = np.histogram(GROC_DATA['expense'],bins=60,normed=True)
Groc = np.cumsum(Groc_hist*np.diff(Groc_bin_edges))   # CDF
Groc_Center = (Groc_bin_edges[:-1] + Groc_bin_edges[1:])/2
Groc        = np.concatenate((np.array([0]),np.array(Groc)),axis=0)
Groc_Center = np.concatenate((np.array([0]),np.array(Groc_Center)),axis=0)

Rest_hist, Rest_bin_edges = np.histogram(REST_DATA['expense'],bins=60,normed=True)
Rest = np.cumsum(Rest_hist*np.diff(Rest_bin_edges))   # CDF
Rest_Center = (Rest_bin_edges[:-1] + Rest_bin_edges[1:])/2
Rest        = np.concatenate((np.array([0]),np.array(Rest)),axis=0)
Rest_Center = np.concatenate((np.array([0]),np.array(Rest_Center)),axis=0)

Bar_hist, Bar_bin_edges = np.histogram(BAR_DATA['expense'],bins=60,normed=True)
Bar = np.cumsum(Bar_hist*np.diff(Bar_bin_edges))     # CDF
Bar_Center = (Bar_bin_edges[:-1] + Bar_bin_edges[1:])/2
Bar        = np.concatenate((np.array([0]),np.array(Bar)),axis=0)
Bar_Center = np.concatenate((np.array([0]),np.array(Bar_Center)),axis=0)

Gas_hist, Gas_bin_edges = np.histogram(GAS_DATA['expense'],bins=60,normed=True)
Gas = np.cumsum(Gas_hist*np.diff(Gas_bin_edges))     # CDF
Gas_Center = (Gas_bin_edges[:-1] + Gas_bin_edges[1:])/4
Gas        = np.concatenate((np.array([0]),np.array(Gas)),axis=0)
Gas_Center = np.concatenate((np.array([0]),np.array(Gas_Center)),axis=0)

#=======================================================================================###
#=======================================================================================###
#=========================                                    ==========================###
#=========================         INITIALIZE PROGRAM         ==========================###
#=========================                                    ==========================###
#=======================================================================================###
#=======================================================================================###
# - This section initializes all relevant variables for the Monte Carlo iterations
import Algorithm
import csv

output_file = open("../Files.d/Checking.csv","w")

# Function found in Algorithm.py
PAY = Algorithm.Paycheck(SALLARY,FED_TAX,STATE_TAX,SOCIAL_SECURITY,
                         MEDICARE,DENTAL,HEALTH,W2GRP,dispersement)

# indexing number of days for iteration
start = str(BEG_MONTH) + '/' + str(BEG_DAY) + '/' + str(BEG_YR)
end   = str(END_MONTH) + '/' + str(END_DAY) + '/' + str(END_YR)
date_index = pd.date_range(start,end)

#=======================================================================================###
#=======================================================================================###
#=========================                                    ==========================###
#=========================        MONTE CARLO PROGRAM         ==========================###
#=========================                                    ==========================###
#=======================================================================================###
#=======================================================================================###
import calendar
import random

random.seed(123456)
count = "NO"
counter = 0

i = 0
for x in date_index:
    day   = int(date_index[i].strftime('%d'))
    month = int(date_index[i].strftime('%m'))
    year  = int(date_index[i].strftime('%Y'))
    
    if dispersement == 'Two_Week' and day == PAY_DAY and month == PAY_MONTH and year == PAY_YR:
        count = "YES"
        counter = 14
    
    if count == "YES" and counter < 14:
        counter = counter + 1

    # Determine the length of each month
    length  = calendar.monthrange(year,month)[1]
    
    # updates checking account based on input file
    CHECKING = Algorithm.Update_Checking_Account(day,CHECKING,RENT,PAY,LOANS,CAR,INTERNET,
                                                 PHONE,AINS,UTILITY,length,Rent_Pay_Date,
                                                 Loan_Pay_Date,Car_Pay_Date,Internet_Pay_Date,
                                                 Phone_Pay_Date,Ains_Pay_Date,Utility_Pay_Date,
                                                 Transfer_to_Savings,Transfer_Date,dispersement,
                                                 counter)

    if count == "YES" and counter == 14:
        counter = 0

    # - This function is stored in Algorithm.py and is used to update the
    #   value of the savings account
    SAVINGS = Algorithm.Update_Savings_Account(day,SAVINGS,Transfer_to_Savings,Transfer_Date)
    
    # - This function updates the checking account based on expected large purchases
    #   indicated in the input file
    CHECKING = Algorithm.Expected_Purchases(CHECKING,year,YR,day,DY,month,MT,EX)
    
    # Hands off the checking term for the monte carlo iterations
    Checking_Transfer = CHECKING

    # Random samples for each spending type for n = sample_size
    MISC_EXPENSE = Algorithm.Linear_Interpolation(Misc,Misc_Center,sample_size)
    GROC_EXPENSE = Algorithm.Linear_Interpolation(Groc,Groc_Center,sample_size)
    REST_EXPENSE = Algorithm.Linear_Interpolation(Rest,Rest_Center,sample_size)
    BAR_EXPENSE  = Algorithm.Linear_Interpolation(Bar,Bar_Center,sample_size)
    GAS_EXPENSE  = Algorithm.Linear_Interpolation(Gas,Gas_Center,sample_size)
    
    
    # sums the value for each element in array
    total = MISC_EXPENSE + GROC_EXPENSE + REST_EXPENSE + BAR_EXPENSE + GAS_EXPENSE
    
    # Hands value back to Checking
    CHECKING = Checking_Transfer - np.mean(total)
    # Determines the standard deviation
    Sigma    = np.std(total)
    
    if month == 1:    month1 = 'Jan'
    elif month == 2:  month1 = 'Feb'
    elif month == 3:  month1 = 'Mar'
    elif month == 4:  month1 = 'Apr'
    elif month == 5:  month1 = 'May'
    elif month == 6:  month1 = 'Jun'
    elif month == 7:  month1 = 'Jul'
    elif month == 8:  month1 = 'Aug'
    elif month == 9:  month1 = 'Sep'
    elif month == 10: month1 = 'Oct'
    elif month == 11: month1 = 'Nov'
    else: month1 = 'Dec'
    
    new_date = month1 + ' ' + str(day) + ' ' + str(year)
    
    
    datawriter = csv.writer(output_file)
    data = [[new_date,CHECKING,CHECKING + 3*Sigma,CHECKING - 3*Sigma]]
    datawriter.writerows(data)

    i = i + 1
output_file.close()


#=======================================================================================###
#=======================================================================================###
#=========================                                    ==========================###
#=========================        VARIABLE DEFINITIONS        ==========================###
#=========================                                    ==========================###
#=======================================================================================###
#=======================================================================================###
# AINS          = A real value that represents the financial value of monthly auto      ###
#                 insurance payments                                                    ###
# Ains_Pay_Date = An integer value that represents the day of the month on which auto   ###
#                 insurance payments are made                                           ###
# BEG_DAY       = An integer value that represents the day of the month for which       ###
#                 financial tracking begins. Value range from 1 to 31                   ###
# BEG_MONTH     = An integer value that represents the month on which financial         ###
#                 tracking will begin.  Months range from 1-12.                         ###
# BEG_YR        = An integer value that represents the year of which financial tracking ###
#                 begins.                                                               ###
# CAR           = A real value that represents a monthly car payment                    ###
# Car_Pay_Date  = An integer value that represents the day of the month that a car      ###
#                 payment is due                                                        ###
# CHECKING      = A real value that represents the value of a personal checking account ###
# DY            = A series of integers expressed as an array that represent the day of  ###
#                 the month in which planned large expenses occur                       ###
# DENTAL        = A real value that represents the amount deducted from a paycheck to   ###
#                 cover dental insurance                                                ###
# dispersement  = A character string that reads either 'Bimonthly' or 'Monthly' that    ###
#                 informs the program when a paycheck should be dispersed in the code   ###
# END_DAY       = An integer value that represents the day of the month for which       ###
#                 financial tracking ends                                               ###
# END_MONTH     = An integer value that represents the month on which financial         ###
#                 tracking ends                                                         ###
# END_YR        = An integer value that represents the year on which financial tracking ###
#                 ends.                                                                 ###
# EX            = A series of real values that are expressed as an array, each          ###
#                 representing a planned large expense                                  ###
# FED_TAX       = A real value that represents the fraction of a paycheck deducted for  ###
#                 federal taxes                                                         ###
# FONEX         = A real value that represents the value of a 401k account              ###
# HEALTH        = A real value that represents the amount deducted from a paycheck to   ###
#                 cover health insurance                                                ###
# INTERNET      = A real value that represents the financial value of a monthly         ###
#                 internet payment                                                      ###
# Internet_Pay_Date = An integer value that represents the day of the month the         ###
#                     internet bill is paid                                             ###
# Krate         = A real value that represents the rate of 401k accrual                 ###
# LOANS         = A real value that represents the value of a monthly loan payment for  ###
#                 student loans                                                         ###
# MEDICARE      = A real value that represents the fraction of a paycheck deducted for  ###
#                 medicare                                                              ###
# MT            = A series of integer values expressed as an array that represent the   ###
#                 months of the year in which planned large expenses occur              ###
# Peak_XX_Value = A float value that represents the value of the largest element in one ###
#                 of the arrays (i.e. MISC_DATA, GROC_DATA, REST_DATA, BAR_DATA or      ###
#                 GAS_DATA)                                                             ###
# PHONE         = A real value that represents the value of a monthly phone payment     ###
# Phone_Pay_Date = An integer value that represents the day of the mony that the phone  ###
#                  payment is made                                                      ###
# RENT          = A real value that represents the monthly cost of apartment rent or a  ###
#                 monthly house mortgage                                                ###
# Rent_Pay_Date = An integer value that represents the day of the month on which rent   ###
#                 or a mortgage is due                                                  ###
# SALLARY       = A real value that represents a personal base sallry                   ###
# sample_size   = An integer value that represents the number of Monte Carlo trials to  ###
#                 determine the time dependent value of a bank account                  ###
# SAVINGS       = A real value that represents the value of a personal savings account  ###
# size_XX       = An integer value that represents the number of elements in one of the ###
#                 arrays (i.e. MISC_DATA, GROC_DATA, REST_DATA, BAR_DATA, or GAS_DATA)  ###
# STATE_TAX     = A real value that represents the fraction of a paycheck deducted for  ###
#                 state taxes                                                           ###
# SOCIAL_SECURITY = A real value that represents the fraction of a paycheck deducted    ###
#                   for social security                                                 ###
# UTILITY       = A float value that represents the financial value of a monthly        ###
#                 utility bill                                                          ###
# Utility_Pay_Date = An integer value that represents the day of the monyh the utility  ###
#                    bill is paid                                                       ###
# WidthX        = A real value that represents the width of a histogram bin             ###
# W2GRP         = A real value that represents deductions from a paycheck to cover      ###
#                 W2GRP costs                                                           ###
# XX_Bin_Center = A series of real values stored in an array, where each value          ###
#                 represents the center of a histogram bin for a variable spending      ###
#                 item (i.e. MISC, REST, GROC, BAR, GAS)                                ###
# XX_CDF        = A series of real values stored in an array, where each value          ###
#                 represents the normalized cummulative distribution function for a     ###
#                 variable spending item (i.e. MISC, REST, GROC, BAR, GAS)              ###
# XXX_DATA      = A real variable in the form of an array that represents the amount of ###
#                 spending on a given day in one of the variable categories such as     ###
#                 MISC, GROC, REST, BAR or GAS                                          ###
# XX_PDF        = A series of real values stored in an array where each value           ###
#                 represents the non-normalized value for the probability density       ###
#                 function for a variable spending item (i.e. MISC, GROC, REST, BAR     ###
#                 GAS)                                                                  ###
# XX_Upper_Limits = A series of real values stored in an array, where each value        ###
#                   represents the upper bound of a histogram bin                       ###
# YR            = A series of integer values that are expressed as a n array which      ###
#                 represent the year in which a planned large expense occurs            ###
#=======================================================================================###