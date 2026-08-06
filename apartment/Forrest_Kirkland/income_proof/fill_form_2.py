#!/usr/bin/env python3
"""Run 2: fill the blank Compliance_Packet.pdf.
Copy of fill_form.py with the p_fill_income.md CHANGES applied:
annual (not monthly) income amounts, HH# column '1's, checklist checkmarks,
no signatures/dates (HelloSign later), Part 5 left clean."""
import fitz, os

BASE = os.path.expanduser('~/BGit/Bryan_git/tom_bryan/apartment/Forrest_Kirkland')
SRC = os.path.join(BASE, 'Compliance_Packet.pdf')
OUT_DIR = os.path.join(BASE, 'income_proof', 'out')
OUT = os.path.join(OUT_DIR, 'filled_out_income.pdf')
os.makedirs(OUT_DIR, exist_ok=True)

PROP = 'WOODLANDS AT FORBES LAKE'
HH   = 'THOMAS R. STARBUCK'
SIZE = '1'

FONT = 'helv'          # typed answers
FB   = 'hebo'          # bold, used for X marks
INK  = (0, 0, 0.55)    # dark blue "ink" so answers stand out from the form

doc = fitz.open(SRC)
ROT = 90   # pages are stored rotated 90 deg; glyphs need matching rotation


def T(pno, x, y, text, size=9, font=FONT, color=INK):
    """Insert text using display-space (rotated) coordinates."""
    pg = doc[pno - 1]
    pt = fitz.Point(x, y) * pg.derotation_matrix
    pg.insert_text(pt, text, fontname=font, fontsize=size, color=color,
                   rotate=ROT)


def X(pno, x, y, size=11):
    """centred X mark"""
    T(pno, x - size * 0.33, y, 'X', size, FB)


def circle(pno, x0, y0, x1, y1):
    pg = doc[pno - 1]
    r = fitz.Rect(x0, y0, x1, y1) * pg.derotation_matrix
    pg.draw_oval(r, color=INK, width=1.1)


def box_check(pno, x, y):
    X(pno, x, y, 10)


# Yes / No column centres inside the Part 2 & Part 4 grids; HH# column left of Yes
YES, NO = 68.0, 99.0
HHN = 42.0

# =============================================== template p1 (cover checklist)
T(1, 190, 90, 'Woodlands At Forbes Lake', 10)   # Property Name line
T(1, 185, 110, 'Tom Starbuck', 10)              # Resident Name line
box_check(1, 68, 205)     # Household Eligibility Certification
box_check(1, 68, 225)     # Household Eligibility Application (HEA)
box_check(1, 69, 265)     # Household Demographics
box_check(1, 67, 282)     # Authorization to Release Confidential Information
box_check(1, 85, 428)     # INCOME: Social Security Verification/Consent
box_check(1, 336, 388)    # INCOME: Pension Verification
box_check(1, 84, 573)     # COMMISSION: Disability Status Certification

# ---------------------------------------------------------------- headers
# HEA pages (template 2..13) share one header block; demographics page 14 differs.
for p in range(2, 14):
    T(p, 30, 82, PROP, 9)
    T(p, 30, 119, HH, 9)
    T(p, 500, 120, SIZE, 9)
T(14, 41, 94, PROP, 9)
T(14, 41, 137, HH, 9)

# =============================================== template p2  (scan page_01)
# PART 1 - head of household row
T(2, 122, 323, 'THOMAS R STARBUCK', 10)
T(2, 340, 323, '10/15/1945', 10)
T(2, 420, 323, '7741', 10)
circle(2, 558, 306, 586, 324)          # "N/A" (not a student) circled
X(2, 320, 169, 10)                     # Certification type: Initial Certification

# =============================================== template p3  (scan page_02)
# rows 1-13; only #7 is Yes
rows_p3 = [(268, NO), (325, NO), (386, NO), (410, NO), (432, NO), (466, NO),
           (502, YES), (524, NO), (558, NO), (594, NO), (618, NO), (650, NO),
           (705, NO)]
for y, col in rows_p3:
    X(3, col, y + 9)
T(3, HHN, 511, '1', 10)                # 7. HH# column
T(3, 462, 510, '15,500.40', 10)        # 7. Social Security retirement (ANNUAL)

# =============================================== template p4  (scan page_03)
X(4, NO,  202)                          # 14. child support
X(4, NO,  250)                          # 15. alimony
X(4, YES, 300)                          # 16. trusts / pensions  -> YES
T(4, HHN, 300, '1', 10)                 # 16. HH# column
T(4, 140, 310, 'LOS ANGELES COUNTY SHERIFF', 9)
T(4, 140, 345, 'PERS (CAL-PERS)', 9)
T(4, 468, 310, '32,274.00', 10)         # ANNUAL (was 2,689.50 monthly)
T(4, 468, 345, '20,835.72', 10)         # ANNUAL (was 1,736.31 monthly)
X(4, NO,  382)                          # 17. real estate / personal property
X(4, NO,  470)                          # 18. cash assistance
X(4, NO,  645)                          # 19. online income

# =============================================== template p5  (scan page_04)
X(5, NO, 215)                           # 20. help paying a bill
X(5, NO, 400)                           # 21. any other income
circle(5, 178, 402, 201, 418)           # inline "No" circled on 21

