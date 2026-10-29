import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def generate_data():
    rng = np.random.default_rng(42)
    n = 200
    tenure = rng.integers(1, 73, n)
    contract = rng.choice(
        ["Month-to-month", "One year", "Two year"], n
    )
    monthly = rng.uniform(20, 120, n).round(2)
    probability = np.where(contract == "Month-to-month", 0.5, 0.15)
    churn = np.where(rng.random(n) < probability, "Yes", "No")

    df = pd.DataFrame({
        "Tenure": tenure,
        "Contract": contract,
        "InternetService": rng.choice(
            ["DSL", "Fiber optic", "No"], n
        ),
        "MonthlyCharges": monthly,
        "TotalCharges": (tenure * monthly).astype(str),
        "Partner": rng.choice(["Yes", "No"], n),
        "Churn": churn
    })

    # Introduce data quality issues.
    df.loc[0:4, "Partner"] = np.nan
    df.loc[5:7, "Churn"] = " yes "
    df.loc[8:10, "InternetService"] = "fiber optic"
    df.loc[11:13, "TotalCharges"] = "unknown"
    df = pd.concat([df, df.iloc[:3]], ignore_index=True)
    return df


def explore_data(df):
    print("\nShape:\n", df.shape)
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nDuplicates:", df.duplicated().sum())
    print("\nSummary:\n", df.describe(include="all"))


def clean_data(df):
    df = df.copy()

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"], errors="coerce"
    )

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    df["Partner"] = df["Partner"].replace(
        {"yes": "Yes", "no": "No"}
    )
    df["Churn"] = df["Churn"].replace(
        {"yes": "Yes", "no": "No"}
    )
    df["InternetService"] = df["InternetService"].replace(
        {"fiber optic": "Fiber optic"}
    )

    df = df.drop_duplicates()

    for col in df.select_dtypes(include="object").columns:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].mode()[0])

    for col in df.select_dtypes(include=np.number).columns:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())

    return df


def analyze_churn(df):
    print("\nOverall Churn Rate:",
          round((df["Churn"] == "Yes").mean() * 100, 2), "%")

    for col in ["Contract", "InternetService"]:
        print(f"\nChurn Rate by {col} (%):")
        print(df.groupby(col)["Churn"].apply(
            lambda x: (x == "Yes").mean() * 100
        ).round(2))

    print("\nAverage Tenure:\n", df.groupby("Churn")["Tenure"].mean())
    print("\nAverage Monthly Charges:\n",
          df.groupby("Churn")["MonthlyCharges"].mean())


def visualize(df):
    df["Churn"].value_counts().plot(kind="bar", title="Churn Distribution")
    plt.tight_layout()
    plt.savefig("churn_distribution.png")
    plt.close()

    df.groupby("Contract")["Churn"].apply(
        lambda x: (x == "Yes").mean() * 100
    ).plot(kind="bar", title="Churn by Contract (%)")
    plt.tight_layout()
    plt.savefig("churn_by_contract.png")
    plt.close()

    for value in ["Yes", "No"]:
        df.loc[df["Churn"] == value, "Tenure"].plot(
            kind="hist", bins=12, alpha=0.5, label=value
        )
    plt.title("Tenure by Churn")
    plt.legend()
    plt.tight_layout()
    plt.savefig("tenure_histogram.png")
    plt.close()

    corr = df.select_dtypes(include=np.number).corr()
    plt.imshow(corr, vmin=-1, vmax=1, cmap="coolwarm")
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.close()


if __name__ == "__main__":
    raw = generate_data()

    print("RAW DATA EXPLORATION")
    explore_data(raw)
    raw.to_csv("customer_churn_raw.csv", index=False)

    cleaned = clean_data(raw)

    print("\nCLEANED DATA VERIFICATION")
    print("Shape:", cleaned.shape)
    print("Missing values:\n", cleaned.isnull().sum())
    print("Duplicates:", cleaned.duplicated().sum())
    print("TotalCharges type:", cleaned["TotalCharges"].dtype)

    cleaned.to_csv("customer_churn_cleaned.csv", index=False)

    analyze_churn(cleaned)
    visualize(cleaned)

    print("\nEDA completed. CSV files and charts saved.")
