from src.load_data import load_state_files, save_normalized, load_normalized
from src.descriptive import (
    most_popular_name_all_time,
    top_gender_ambiguous_name,
    largest_increase_and_decrease,
)
from src.insights_gender_ambiguity import yearly_ambiguity_summary
from src.viz import plot_name_timeseries, plot_ambiguity_trend
from src.config import OUTPUT_TABLES

def main():
    all_data = load_state_files()
    save_normalized(all_data)
    all_data = load_normalized()

    OUTPUT_TABLES.mkdir(parents=True, exist_ok=True)

    most_popular = most_popular_name_all_time(all_data)
    most_popular.to_csv(OUTPUT_TABLES / "most_popular_all_time.csv", index=False)

    amb_2013 = top_gender_ambiguous_name(all_data, 2013)
    amb_1945 = top_gender_ambiguous_name(all_data, 1945)
    amb_2013.to_frame().T.to_csv(OUTPUT_TABLES / "most_ambiguous_2013.csv", index=False)
    amb_1945.to_frame().T.to_csv(OUTPUT_TABLES / "most_ambiguous_1945.csv", index=False)

    inc, dec = largest_increase_and_decrease(all_data)
    inc.to_frame().T.to_csv(OUTPUT_TABLES / "largest_increase_since_1980.csv", index=False)
    dec.to_frame().T.to_csv(OUTPUT_TABLES / "largest_decrease_since_1980.csv", index=False)

    top_name = most_popular.iloc[0]["name"]
    plot_name_timeseries(all_data, top_name)

    amb_summary = yearly_ambiguity_summary(all_data)
    amb_summary.to_csv(OUTPUT_TABLES / "ambiguity_summary.csv", index=False)
    plot_ambiguity_trend(amb_summary)

if __name__ == "__main__":
    main()
