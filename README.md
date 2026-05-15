# Market Basket Analysis

Apriori association rule mining on retail grocery transaction data. Finds which products are frequently bought together and quantifies the strength of those relationships.

## What it does

Reads a CSV of grocery transactions, runs the Apriori algorithm, and outputs association rules ranked by confidence. Each rule has the form **antecedent → consequent** (e.g. "bread → butter") with support, confidence, and lift scores.

## Dataset

`store_data.csv` — each row is one transaction, each column is one item in the basket. The file is included in the repo.

## Tech Stack

- Python 3
- pandas
- apyori

## How to Run

```bash
pip install pandas apyori
python market_basket.py
```

Results are printed to the terminal and saved to `association_rules.csv`.

## Sample Output

| antecedent     | consequent      | support | confidence | lift |
|----------------|-----------------|---------|------------|------|
| mineral water  | eggs            | 0.0498  | 0.30       | 2.10 |
| spaghetti      | mineral water   | 0.0597  | 0.29       | 1.83 |
| chocolate      | mineral water   | 0.0526  | 0.28       | 1.75 |

**support** — fraction of transactions containing both items  
**confidence** — probability of consequent given antecedent  
**lift** — how much more likely than random co-occurrence (>1 means positively correlated)