# =============================================== template p6  (scan page_05)
# PART 3 - employment block 1
T(6, 60,  192, 'THOMAS R STARBUCK', 10)
T(6, 300, 192, 'RETIRED', 10)
T(6, 40,  230, 'N/A', 10)               # employer name
T(6, 290, 230, 'N/A', 10)               # contact person
T(6, 430, 230, 'N/A', 10)               # employer email
T(6, 40,  267, 'N/A', 10)               # employer address
T(6, 265, 267, 'N/A', 10)               # city
T(6, 495, 267, 'N/A', 10)               # employer phone
T(6, 42,  323, '0', 10)                 # salary

# =============================================== template p7  (scan page_06)
box_check(7, 33, 230)                   # "I/We have assets"
X(7, NO,  330)                          # 1. RVs/boats/collections
X(7, NO, 428)                           # 2. cash on hand -> NO; everything else empty
T(7, HHN, 460, '1', 10)                 # 3. HH# column
X(7, YES, 460)                          # 3. checking
T(7, 150, 492, 'BANK OF AMERICA', 9)
T(7, 300, 492, '184012443', 9)
T(7, 403, 493, '4,781.50', 10)
T(7, 466, 493, '0%', 10)                # interest rate
T(7, 534, 493, '0.00', 10)              # annual income from asset
T(7, HHN, 590, '1', 10)                 # 4. HH# column
X(7, YES, 590)                          # 4. savings
T(7, 150, 615, 'BANK OF AMERICA', 9)
T(7, 300, 615, '3251 3920 3961', 9)
T(7, 403, 617, '81,966.33', 10)
T(7, 460, 617, '0.04%', 10)             # interest rate
T(7, 534, 617, '32.79', 10)             # annual income from asset
X(7, NO,  700)                          # 5. internet-based assets

# =============================================== template p8  (scan page_07)
X(8, NO,  220)                          # 6. debit card -> NO; all other values empty
X(8, NO, 345)                           # 7. brokerage
X(8, NO, 460)                           # 8. capital investments
X(8, NO, 525)                           # 9. annuities
X(8, NO, 645)                           # 10. money market

# =============================================== template p9  (scan page_08)
for y in (225, 330, 400, 505, 625):     # 11-15 all NO
    X(9, NO, y)

# =============================================== template p10 (scan page_09)
X(10, NO,  218)                         # 16. lump sum
X(10, NO,  285)                         # 17. safety deposit box
X(10, NO,  345)                         # 18. other assets
X(10, NO,  445)                         # 19. gave away assets
T(10, HHN, 575, '1', 10)                # 20. HH# column
X(10, YES, 575)                         # 20. tax refund
T(10, 402, 617, '3,822', 10)            # tax refund amount (was 4,747)
T(10, 470, 617, '0%', 10)               # 20. interest rate
T(10, 528, 617, '0', 10)                # 20. annual income
T(10, HHN, 665, '1', 10)                # 21. HH# column
X(10, YES, 665)                         # 21. real estate property
T(10, 140, 662, '1238 HERITAGE RANCH RD', 9)
T(10, 140, 676, 'SAN JACINTO, CA 92583', 9)
T(10, 402, 668, '118,500', 10)
T(10, 470, 668, '0%', 10)               # 21. interest rate
T(10, 528, 668, '0', 10)                # 21. annual income
circle(10, 494, 714, 530, 733)          # "Yes" - assets exceed $50,000

# =============================================== template p11 (scan page_10)
# Part 5 left clean this time - no strike-out lines, no N/A text.

# =============================================== template p12 (scan page_11)
X(12, 40, 275, 12)                      # Part 6, option 1 (signature left blank)

# =============================================== template p13 (scan page_12)
# signature / printed name / date left blank for HelloSign
T(13, 205, 596, 'BRYAN T. STARBUCK   SON   425 949-6801', 10)

# =============================================== template p14 (scan page_13)
T(14, 58,  256, 'THOMAS R. STARBUCK', 9)
T(14, 215, 256, 'Head of Household', 8)
T(14, 340, 256, 'WHITE', 9)
T(14, 430, 256, 'Prefer not to say', 8)
T(14, 505, 256, 'Not Disabled', 8)
# signature + date left blank for HelloSign

# =============================================== template p16 (scan page_15)
# Household Demographics Instruction sheet - the answers written in the margin
T(16, 300, 453, 'THOMAS R. STARBUCK', 9)    # HOUSEHOLD NAME
T(16, 395, 476, 'SELF', 9)                  # HOUSEHOLD COMPOSITION
T(16, 420, 496, 'NONE', 9)                  # HOUSEHOLD RELATIONSHIP
T(16, 345, 545, 'WHITE', 9)                 # RACE

# =============================================== template p17 (scan page_17)
T(17, 160, 116, PROP, 10)
# signature / printed name / date left blank for HelloSign

# =============================================== template p18 (scan page_16)
T(18, 175, 155, PROP, 10)
T(18, 175, 194, 'THOMAS R. STARBUCK', 10)
box_check(18, 87, 404)                  # "NO - neither I nor any household member"
# signature left blank for HelloSign

doc.save(OUT, deflate=True)
print('wrote', OUT, len(doc), 'pages')
print()
print('REMINDERS FOR BRYAN (attachments, not on the form):')
print(' * Row #20 tax refund needs external proof: a bank statement showing')
print('   the refund deposit. Source: Bank/BoA_Bank_statement.pdf')
print(' * A "Cash on Hand" affidavit is still needed for the Row #2 cash amount.')
print('----------------------------------------')
print('DONE: wrote', OUT)
print('----------------------------------------')
