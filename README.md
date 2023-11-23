README: Updating CSV Records in Updated_List Folder

Overview
This document provides an overview of the process for updating CSV records in the Knack_List folder using the Complete_list CSV. The purpose of this process is to incorporate any additional or modified records from the Complete_list CSV into the Knack_List CSV. The comparison is based on a primary key present in both CSVs, ensuring accurate identification of extra or changed records.

Workflow
Source CSVs:

Knack_List Folder: Contains the original CSV with records extracted on a specific date (e.g., 10/01/2023).
Complete_list CSV: Contains an updated set of records, potentially with additional or modified entries, extracted at a later date (e.g., 11/01/2023).
Primary Key Comparison:

The update process relies on a primary key present in both CSVs. This key is used to identify corresponding records between the Knack_List and Complete_list CSVs.
Record Update:

For each record in the Complete_list CSV:

If the record's primary key is not present in the Knack_List CSV, it is considered an extra record and is added to the Atty_Email_Date CSV.
If the record's primary key is present but with differences in data (e.g., timekeeper status), the record in the Knack_List CSV is updated with the values from the Complete_list CSV.

Example:

If an attorney's status changes from "Active" to "Inactive" in the Complete_list CSV, the corresponding record in the Knack_List CSV will be updated to reflect this change.
Usage:

This process is designed to be executed periodically to ensure that the records in the Knack_List CSV are up-to-date based on the latest data in the Complete_list CSV.

Automation:

Consideration should be given to automating this update process to streamline the workflow and ensure timely updates.
Implementation Details

Requirements:
Python (or another programming language)
Libraries for CSV handling (e.g., pandas)
Proper file and folder access permissions

Steps:
Load CSVs:

Read both the Knack_List and Complete_list CSVs into data structures for comparison.

Primary Key Comparison:

Identify the primary key(ID) present in both CSVs and use it to match records.

Update Process:
Iterate through records in the Complete_list CSV.
Check if the record's primary key is in the Knack_List CSV.
Update or add records accordingly.

Write Changes:
Save the updated Knack_List CSV with the incorporated changes with the name of Atty_Email_Date in Updated_List.
