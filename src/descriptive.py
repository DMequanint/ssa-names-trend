import pandas as pd
from .config import (
    AMBIGUITY_MIN_TOTAL,
    TREND_BASE_START, TREND_BASE_END,
    TREND_RECENT_START, TREND_RECENT_END,
)

def most_popular_name_all_time(df: pd.DataFrame, merge_sex: bool = True) -> pd.DataFrame:
    if merge_sex:
        grouped = df.groupby("name", as_index=False)["count"].sum()
    else:
        grouped = df.groupby(["name", "sex"], as_index=False)["count"].sum()
    max_total = grouped["count"].max()
    return grouped[grouped["count"] == max_total].sort_values("name")

def gender_ambiguity_by_year(df: pd.DataFrame, year: int) -> pd.DataFrame:
    year_df = df[df["year"] == year]
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

    both_mask = (agg["M"] > 0) & (agg["F"] > 0)
    agg = agg[both_mask].copy()

    agg["ambiguity_ratio"] = agg[["M", "F"]].min(axis=1) / agg[["M", "F"]].max(axis=1)
    agg = agg.sort_values("ambiguity_ratio", ascending=False)
    return agg

def top_gender_ambiguous_name(df: pd.DataFrame, year: int) -> pd.Series:
    amb = gender_ambiguity_by_year(df, year)
    return amb.iloc[0]

def percentage_change_since_1980(df: pd.DataFrame, merge_sex: bool = True) -> pd.DataFrame:
    base = df[(df["year"] >= TREND_BASE_START) & (df["year"] <= TREND_BASE_END)]
    recent = df[(df["year"] >= TREND_RECENT_START) & (df["year"] <= TREND_RECENT_END)]

    group_cols = ["name"] if merge_sex else ["name", "sex"]

    base_sum = base.groupby(group_cols, as_index=False)["count"].sum().rename(columns={"count": "base"})
    recent_sum = recent.groupby(group_cols, as_index=False)["count"].sum().rename(columns={"count": "recent"})

    merged = pd.merge(base_sum, recent_sum, on=group_cols, how="inner")
    merged = merged[merged["base"] >= 50]
    merged["pct_change"] = (merged["recent"] - merged["base"]) / merged["base"]

    return merged

def largest_increase_and_decrease(df: pd.DataFrame, merge_sex: bool = True):
    pct = percentage_change_since_1980(df, merge_sex=merge_sex)
    inc = pct.sort_values("pct_change", ascending=False).iloc[0]
    dec = pct.sort_values("pct_change", ascending=True).iloc[0]
    return inc, dec
