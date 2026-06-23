ROOT_DIR dir is ~/BGit/Bryan_git/tom_bryan/apartment


GOAL: Find senior apartments for Tom Starbuck (about 84 years old), Bryan's dad,
in Redmond / Bellevue Washington or nearby within about a 20-minute drive. Grow
the apartment list longer over time, and keep the CSV files well structured.


====================================================================
FILES
====================================================================

* APARTMENTS_FILE is file {ROOT_DIR}/apartments.csv
  * The main, human-readable list. One row per senior apartment community.
  * Sorted by score, best first.

* ADVANCED_FILE is file {ROOT_DIR}/advanced.csv
  * The "advanced" companion data, joined to APARTMENTS_FILE by the name column.
  * Holds website, review data, and raw coordinates so the main list stays clean.

* INDEPENDENT_LIVING_FILE is file {ROOT_DIR}/independent_living.csv
  * Senior independent-living-with-bundled-services options. Lower preference,
    kept separate from the main list.

* GOALS_FILE is file {ROOT_DIR}/goals.txt
  * The charter. Read it first to understand what Tom wants.


====================================================================
GEOGRAPHY (stored so distances are easy to recompute)
====================================================================

* EPICENTER_1 is the value = the I-405 / SR-520 interchange, Bellevue WA.
  * EPICENTER_1_LATLON is the value = 47.6280, -122.1876

* EPICENTER_2 is the value = 16430 NE 50th St, Redmond WA 98052.
  * EPICENTER_2_LATLON is the value = 47.6442, -122.1215

* MIDPOINT is the value = the point halfway between EPICENTER_1 and EPICENTER_2.
  * MIDPOINT_LATLON is the value = 47.6361, -122.1546
  * This is the single reference point used for the km_to_midpoint column.
  * Being close to the midpoint means being close to BOTH epicenters, which is
    what we care about most.


====================================================================
WHAT WE WANT
====================================================================

* SENIOR APARTMENTS (age-restricted rentals, 55+ or 62+).
* We do NOT want Assisted Living, memory care, or CCRCs.
* We prefer plain senior apartments OVER senior independent-living-with-services.
  * Independent-living-with-bundled-services goes in INDEPENDENT_LIVING_FILE.
* Income-based / affordable and market-rate age-restricted rentals are both fine.
* Mixed-population buildings (families + seniors) are acceptable but lower value;
  always say so in the notes ("MIXED population, not senior-only").


====================================================================
PREFERRED LOCATIONS (priority order, best first)
====================================================================

* 1. Bellevue or Redmond   (most preferred)
* 2. Kirkland
* 3. Factoria
* 4. Woodinville
* 5. Issaquah
* Renton and Bothell are acceptable but farther; they rank lower on distance.


====================================================================
SCORING (how each apartment earns its score, 0 to 100)
====================================================================

* Closeness to MIDPOINT (the km_to_midpoint value) is the biggest factor.
  Smaller is better.
* RENT: we prefer rent near $1,300/month. It is less interesting as price climbs
  toward $3,000/month and beyond.
* LOCATION PRIORITY: apply the preferred-locations order above as a thumb on the
  scale, so Bellevue/Redmond outrank equally-distant Kirkland, etc.
* Use existing rows as calibration anchors when scoring a new row: slot a new
  community next to the existing community it most resembles in distance, city,
  and rent, then nudge for rent and senior-only vs mixed.


====================================================================
HOW TO GROW THE LIST
====================================================================

* Read GOALS_FILE first. Then read both CSV files so you do not add duplicates.
* Search the web for senior apartment communities in the preferred locations.
  Good sources to enumerate by provider:
  * KCHA - King County Housing Authority (kcha.org) senior / 62+ properties
  * Imagine Housing (imaginehousing.org)
  * SHAG (housing4seniors.com)
  * CIRC Living / Transforming Age (circliving.org)
  * Catholic Community Services / Catholic Housing Services
  * ARCH affordable-housing list (archhousing.org)
* For each NEW community (not already in either CSV):
  * Confirm it is an age-restricted RENTAL, not assisted living or a CCRC.
    If it bundles services, put it in INDEPENDENT_LIVING_FILE instead.
  * Find: address, monthly rent (range, or "income-based"), bedrooms, age rule,
    phone, website, any review data, and latitude/longitude.
  * Compute km_to_midpoint with the haversine formula from MIDPOINT_LATLON.
  * Assign a score per the SCORING section.
  * Append one row to APARTMENTS_FILE and one matching row (same name) to
    ADVANCED_FILE.
* Re-sort APARTMENTS_FILE by score, best first. Keep ADVANCED_FILE joinable by
  name.
* Use "unknown" for any value you cannot confirm. Never invent data.


====================================================================
APPENDIX: CSV COLUMN DEFINITIONS
====================================================================

APARTMENTS_FILE columns, in order:

* 1. name           Community name. Join key to ADVANCED_FILE.
* 2. city           City the community is in.
* 3. address        Full street address (quote it; it contains commas).
* 4. monthly_rent   A range like 945-1283, a single number, or "income-based".
* 5. bedrooms       Unit types, e.g. "studio,1BR,2BR".
* 6. senior_type    Age rule, e.g. 55+, 62+, or "senior".
* 7. score          0 to 100, higher is better. List is sorted by this.
* 8. phone          Best contact phone number.
* 9. km_to_midpoint Straight-line km from MIDPOINT_LATLON. Smaller is better.
* 10. notes         One line: type, unit count, restrictions, waitlist, flags.

ADVANCED_FILE columns, in order:

* 1. name           Community name. Same value as in APARTMENTS_FILE (a COPY,
                    used to join the two files).
* 2. website        Listing or community URL.
* 3. review_score   Rating value, or "unknown".
* 4. review_count   Number of reviews, or "unknown".
* 5. review_source  Where the rating came from (Google, Caring.com, etc.).
* 6. lat            Latitude of the community.
* 7. lon            Longitude of the community.
