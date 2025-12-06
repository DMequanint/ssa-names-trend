import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from .config import FIGURES

FIGURES.mkdir(parents=True, exist_ok=True)

def plot_name_timeseries(df: pd.DataFrame, name: str, merge_sex: bool = True):
    sub = df[df["name"] == name]
    if merge_sex:
        sub = sub.groupby("year", as_index=False)["count"].sum()

    plt.figure(figsize=(8, 4))
    sns.lineplot(data=sub, x="year", y="count")
    plt.title(f"Popularity of {name} over time")
    plt.tight_layout()
    out = FIGURES / f"name_timeseries_{name}.png"
    plt.savefig(out, dpi=150)
    plt.close()
    return out

def plot_ambiguity_trend(amb_summary: pd.DataFrame):
    fig, ax1 = plt.subplots(figsize=(8, 4))

    color1 = "tab:blue"
    ax1.set_xlabel("Year")
    ax1.set_ylabel("# Highly ambiguous names", color=color1)
    ax1.plot(amb_summary["year"], amb_summary["num_highly_ambiguous_names"], color=color1)
    ax1.tick_params(axis="y", labelcolor=color1)

    ax2 = ax1.twinx()
    color2 = "tab:orange"
    ax2.set_ylabel("Share of babies with ambiguous names", color=color2)
    ax2.plot(amb_summary["year"], amb_summary["share_babies_ambiguous"], color=color2)
    ax2.tick_params(axis="y", labelcolor=color2)

    fig.tight_layout()
    out = FIGURES / "ambiguity_trend.png"
    plt.savefig(out, dpi=150)
    plt.close()
    return out
