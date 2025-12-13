# itcs204_finalsproject_agawin - Scripts

This folder contains a small script to get the most frequent customer name from the Amazon dataset.

Usage example:

1. Run the script from the repository root with the path to `Amazon.csv`:

```bash
python scripts/most_frequent_customer.py Amazon.csv --top 3
```

2. Or import `get_top_customers` from the script in a notebook:

```python
from scripts.most_frequent_customer import get_top_customers
top = get_top_customers('Amazon.csv', top_n=3)
print(top)
```

The function normalizes case by default so variants of the same name are counted together. Use `--no-normalize` for exact case-sensitive counts.
