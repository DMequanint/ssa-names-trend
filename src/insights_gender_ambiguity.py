import pandas as pd
from .config import AMBIGUITY_MIN_TOTAL

def yearly_ambiguity_summary(df: pd.DataFrame) -> pd.DataFrame:
    records = []

    for year, year_df in df.groupby("year"):
        agg = (
            year_df
            .groupby(["name", "sex"], as_index=False)["count"]
            .sum()
            .pivot(index="name", columns="sex", values="count")
            .fillna(0)
        )
        for col in ["M", "F"]:
            if col not in agg.columns:
                agg[col] = 0

        agg["total"] = agg["M"] + agg["F"]
        agg = agg[agg["total"] >= AMBIGUITY_MIN_TOTAL]

        both = agg[(agg["M"] > 0) & (agg["F"] > 0)].copy()
        both["ratio"] = both[["M", "F"]].min(axis=1) / both[["M", "F"]].max(axis=1)

        highly_ambiguous = both[both["ratio"] >= 0.8]
        num_highly = len(highly_ambiguous)

        total_babies = year_df["count"].sum()
        ambiguous_babies = year_df[year_df["name"].isin(both.index)]["count"].sum()

        records.append(
            {
                "year": year,
                "num_highly_ambiguous_names": num_highly,
                "share_babies_ambiguous": ambiguous_babies / total_babies if total_babies else 0.0,
            }
        )

    return pd.DataFrame(records).sort_values("year")
