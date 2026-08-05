ROOT_DIR dir is ~/BGit/Bryan_git/tom_bryan/apartment/Forrest_Kirkland/clarification

IN_DIR dir is {ROOT_DIR}/in/
OUT_DIR dir is {ROOT_DIR}/out/

INPUT_PDF is file {IN_DIR}/clarification.pdf
  * This is the blank form template. READ-ONLY. Never modify it.
  * Single page, 612 x 1008 points, no rotation.

OUTPUT_PDF is file {OUT_DIR}/filled_out_clarification.pdf
  * This is the only file you create. All edits land here.
  * Start it as a copy of {INPUT_PDF}, then type the values from the
    CHANGES sections below onto it.

FILL_SCRIPT is file {ROOT_DIR}/fill_clarification.py
  * The python (PyMuPDF / fitz) script this prompt creates and re-runs.
  * If it already exists from a previous run, reuse it and only update the
    values and coordinates that changed. If it does not exist, create it.

REFERENCE_SCRIPT is file ~/BGit/Bryan_git/tom_bryan/apartment/Forrest_Kirkland/income_proof/fill_form.py
  * READ-ONLY reference from an earlier packet. It shows the working
    technique: PyMuPDF insert_text, fonts, and dark-blue ink color.
  * Copy the technique into {FILL_SCRIPT}. Do NOT reuse its coordinates,
    its input file, or its output file — that was a different form. Do not
    read or write any other file outside {ROOT_DIR}.

BACKUP_DIR dir is {OUT_DIR}/backup/

============================================================
HOW TO RUN
============================================================

* BACKUP STEP (do this FIRST, before generating anything):
  * If {OUTPUT_PDF} already exists, move it aside into {BACKUP_DIR} so the
    old run is never lost. Create {BACKUP_DIR} if missing.
  * If a file with the same name already sits in {BACKUP_DIR}, rename the
    one being moved by appending the file's last-modified date-time stamp
    (for example filled_out_clarification_2026-08-05_09-15-00.pdf) so
    nothing in the backup directory is ever overwritten.
  * After this step the output location must be empty so the new run
    writes to a clean path.
* Render {INPUT_PDF} to an image and look at it to find the exact boxes
  and lines named in the CHANGES sections below, then work out the
  coordinates for each value.
* Create or update {FILL_SCRIPT} so it reads {INPUT_PDF}, writes every
  value from the CHANGES sections, and saves to {OUTPUT_PDF}. Create
  {OUT_DIR} if missing.
* Run {FILL_SCRIPT}.
* After generating, render {OUTPUT_PDF} to an image and visually verify
  each value landed in the right box before declaring done.
* This prompt is re-runnable: running it again refills the same values by
  making a fresh output copy from the input template.

GLOBAL RULE - SIGNATURES AND DATES OF SIGNATURE
* Do NOT fill in any signature line or any date line that sits next to a
  signature. Leave them completely empty. They will be signed later with
  HelloSign. The "Date" field called out in the CHANGES below is the form's
  own date field, not a signature date — fill that one.

============================================================
CHANGES - VALUES TO FILL
============================================================

Property: Woodlands At Forbes Lake

================================
Header Form
================================


* Initial Certification: (If in the circle solid)

* Date of Clarificaiton:
   CORRECT: Aug 5th, 2026

* "Date":
   INCORRECT: (Empty)
   CORRECT: Aug 5th, 2026

* "Resident Name":
   INCORRECT: (Empty)
   CORRECT: Tom Starbuck


================================
Questions Section
================================
* Question #1:
  * Put the text below in this in quotes. Put it into the line below question number #1. 
  * "Is your property fully paid off?"

* Question #2:
  * Put the text below in this in quotes. Put it into the line below question number #2. 
  * "Is there anything you have to paid on your property outside of Property tax?"

* Question #3:
  * Put the text below in this in quotes. Put it into the line below question number #3. 
  * "Do you plan on your real estate selling in the next couple of months?"



================================
Answers Section
================================
* Answer #1:
  * Put the text below in this in quotes. Put it into the line below Answer number #1. 
  * "Yes. It is fully paid off"

* Answer #2:
  * Put the text below in this in quotes. Put it into the line below Answer number #2. 
  * "No.  There is nothing to paid on my property outside of Property tax"

* Answer #3:
  * Put the text below in this in quotes. Put it into the line below Answer number #3. 
  * "No.  I do not plan on my real estate selling in the next couple of months"




============================================================
VERIFICATION
============================================================
* Render {OUTPUT_PDF} to an image and confirm:
  * the two date fields show Aug 5th, 2026
  * Resident Name shows Tom Starbuck
  * each question text sits on the line below its question number
  * each answer text sits on the line below its answer number
  * no signature line or signature-date line is filled
  * {INPUT_PDF} is byte-identical to before the run
* Output to stdout:
  ----------------------------------------
  DONE: wrote {OUTPUT_PDF}
  ----------------------------------------
