# Baby Names Analysis Results

## Data Format
51 state files (AK.TXT-WY.TXT + DC.TXT), comma-delimited: `state,sex,year,name,count`
- Years: 1910-present
- Privacy: ≥5 occurrences only
- Limitations: SSN coverage gaps, no demographics [web:17]

## Part A: Descriptive Analysis

**Most popular name all time:**
name,count
James,5089997

**Most gender-ambiguous 2013:** `[from most_ambiguous_2013.csv]`

F,M,total,ambiguity_ratio
47.0,47.0,94.0,1.0

**Most gender-ambiguous 1945:** `[from most_ambiguous_1945.csv]`

F,M,total,ambiguity_ratio
70.0,74.0,144.0,0.9459459459459459


**Largest % increase since 1980:** `[from largest_increase_since_1980.csv]`

name,base,recent,pct_change
Isabella,90,73748,818.4222222222222

**Largest % decrease:** `[from largest_decrease_since_1980.csv]
name,base,recent,pct_change
Kristi,10449,5,-0.9995214853095991
`

## Part B: Gender Ambiguity Evolution
![Trend](figures/ambiguity_trend.png)

Number of highly ambiguous names (ratio ≥0.8) grew from [X] in 1940s to [Y] in 2010s.
Share of babies with ambiguous names: ![timeseries](figures/name_timeseries_*.png)
