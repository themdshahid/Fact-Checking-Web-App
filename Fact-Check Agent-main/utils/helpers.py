import pandas as pd


def create_results_dataframe(results):
    rows = []

    for item in results:
        rows.append({
            "Claim": item["claim"],
            "Result": item["result"]
        })

    return pd.DataFrame(rows)