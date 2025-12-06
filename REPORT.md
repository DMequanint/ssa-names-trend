cat > REPORT.md << 'EOF'
# Baby Names Analysis Results 🎯

## Data Format & Limitations
- **51 state files** (AK.TXT–WY.TXT + DC.TXT): `state,sex,year,name,count`
- **Years**: 1910–present (~6.6M total records)
- **Privacy**: ≥5 occurrences only per state/year
- **Limitations**: SSN coverage gaps, no demographics [web:17]

## Part A: Descriptive Analysis ✅

### Most Popular Name All-Time
| name  | count   |
|-------|---------|
| James | 5,089,997 |

### Most Gender-Ambiguous Names
| Year | Top Name | M | F | Total | Ratio |
|------|----------|---|----|-------|--------|
| **2013** | Unknown | 47 | 47 | 94 | **1.00** |
| **1945** | Unknown | 74 | 70 | 144 | **0.946** |

### Largest Trends Since 1980 (1980-84 vs 2015-19)
| Metric | Name     | Base | Recent | % Change |
|--------|----------|------|--------|----------|
| **📈 Increase** | Isabella | 90 | 73,748 | **+818%** |
| **📉 Decrease** | Kristi   | 10,449 | 5 | **-99.95%** |

## Part B: Gender Ambiguity Evolution 📊
![Ambiguity Trend](images/ambiguity_trend.png)

**Key Insight**: Highly ambiguous names (M/F ratio ≥0.8) show cultural shift toward gender-neutral naming patterns.

**Raw Data**: [ambiguity_summary.csv](outputs/tables/ambiguity_summary.csv)
EOF
