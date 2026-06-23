ROOT_DIR dir is ~/BGit/Bryan_git/tom_bryan/broker

OUTPUT_FILE is file {ROOT_DIR}/brokers.csv

GOALS_FILE is file {ROOT_DIR}/goals_broker.txt


===========================
PURPOSE

* Find brokers / advisors who help a person locate and get into an apartment,
  especially brokers who SPECIALIZE IN SENIORS (senior housing placement,
  senior living advisors, senior real estate specialists / SRES).
* Search the internet for them, gather their data, and write {OUTPUT_FILE}.
* This is for Tom Starbuck. Read {GOALS_FILE} first for the full charter.


===========================
WHERE THEY MUST SERVE

HIGHEST PRIORITY (far greater priority — list these first):
  * Redmond, WA
  * Bellevue, WA
  * Kirkland, WA

ALSO ACCEPTABLE:
  * Factoria, WA   (district within Bellevue)
  * Issaquah, WA
  * Woodinville, WA

* A broker who covers "the Eastside" or "King County" counts — note which cities.


===========================
WHAT TO SEARCH FOR

* Run multiple internet searches. Vary the terms. Examples:
  * "senior living advisor Redmond WA"
  * "senior placement agent Bellevue WA"
  * "senior housing locator Kirkland WA"
  * "senior real estate specialist SRES Eastside WA"
  * "apartment locator Bellevue WA seniors"
  * "assisted living placement Redmond Bellevue Kirkland"
  * National services with local agents: A Place for Mom, CarePatrol,
    Oasis Senior Advisors, Assisted Living Locators, Senior Living Advisors.
* For each candidate, open their site / listing to confirm location, phone,
  whether they specialize in seniors, and any review scores.


===========================
DATA TO COLLECT (every column we can fill)

For each broker, gather as much as possible:
  * Broker_Name        — person's name if known, else company contact
  * Company            — business / brokerage name
  * City               — primary city
  * State              — WA
  * Serves_Areas       — which of our target cities (and broader region) they cover
  * Senior_Specialist  — yes / no / partial  (do they focus on seniors?)
  * Services           — short description (placement, apartment locating, SRES, etc.)
  * Score_Rating       — review score (e.g. 4.8) if found
  * Reviews_Count      — number of reviews behind the score
  * Score_Source       — where the score came from (Google, Yelp, etc.)
  * Phone
  * Email
  * Website
  * Address            — street address if available
  * Source             — URL / where we found this broker
  * Priority           — HIGH if in Redmond/Bellevue/Kirkland, else MED
  * Notes              — anything useful (free service, fees, senior focus details)
  * Status             — bracket: [     ] [TO-CALL] [CONTACTED] [ DONE]


===========================
RULES

* CSV: first row is the header with the exact column names above, in that order.
* Quote any field that contains a comma.
* If a value is unknown, leave it blank — do not invent data.
* Only record real, verifiable brokers found via search. No fabrication.
* Sort the rows: HIGH priority first (Redmond / Bellevue / Kirkland), then MED.
* Within a priority group, put senior specialists first, then by Score_Rating high to low.
* Aim for a good number of candidates (target 12+ if available).


===========================
OUTPUT

* Write all rows to {OUTPUT_FILE}.
* Then print to stdout a short summary: how many brokers found, how many HIGH
  priority, and how many are senior specialists.
* Update the STATUS section of {GOALS_FILE} to mark brokers.csv as built.
