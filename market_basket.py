import pandas as pd
from apyori import apriori


def load_transactions(filepath: str) -> list:
    data = pd.read_csv(filepath, header=None)
    records = []
    for i in range(len(data)):
        records.append([str(data.values[i, j]) for j in range(data.shape[1])])
    return records


def run_apriori(records: list, min_support=0.0045, min_confidence=0.2, min_lift=1.5) -> list:
    rules = apriori(records, min_support=min_support, min_confidence=min_confidence,
                    min_lift=min_lift, min_length=2)
    return list(rules)


def parse_results(results: list) -> pd.DataFrame:
    antecedent, consequent, support, confidence, lift = [], [], [], [], []

    for item in results:
        pair = list(item[0])
        if len(pair) < 2:
            continue
        antecedent.append(pair[0])
        consequent.append(pair[1])
        support.append(item[1])
        confidence.append(item[2][0][2])
        lift.append(item[2][0][3])

    df = pd.DataFrame({
        "antecedent": antecedent,
        "consequent": consequent,
        "support": support,
        "confidence": confidence,
        "lift": lift,
    })
    return df.sort_values(by="confidence", ascending=False).dropna().reset_index(drop=True)


def main():
    transactions = load_transactions("store_data.csv")
    results = run_apriori(transactions)
    df = parse_results(results)
    print(df.to_string(index=False))
    df.to_csv("association_rules.csv", index=False)
    print("\nResults saved to association_rules.csv")


if __name__ == "__main__":
    main()
