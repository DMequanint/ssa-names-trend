# Baby Names Analysis

This project analyzes US baby names from state-level SSA-like data.
It answers descriptive questions (most popular names, gender ambiguity,
popularity trends) and explores an additional insight.

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Place all state files (e.g. CA.txt, NY.txt, ...) into `data/raw/`.
4. Run the main analysis:

   ```
   python run_all.py
   ```

See `outputs/` for CSVs and `figures/` for plots.
