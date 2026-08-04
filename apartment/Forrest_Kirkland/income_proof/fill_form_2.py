#!/usr/bin/env python3
"""Run 2: fill the blank Compliance_Packet.pdf per p_fill_income.md.

Based on fill_form.py (run 1). Differences:
  * checklist page 1 gets 7 check marks
  * Initial Certification checked on HEA page 1
  * HH# "1" entries added on income/asset rows
  * income amounts are ANNUAL (monthly x 12)
  * checking/savings interest rate + annual income filled
  * Part 5 left clean (no strike-out X, no N/A text)
  * NO signatures, signature dates, or places of signature (HelloSign later)
"""
import fitz, os

BASE = os.path.expanduser('~/BGit/Bryan_git/tom_bryan/apartment/Forrest_Kirkland')
SRC = os.path.join(BASE, 'Compliance_Packet.pdf')
OUT = os.path.join(BASE, 'income_proof', 'out', 'filled_out_income.pdf')
os.makedirs(os.path.dirname(OUT), exist_ok=True)

PROP = 'WOODLANDS AT FORBES LAKE'
HH   = 'THOMAS R. STARBUCK'
SIZE = '1'

FONT = 'helv'
FB   = 'hebo'
INK  = (0, 0, 0.55)

doc = fitz.open(SRC)
ROT = 90


def T(pno, x, y, text, size=9, font=FONT, color=INK):
    pg = doc[pno - 1]
    pt = fitz.Point(x, y) * pg.derotation_matrix
    pg.insert_text(pt, text, fontname=font, fontsize=size, color=color,
                   rotate=ROT)


def X(pno, x, y, size=11):
    T(pno, x - size * 0.33, y, 'X', size, FB)


def circle(pno, x0, y0, x1, y1):
    pg = doc[pno - 1]
    r = fitz.Rect(x0, y0, x1, y1) * pg.derotation_matrix
    pg.draw_oval(r, color=INK, width=1.1)


def box_check(pno, x, y):
    X(pno, x, y, 10)


YES, NO = 68.0, 99.0
HHCOL = 42.0        # left edge of the "1" inside the HH# column

# ================================================ page 1 - COMPLIANCE FORMS CHECKLIST
T(1, 195, 86, PROP, 9)
T(1, 195, 106, HH, 9)
box_check(1, 70, 204)      # Household Eligibility Certification
box_check(1, 70, 225)      # Household Eligibility Application (HEA)
box_check(1, 71, 265)      # Household Demographics
box_check(1, 71, 283)      # Authorization to Release Confidential Information
box_check(1, 88, 420)      # Social Security Verification/Consent for Release
box_check(1, 336, 389)     # Pension Verification
box_check(1, 85, 574)      # Disability Status Certification

# ---------------------------------------------------------------- headers
for p in range(2, 14):
    T(p, 30, 82, PROP, 9)
    T(p, 30, 119, HH, 9)
    T(p, 500, 120, SIZE, 9)
T(14, 41, 94, PROP, 9)
T(14, 41, 137, HH, 9)

# =============================================== template p2 (printed Page 1)
box_check(2, 322, 170)                  # Initial Certification
T(2, 122, 323, 'THOMAS R STARBUCK', 10)
T(2, 340, 323, '10/15/1945', 10)
T(2, 420, 323, '7741', 10)
circle(2, 558, 306, 586, 324)           # "N/A" (not a student) circled

# =============================================== template p3 (printed Page 2)
rows_p3 = [(268, NO), (325, NO), (386, NO), (410, NO), (432, NO), (466, NO),
           (502, YES), (524, NO), (558, NO), (594, NO), (618, NO), (650, NO),
           (705, NO)]
for y, col in rows_p3:
    X(3, col, y + 9)
T(3, HHCOL, 511, '1', 10)               # HH# for row 7
T(3, 468, 510, '15,500', 10)            # 7. Social Security retirement (annual)

# =============================================== template p4 (printed Page 3)
X(4, NO,  202)                          # 14. child support
X(4, NO,  250)                          # 15. alimony
X(4, YES, 300)                          # 16. trusts / pensions -> YES
T(4, HHCOL, 300, '1', 10)               # HH# for row 16
T(4, 140, 310, 'LOS ANGELES COUNTY SHERIFF', 9)
T(4, 140, 345, 'PERS (CAL-PERS)', 9)
T(4, 469, 310, '32,274.00', 10)         # annual
T(4, 469, 345, '20,835.72', 10)         # annual
X(4, NO,  382)                          # 17. real estate / personal property
X(4, NO,  470)                          # 18. cash assistance
X(4, NO,  645)                          # 19. online income

# =============================================== template p5 (printed Page 4)
X(5, NO, 215)                           # 20. help paying a bill
X(5, NO, 400)                           # 21. any other income
circle(5, 178, 402, 201, 418)

# =============================================== template p6 (printed Page 5)
T(6, 60,  192, 'THOMAS R STARBUCK', 10)
T(6, 300, 192, 'RETIRED', 10)
T(6, 40,  230, 'N/A', 10)
T(6, 290, 230, 'N/A', 10)
T(6, 430, 230, 'N/A', 10)
T(6, 40,  267, 'N/A', 10)
T(6, 265, 267, 'N/A', 10)
T(6, 495, 267, 'N/A', 10)
T(6, 42,  323, '0', 10)

