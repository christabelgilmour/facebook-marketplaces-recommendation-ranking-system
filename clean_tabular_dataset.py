import pandas as pd

class data_cleaning():

    def clean_product_dataset():
        df = pd.read_csv("Products.csv", index_col=0)
        df = df.dropna(axis=0)
        df["price"] = df["price"].str.strip("£")
        df["price"] = df["price"].str.replace(",","")
        df["price"] = df["price"].astype("float64")
        print(df)


if __name__ == "__main__":
    data_cleaning.clean_product_dataset()
