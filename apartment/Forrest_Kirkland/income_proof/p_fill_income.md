ROOT_DIR dir is ~/BGit/Bryan_git/tom_bryan/apartment/Forrest_Kirkland

INCOME_DIR dir is {ROOT_DIR}/income_proof
OUT_DIR dir is {INCOME_DIR}/out/

INPUT_PDF is file {ROOT_DIR}/Compliance_Packet.pdf
  * This is the blank form template. READ-ONLY. Never modify it.

OUTPUT_PDF is file {OUT_DIR}/filled_out_income.pdf
  * This is the only file you create. All edits land here.

PREV_SCRIPT is file {INCOME_DIR}/fill_form.py
  * The python (PyMuPDF / fitz) script that filled the form last time.
  * It has the correct page coordinates, rotation handling (pages are stored
    rotated 90 degrees), fonts, and dark-blue ink color already worked out.
  * START FROM THIS SCRIPT. Copy it, then apply the CHANGES below. Do not
    re-derive coordinates that already worked.

PREV_OUTPUT_1 is file {INCOME_DIR}/filled_out_income.pdf
PREV_OUTPUT_2 is file {INCOME_DIR}/Completed_2_Tom_Apartment.pdf
  * Last run's outputs. READ-ONLY. Learn from them; they were mostly correct.
  * Everything they did is replicated EXCEPT what the CHANGES sections below say.

REFERENCE_SCAN_PAGES dir is {INCOME_DIR}/pages/
  * page_NN.jpeg + page_NN.OCR + page_NN.txt = the scanned hand-filled packet
    that the previous run was built from. Use these to locate rows, columns,
    and checkboxes when a change below needs a new coordinate.

BANK_STATEMENT is file {ROOT_DIR}/Bank/BoA_Bank_statement.pdf
DAD_INFO is file {ROOT_DIR}/dad_info.txt
  * Background facts about Tom (Thomas R. Starbuck) if a value is needed.

BACKUP_DIR dir is {OUT_DIR}/backup/

============================================================
HOW TO RUN
============================================================

* BACKUP STEP (do this FIRST, before generating anything):
  * If {OUTPUT_PDF} already exists, move it aside into {BACKUP_DIR} so the
    old run is never lost. Create {BACKUP_DIR} if missing.
  * If a file with the same name already sits in {BACKUP_DIR}, rename the
    one being moved by appending the file's last-modified date-time stamp
    (for example filled_out_income_2026-08-04_09-15-00.pdf) so nothing in
    the backup directory is ever overwritten.
  * After this step the output location must be empty so the new run
    writes to a clean path.
* Copy {PREV_SCRIPT} to a new script inside {INCOME_DIR} (for example
  fill_form_2.py). Keep the old script untouched.
* Change OUT in the script to {OUTPUT_PDF}. Create {OUT_DIR} if missing.
* Apply every change in the CHANGES sections below.
* After generating, render the changed pages to images and visually verify
  each change landed in the right box before declaring done.

PAGE NUMBERING NOTE
* The form prints its own page number at the bottom of each sheet ("Page #1",
  "Page #2", ...). The PDF page index is one higher because of the cover page.
* Each section header below gives both: the printed page number and the PDF
  page number. Trust the printed number when locating content; the script's
  T()/X() calls use the PDF page number.

GLOBAL RULE - SIGNATURES AND DATES
* Do NOT fill in any signature, any printed-name-next-to-signature line that
  the previous run treated as a signature, any signature date, or any place
  of signature. Leave them completely empty. They will be signed later with
  HelloSign.
* In the previous script this means REMOVE the signature/date lines on
  template pages 13, 14, 17, and 18 (the 'Thomas R. Starbuck' script-style
  entries and the '07/28/2026' dates). Non-signature typed values on those
  pages (property name, printed household name in headers, checkboxes) stay.

GLOBAL RULE - DOLLAR AMOUNTS ARE NOW ANNUAL
* Last time income amounts were entered monthly. This time the form wants
  annual amounts. The specific replacements are listed page by page below
  (monthly x 12).

============================================================
CHANGES vs LAST TIME
============================================================

Property: Woodlands At Forbes Lake

