import os
import tempfile
import pandas as pd
from scripts.most_frequent_customer import get_top_customers


def test_get_top_customers_basic():
    # Create a small CSV with customer names
    data = {
        "CustomerName": ["Alice", "Bob", "alice", "Charlie", "Bob", "Bob", "Alice"]
    }
    df = pd.DataFrame(data)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as tmp:
        df.to_csv(tmp.name, index=False)
        tmp_path = tmp.name
    try:
        top = get_top_customers(tmp_path, column="CustomerName", top_n=2, case_insensitive=True)
        assert top.iloc[0] == 3  # Alice: Alice, alice
        assert top.index[0].lower().startswith("alice")
        assert top.iloc[1] == 3  # Bob
    finally:
        os.remove(tmp_path)


if __name__ == "__main__":
    test_get_top_customers_basic()
    print("All tests passed")
