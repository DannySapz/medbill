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
Aceeptance Stories
++++++++++++++++++

| Scenario 01: Billing procedue code 76514 (Pacheymetry)
| Given that I have billed procedure code 76514,
| And will have to bill a diagnosis for this test,
| When I enter a diagnosis
| Then it will tell me if the diagnosis can be used for that procedure code
| And if not, it will show "False" and prompt for a new diagnosis.
