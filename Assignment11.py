import numpy as np
import pandas as pd

def create_random_series():
    rng = np.random.default_rng(42)
    numbers = rng.integers(1, 101, size=10)
    return pd.Series(numbers)

def create_labeled_series(values):
    labels = ['A', 'B', 'C', 'D', 'E',
              'F', 'G', 'H', 'I', 'J']
    return pd.Series(values.values, index=labels)

def describe_series(series):
    print(series)
    print("Data type:", series.dtype)
    print("Shape:", series.shape)
    print("Size:", series.size)
    print("Index:", series.index)

if __name__ == "__main__":
    series = create_random_series()

    print("Random Series:")
    describe_series(series)

    labeled_series = create_labeled_series(series)

    print("\nLabeled Series:")
    describe_series(labeled_series)

    print("\nBasic Statistics:")
    print("Minimum:", series.min())
    print("Maximum:", series.max())
    print("Mean:", series.mean())
    print("Sum:", series.sum())

    print("\nSeries Sorted by Value:")
    print(series.sort_values())

    print("\nValues Greater Than 50:")
    print(series[series > 50])