================================
Cover / checklist page (PDF Page #1 area, the packet checklist)
================================
* Add 4 check marks in the boxes for:
  * "Household Eligibility Certification"
  * "Household Eligibility Application (HEA)"
  * "Household Demographics"
  * "Authorization to Release Confidential Information"

* INCOME section of the checklist:
  * [x] Social Security Verification/Clarification by Telephone
  * [x] Pension Verification

* COMMISSION SPECIAL-NEEDS section:
  * [x] Disability Status Certification

* "Property Name":
   INCORRECT: (Empty)
   CORRECT: Woodlands At Forbes Lake

* "Resident Name":
   INCORRECT: (Empty)
   CORRECT: Tom Starbuck


================================
Printed "Page #1" (PDF page 2) - HEA Page 1
================================
* Check the box before "Initial Certification". The check-box is hard to
  see on the form; find it just before that word and place the X there.

================================
Printed "Page #2" (PDF page 3) - income rows 1-13
================================
* Row #7 (Social Security retirement, the row marked YES last time):
  * Put "1" in the first column, the "HH#" column, for row #7.
  * Column #3 amount: change FROM $1,291.70 (monthly) TO $15,500.40 (annual).  (Don't forget the $0.40 at the end of $15,500.40)

================================
Printed "Page #3" (PDF page 4) - income rows 14-19
================================
* Row #16 (Regular payments from trusts / pensions - the YES row):
  * Put "1" in the first "HH#" column for row #16.
  * Column #3, first amount line (LA County Sheriff pension):
    change FROM $2,689.50 TO $32,274.00 (annual).
  * Column #3, second amount line just below (PERS / Cal-PERS):
    change FROM $1,736.31 TO $20,835.72 (annual).

================================
Printed "Page #6" (PDF page 7) - assets rows 1-5
================================
* Row #2 Cash on Hand
  * Put "x" in the first "NO" column.
  * Do not put anything else on this row (except "NO" Column)

* Row #3 Checking Account(s):
  * Put "1" in the first "HH#" column.
  * Column #4 (interest rate): change TO 0% 
  * Column #5 (Annual Income, the far right column): $0.00 
* Row #4 Savings Account(s):
  * Put "1" in the first "HH#" column.
  * Column #4 (interest rate): change FROM 0% TO 0.04%
  * Column #5 (income from asset): change FROM $0 TO $32.79

================================
Printed "Page #7" (PDF page 8) - assets rows 6-10
================================
* Row #6 Debit Card(s): 
  * "X" in the "NO" column.  Not the "Yes" column.
  * Besides the "X" in "No" column, leave all other values empty. 
  * Remove the "Bank of America" under "Bank Name #1"
  * Remove "Last 4 Digits" value. "3799"


================================
Printed "Page #9" (PDF page 10) - assets rows 16-21
================================
* Row #20 "Have you received a tax refund in the last 12 months":
  put "1" in the first "HH#" column (column #1).
  * "interest Rate" column: enter "0%" (Row #20)
  * "Annual Income" column: enter "$0" (Row #20)

* Row #21 Real Estate Property: put "1" in the first "HH#" column.

* Row #21: Change amount
   Before: $4,747
   AFTER: $3,822
  * "interest Rate" column: enter "0%" (Row #21)
  * "Annual Income" column: enter "$0" (Row #21)

================================
Printed "Page #10" (PDF page 11) - PART 5
================================
* Last time the script drew a large blue "X" (two crossing lines) over the
  "PART 5:" header, striking the page out. DO NOT draw those lines this time
  (in the script: delete the two line() calls on template page 11).
* Also do NOT add the text "N/A - household has income; Part 5 does not
  apply" (delete that T() call).
* Part 5 is left clean and unmarked this time.

================================
Printed "Page #11" (PDF page 12) - PART 6
================================
* Keep the X on option box #1 as last time. Dad will SIGN in Box #1 later
  via HelloSign - leave any signature area there empty.


================================
(PDF page 14) Page Title "Househould Demographics" (Bottom of page says "Page 1 of 3")
================================
* "Household Relationship" (column #3):
   INCORRECT: "RENTER"
   CORRECT: "Head of Household"

* "Disability Status*" (column #6):
   INCORRECT: "No"
   CORRECT: "Not Disabled"


================================
(PDF page 16) Page Title "Househould Demographics" (Bottom of page says "Page 3 of 3")
================================
* Don't enter anything on this page.


============================================================
FOLLOW-UPS / ATTACHMENTS (do not put on the form; note for Bryan)
============================================================
* Row #20 tax refund ($4,747) needs external proof: a bank statement
  showing the $4,747 deposit. Source: {BANK_STATEMENT}.
* A "Cash on Hand" affidavit is still needed for the Row #2 cash amount.
* Output to stdout a reminder listing these two items at the end of the run.

============================================================
VERIFICATION
============================================================
* Render every page listed above from {OUTPUT_PDF} to images and confirm:
  * each new "1" sits inside the HH# column of the correct row
  * each replaced dollar amount shows the new annual value, not the old one
  * Part 5 page has no X lines and no N/A text
  * no signature or signature-date fields are filled anywhere
* Output to stdout:
  ----------------------------------------
  DONE: wrote {OUTPUT_PDF}
  ----------------------------------------
