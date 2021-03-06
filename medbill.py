#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Medbill pro program"""


from datetime import datetime
import diagnosis


NOW = datetime.now()
#Input patient's name.
NAME = raw_input('Patient name: ')
#Input patient's date of birth.
DATE = raw_input('Date of birth(MM/DD/YYYY): ')
PROCEDURE_LIST = ['76512', '76514', '76519', '92025', '92235']
INSURANCE_LIST = ['1199', 'Aetna', 'BCBS', 'Cigna', 'GHI', 'HIP', 'Fidelis',
                  'Oxford', 'Metroplus', 'Medicare', 'Medicaid', 'AARP',
                  'Healthfirst', 'HealthPlus', 'United Healthcare']


#Input patient's insurance.  If not on the insurance list, will print out all
#available insurances.
while True:
    INSURANCE = raw_input('Insurance: ')
    if INSURANCE in INSURANCE_LIST:
        break
    else:
        print 'Invalid insurance. Available insurances:'
        for insurance in INSURANCE_LIST:
            print insurance

#Input procedure code that was performed on the patient.  Shows which procedure
#codes are availabe.
while True:
    PROCEDURE = raw_input('Procedure code(76512, 76514, 76519, 92025, 92235):')
    if PROCEDURE not in PROCEDURE_LIST:
        print 'Invalid procedure code'
    else:
        break

#Input diagnosis code. If diagnosis code does not match the procedure code
#that was entered previously, will list all the diagnosis that are billable
#for the procedure done.
while True:
    DIAGNOSIS = raw_input('Diagnosis code: ')
    INVALID_CODE = 'Diagnosis doesn\'t match. Choose from these diagnoses:'
    if DIAGNOSIS in diagnosis.DX_92025:
        DIAGNOSIS = diagnosis.DX_92025[DIAGNOSIS]
        break
    elif DIAGNOSIS in diagnosis.DX_76519:
        DIAGNOSIS = diagnosis.DX_76519[DIAGNOSIS]
        break
    elif DIAGNOSIS in diagnosis.DX_92235:
        DIAGNOSIS = diagnosis.DX_92235[DIAGNOSIS]
        break
    elif DIAGNOSIS in diagnosis.DX_76514:
        DIAGNOSIS = diagnosis.DX_76514[DIAGNOSIS]
        break
    elif DIAGNOSIS in diagnosis.DX_76512:
        DIAGNOSIS = diagnosis.DX_76512[DIAGNOSIS]
        break
    else:
        if PROCEDURE == '92025':
            print INVALID_CODE
            for keys, values in diagnosis.DX_92025.iteritems():
                print keys, values
        elif PROCEDURE == '76519':
            print INVALID_CODE
            for keys, values in diagnosis.DX_76519.iteritems():
                print keys, values
        elif PROCEDURE == '92235':
            print INVALID_CODE
            for keys, values in diagnosis.DX_92235.iteritems():
                print keys, values
        elif PROCEDURE == '76514':
            print INVALID_CODE
            for keys, values in diagnosis.DX_76514.iteritems():
                print keys, values
        elif PROCEDURE == '76512':
            print INVALID_CODE
            for keys, values in diagnosis.DX_76512.iteritems():
                print keys, values


#Prints all the user input on the screen.
SUPERBILL = '*' * 80 + '\n'
SUPERBILL += 'SUPERBILL {0:>30} for ' + '{0}/{1}/{2}'.format(NOW.month, NOW.day,
                                                             NOW.year) + '\n'
SUPERBILL += '*' * 80 + '\n'
SUPERBILL += 'Insurance: {1}\n'
SUPERBILL += 'Date of birth: {2}\n'
SUPERBILL += 'Procedure code(s): {3}\n'
SUPERBILL += 'Diagnosis code(s): {4}\n'
SUPERBILL = SUPERBILL.format(NAME, INSURANCE, DATE, PROCEDURE, DIAGNOSIS)

print SUPERBILL

#Saves each superbill to a file named superbill.txt to be printed if needed.
SAVEFILE = open('superbill.txt', 'w')
SAVEFILE.write(SUPERBILL)
SAVEFILE.close()


if __name__ == '__main__':
    print NOW
