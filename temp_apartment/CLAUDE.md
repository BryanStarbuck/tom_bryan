# Temporary Apartment — Charter

Find Tom Starbuck a **month-to-month apartment or hotel-like stay** he can rent while
he looks for a longer-term place. He needs somewhere to live for **one or two months**
before he signs a lease somewhere else.

## People

* **Tom Starbuck** — Bryan's dad. The person who needs the place.
* **Bryan Starbuck** — Tom's son. Does the research and planning.

## Requirements

* **Term:** Month-to-month. One to two months. No long lease.
* **Budget:** Ideally **under $3,300/month**. Airbnb tends to be too expensive, so
  price planning matters — compare real monthly totals, not nightly teaser rates.
* **Privacy:** **No cohabitating and no roommates.** Tom gets his own place.
  **Sublets are acceptable** and can be a good option.

## Location

Preference order:

1. **Redmond, WA** (preferred)
2. **East Bellevue, WA** (preferred)
3. **South Kirkland, WA** (acceptable)

Bellevue and Kirkland generally are in scope; the sub-areas above are the target.

## Kinds of Options

Anything that produces a private month-to-month stay counts:

* Apartment buildings that allow month-to-month leases
* Hotels / extended-stay hotels
* Nationwide furnished-rental services that allow month-to-month
* Sublets

**Blueground** (theblueground.com) is a known base option — we have used it before.
It is an online platform listing many different places, so it is its own category
rather than a single building.

## Directory Structure

```
temp_apartment/
├── CLAUDE.md          # this charter
├── overview.mdx       # the overview of the search
├── locations.csv      # all locations, one row each
└── locations/
    ├── hotel/
    ├── apartment/
    ├── blueground/
    └── {other categories as found}/
```

### locations.csv

One row per location or solution. The flat list of everything we are considering.

### locations/ — one subdirectory per category

Categories are things like `hotel/`, `apartment/`, `blueground/`. Add new category
directories as new kinds of solutions turn up. Blueground gets its own directory
because it is a platform spanning many properties, not one building.

### One .mdx file per location

Inside each category directory, one `.mdx` file per location or instance — a single
apartment building, an online listing, a platform, whatever the unit is.

* **Filename:** the name of the place, **underscores instead of spaces**
  (e.g. `The_Bellevue_Suites.mdx`)
* **Structure:** most important information at the **top**; increasing detail as you
  go **down** the file.
* **Links:** every file should hyperlink to its peer files where relevant.
