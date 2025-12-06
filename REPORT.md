# Baby Names Analysis Results 🎯

## Data Format & Limitations
- **51 state files** (AK.TXT–WY.TXT + DC.TXT): `state,sex,year,name,count`
- **6.6M total records** (1910–present) 
- **Privacy**: ≥5 occurrences/state/year only
- **Limitations**: SSN coverage gaps [web:17]

## Part A: Descriptive Analysis ✅

### Most Popular Name All-Time
| Name  | Count     |
|-------|-----------|
| James | 5,089,997 |

### Most Gender-Ambiguous Names
| Year | M  | F  | Total | Ratio |
|------|----|----|-------|-------|
| 2013 | 47 | 47 | 94    | **1.00** |
| 1945 | 74 | 70 | 144   | **0.946** |

### Trends Since 1980 (1980-84 vs 2015-19)
| Metric       | Name     | Base   | Recent | % Change |
|--------------|----------|--------|--------|----------|
| **📈 Increase** | Isabella | 90     | 73,748 | **+818%** |
| **📉 Decrease** | Kristi   | 10,449 | 5      | **-99.95%** |

## Part B: Gender Ambiguity Evolution 📊
**Insight**: Highly ambiguous names (M/F ratio ≥0.8) grew 4x from 1940s to 2010s.

**Sample Data** (ambiguity_summary.csv):

