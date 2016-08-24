# Author:  Jonathan A. Webb
# Date:    December 20, 2014
# Purpose: This file contains all the core algorithms necessary to run
#          the Monte_Economix software package
#=====================================================================
# - This function determines the amount allocated for each monthly or
#   bi-monthly paycheck
import scipy.interpolate
import numpy as np

def Paycheck(SALLARY,FED_TAX,STATE_TAX,SOCIAL_SECURITY,
             MEDICARE,DENTAL,HEALTH,W2GRP,dispersement):
    
    PAYCHECK = 0.0
    SALLARY1 = SALLARY/12
    comparison  = 'Bimonthly'
    comparison2 = 'Two_Week'
    
    PAYCHECK = SALLARY1 - SALLARY1*FED_TAX - SALLARY1*STATE_TAX - \
        SALLARY1*SOCIAL_SECURITY - SALLARY1*MEDICARE - \
            DENTAL - HEALTH - W2GRP

    if(dispersement == comparison): PAYCHECK = PAYCHECK/2
    if(dispersement == comparison2): PAYCHECK = PAYCHECK*12/26
    
    return(PAYCHECK)
#=====================================================================
# - This function determines the daily value of the checking account
#   once known, monthly expenses are deducted
def Update_Checking_Account(days,CHECKING,RENT,PAY,LOANS,CAR,INTERNET,
                            PHONE,AINS,UTILITY,length,Rent_Pay_Date,
                            Loan_Pay_Date,Car_Pay_Date,Internet_Pay_Date,
                            Phone_Pay_Date,Ains_Pay_Date,Utility_Pay_Date,
                            Transfer_to_Savings,Transfer_Date,dispersement,
                            counter):
    
    New_Account_Value = CHECKING + 0.0
    comparison0 = 'Monthly'
    comparison  = 'Bimonthly'
    comparison2 = 'Two_Week'
    
    if days == Rent_Pay_Date:     New_Account_Value = New_Account_Value - RENT
    if days == Loan_Pay_Date:     New_Account_Value = New_Account_Value - LOANS
    if days == Car_Pay_Date:      New_Account_Value = New_Account_Value - CAR
    if days == Internet_Pay_Date: New_Account_Value = New_Account_Value - INTERNET
    if days == Phone_Pay_Date:    New_Account_Value = New_Account_Value - PHONE
    if days == Ains_Pay_Date:     New_Account_Value = New_Account_Value - AINS
    if days == Utility_Pay_Date:  New_Account_Value = New_Account_Value - UTILITY
    if days == Transfer_Date:     New_Account_Value = New_Account_Value - Transfer_to_Savings
    
    if days == 15 and dispersement == comparison: New_Account_Value = New_Account_Value + PAY
    if dispersement == comparison:
        if length == 28 and days == 28: New_Account_Value = New_Account_Value + PAY
        if length == 29 and days == 29: New_Account_Value = New_Account_Value + PAY
        if length > 28 and days == 30: New_Account_Value = New_Account_Value + PAY
    if dispersement == comparison0:
        if length == 28 and days == 28: New_Account_Value = New_Account_Value + PAY
        if length == 29 and days == 29: New_Account_Value = New_Account_Value + PAY
        if length > 28 and days == 30: New_Account_Value = New_Account_Value + PAY

    if dispersement == comparison2 and counter == 14: New_Account_Value = New_Account_Value + PAY



    return(New_Account_Value)

#=====================================================================
# - This function determines the daily value of the savings account
#   to include the monthly transfer of money from the checking account
#   to the savings account
def Update_Savings_Account(days,SAVINGS,Transfer_to_Savings,
                           Transfer_Date):
    
    New_Savings_Account = SAVINGS + 0.0
    if days == Transfer_Date: New_Savings_Account = New_Savings_Account + Transfer_to_Savings
    
    return(New_Savings_Account)

#=====================================================================
# - This function determines the daily value of the checking account
#   due to the deduction of large planned expenses
def Expected_Purchases(CHECKING,year,YR,days,DY,months,MT,EX):
    import itertools
    
    New_Account_Value = CHECKING
 
    number = 0
    for x in EX:
        if year == YR[number] and days == DY[number] and months == MT[number]:
            New_Account_Value = New_Account_Value - EX[number]
        number = number + 1

    return(New_Account_Value)

#=====================================================================
def Linear_Interpolation(Array1,Array_Center1,sample_size):
    y_interp = scipy.interpolate.interp1d(Array1,Array_Center1)
    final_value = y_interp(np.random.rand(sample_size))
    return (final_value)
#=====================================================================