# =============================================== template p7 (printed Page 6)
box_check(7, 33, 230)                   # "I/We have assets"
X(7, NO,  330)                          # 1. RVs/boats/collections
X(7, YES, 428)                          # 2. cash on hand
T(7, HHCOL, 428, '1', 10)               # HH# row 2
T(7, 403, 428, '2,600', 10)
T(7, 470, 428, '0', 10)
T(7, 528, 428, '0', 10)
X(7, YES, 460)                          # 3. checking
T(7, HHCOL, 460, '1', 10)               # HH# row 3
T(7, 150, 492, 'BANK OF AMERICA', 9)
T(7, 300, 492, '184012443', 9)
T(7, 403, 493, '4,781.50', 10)
T(7, 466, 493, '1.96', 10)              # interest rate (% preprinted)
T(7, 530, 493, '93.72', 10)             # annual income from asset
X(7, YES, 590)                          # 4. savings
T(7, HHCOL, 590, '1', 10)               # HH# row 4
T(7, 150, 615, 'BANK OF AMERICA', 9)
T(7, 300, 615, '3251 3920 3961', 9)
T(7, 403, 617, '81,966.33', 10)
T(7, 462, 617, '3.961', 10)             # interest rate
T(7, 528, 617, '3,246.69', 10)          # annual income from asset
X(7, NO,  700)                          # 5. internet-based assets

# =============================================== template p8 (printed Page 7)
X(8, YES, 220)                          # 6. debit card
T(8, HHCOL, 220, '1', 10)               # HH# row 6
T(8, 150, 261, 'BANK OF AMERICA', 9)
T(8, 300, 261, '3799', 9)
T(8, 403, 253, '0', 10)
T(8, 470, 253, '0', 10)
T(8, 528, 253, '0', 10)
X(8, NO, 345)
X(8, NO, 460)
X(8, NO, 525)
X(8, NO, 645)

# =============================================== template p9 (printed Page 8)
for y in (225, 330, 400, 505, 625):
    X(9, NO, y)

# =============================================== template p10 (printed Page 9)
X(10, NO,  218)
X(10, NO,  285)
X(10, NO,  345)
X(10, NO,  445)
X(10, YES, 575)                         # 20. tax refund
T(10, HHCOL, 575, '1', 10)              # HH# row 20
T(10, 402, 617, '3,822', 10)
X(10, YES, 665)                         # 21. real estate property
T(10, HHCOL, 665, '1', 10)              # HH# row 21
T(10, 140, 662, '1238 HERITAGE RANCH RD', 9)
T(10, 140, 676, 'SAN JACINTO, CA 92583', 9)
T(10, 402, 668, '118,500', 10)
T(10, 527, 668, '0', 10)
circle(10, 494, 714, 530, 733)          # "Yes" - assets exceed $50,000

# =============================================== template p11 (printed Page 10)
# Part 5 left completely clean this time (no strike-out, no N/A text).

# =============================================== template p12 (printed Page 11)
X(12, 40, 275, 12)                      # Part 6, option 1 (Dad signs box 1 via HelloSign)

# =============================================== template p13 (printed Page 12)
# signature / printed name / date left EMPTY for HelloSign
T(13, 40, 668, 'BRYAN T. STARBUCK', 10)
T(13, 253, 668, 'SON', 10)
T(13, 447, 668, '425 949-6801', 10)

# =============================================== template p14 (demographics)
T(14, 58,  256, 'THOMAS R. STARBUCK', 9)
T(14, 215, 256, 'RENTER', 9)
T(14, 340, 256, 'WHITE', 9)
T(14, 430, 256, 'Prefer not to say', 8)
T(14, 505, 256, 'NO', 9)
# signature + date left EMPTY for HelloSign

# =============================================== template p16
T(16, 300, 453, 'THOMAS R. STARBUCK', 9)
T(16, 395, 476, 'SELF', 9)
T(16, 420, 496, 'NONE', 9)
T(16, 345, 545, 'WHITE', 9)

# =============================================== template p17
T(17, 160, 116, PROP, 10)
T(17, 290, 452, 'THOMAS R. STARBUCK', 10)
# signature + date left EMPTY for HelloSign

# =============================================== template p18
T(18, 175, 155, PROP, 10)
T(18, 175, 194, 'THOMAS R. STARBUCK', 10)
box_check(18, 87, 404)                  # "NO - neither I nor any household member"
# signature left EMPTY for HelloSign

doc.save(OUT, deflate=True)
print('wrote', OUT, len(doc), 'pages')
print('-' * 40)
print('REMINDERS (attachments still needed):')
print(' * Bank statement proving the $3,822 tax refund deposit')
print('   -> Tax_Refund.pdf (BoA wire-in 01/22/2026) / ../Bank/BoA_Bank_statement.pdf')
print(' * Cash on Hand affidavit for the $2,600 cash amount')
print('-' * 40)
