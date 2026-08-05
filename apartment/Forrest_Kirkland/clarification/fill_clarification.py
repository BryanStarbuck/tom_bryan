#!/usr/bin/env python3
"""Fill the blank Clarification Record (in/clarification.pdf) and write
out/filled_out_clarification.pdf. Technique follows income_proof/fill_form.py
(PyMuPDF insert_text, dark-blue ink). This page is unrotated 612x1008."""
import fitz, os

BASE = os.path.expanduser(
    '~/BGit/Bryan_git/tom_bryan/apartment/Forrest_Kirkland/clarification')
SRC = os.path.join(BASE, 'in', 'clarification.pdf')
OUT = os.path.join(BASE, 'out', 'filled_out_clarification.pdf')
os.makedirs(os.path.dirname(OUT), exist_ok=True)

FONT = 'helv'
INK = (0, 0, 0.55)      # dark blue ink

doc = fitz.open(SRC)
pg = doc[0]


def T(x, y, text, size=10):
    pg.insert_text(fitz.Point(x, y), text, fontname=FONT, fontsize=size,
                   color=INK)


DATE = 'Aug 5th, 2026'

# ----- header -----
T(180, 135.5, 'Tom Starbuck')                 # Applicant/Resident Name
T(478, 135.5, DATE)                           # top "Date:" field
# Initial Certification — fill the small "o" circle solid
# the circle glyph occupies roughly (75.3,150.3)-(81.3,163.8); ink its bowl
pg.draw_oval(fitz.Rect(74.6, 155.2, 82.0, 162.6), color=INK, fill=INK)
T(170, 265.5, DATE)                           # Date of Clarification

# ----- questions (label baseline y; text goes on the line below) -----
T(76, 388, '"Is your property fully paid off?"')
T(76, 442, '"Is there anything you have to paid on your property outside of '
           'Property tax?"')
T(76, 496, '"Do you plan on your real estate selling in the next couple of '
           'months?"')

# ----- answers -----
T(76, 642, '"Yes. It is fully paid off"')
T(76, 696, '"No.  There is nothing to paid on my property outside of '
           'Property tax"')
T(76, 750, '"No.  I do not plan on my real estate selling in the next couple '
           'of months"')

# signature / employee lines intentionally left blank (HelloSign later)

doc.save(OUT, deflate=True)
print('wrote', OUT)
