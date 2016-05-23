===========
MedBill Pro 
===========

++++++++
Personas
++++++++

=======     ============================================================
Feature                             Description
=======     ============================================================
Name        Jane the Biller
Details     Is a medical biller.  She works full-time at an
            ophthalmologist's office.
Goals       Wants to be able to bill claims faster and more efficiently.
=======     ============================================================

++++++++++++++++
Problem Scenario
++++++++++++++++

=================     ====================     =======================
Problem Scenarios     Current Alternatives     Value Proposition
=================     ====================     =======================
Jane the Biller       Making a list of all     Creating a program
spends most of        diagnosis codes for      that can tell a
her time checking     each test.               biller if the diagnosis
if the diagnosis                               code entered can be
codes billed by                                billed with test done.
the doctor is
billable with the
tests done.
=================     ====================     =======================

++++++++++++
User Stories
++++++++++++

As Jane the Biller, I want to be able to bill the claims faster without having
to flip through diagnoses books which kills time.

++++++++++++++++++
Acceptance Stories
++++++++++++++++++

| Scenario 01: Billing procedue code 76514 (Pachymetry)
| Given that I have billed/entered procedure code 76514,
| And will have to bill/enter a diagnosis code for this test,
| When I enter a diagnosis code
| Then it will tell me if the diagnosis can be used for that procedure code
| And if not, it will list all the diagnosis codes available and prompt to
| try again.

++++++++
Example:
++++++++

.. code:: console

>>> 
Patient name: John Smith
Date of birth(MM/DD/YYYY): 07/04/1948
Insurance: bcbs
Invalid insurance. Available insurances:
1199
Aetna
BCBS
Cigna
GHI
HIP
Fidelis
Oxford
Metroplus
Medicare
Medicaid
AARP
Healthfirst
HealthPlus
United Healthcare
Insurance: BCBS
Procedure code(76512, 76514, 76519, 92025, 92235):76514
Diagnosis code: H40.123
Diagnosis doesn't match. Choose from these diagnoses:
H40,001 Preglaucoma, unspecified, right eye
Q15.0 Congenital glaucoma
T86.841 Corneal transplant failure
T86.840 Corneal transplant rejection
H40.041 Steroid responder, right eye
H40.043 Steroid responder, bilateral
H40.042 Steroid responder, left eye
Z98.42 Cataract extraction status, left eye
Z98.41 Cataract extraction status, right eye
H40.003 Preglaucoma, unspecified, bilateral
H40.002 Preglaucoma, unspecified, left eye
H40.023 Open angle with borderline findings, high risk, bilateral
H40.022 Open angle with borderline findings, high risk, left eye
H40.021 Open angle with borderline findings, high risk, right eye
H18.12 Bullous keratopathy, left eye
H18.13 Bullous keratopathy, bilateral
H18.11 Bullous keratopathy, right eye
H40.89 Other specified glaucoma
Z98.83 Filtering (vitreous) bleb after glaucoma surgery status
H40.051 Ocular hypertension, right eye
H40.052 Ocular hypertension, left eye
H40.053 Ocular hypertension, bilateral
H18.20 Unspecified corneal edema
H40.9 Unspecified glaucoma
H40.031 Anatomical narrow angle, right eye
H40.032 Anatomical narrow angle, left eye
H40.033 Anatomical narrow angle, bilateral
H42 Glaucoma in diseases classified elsewhere
H40.012 Open angle with borderline findings, low risk, left eye
H40.013 Open angle with borderline findings, low risk, bilateral
H40.011 Open angle with borderline findings, low risk, right eye
Diagnosis code: H40.023
********************************************************************************
SUPERBILL                     John Smith for 5/23/2016
********************************************************************************
Insurance: BCBS
Date of birth: 07/04/1948
Procedure code(s): 76514
Diagnosis code(s): Open angle with borderline findings, high risk, bilateral

2016-05-23 21:23:37.184765

Every new superbill entered will be saved to a file named superbill.txt.  See
below:

.. code: console

********************************************************************************
SUPERBILL                     John Smith for 5/23/2016
********************************************************************************
Insurance: BCBS
Date of birth: 07/04/1948
Procedure code(s): 76514
Diagnosis code(s): Open angle with borderline findings, high risk, bilateral
