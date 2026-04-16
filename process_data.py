import pandas as pd

df1 = pd.read_csv("data/daily_sales_data_0.csv")  # Read the first CSV file into a DataFrame
df2 = pd.read_csv("data/daily_sales_data_1.csv")  # Read the second CSV file into a DataFrame
df3 = pd.read_csv("data/daily_sales_data_2.csv")  # Read the third CSV file into a DataFrame

df = pd.concat([df1, df2, df3]) # Concatenate the three DataFrames into a single DataFrame

df = df[df["product"].str.lower() == "pink morsel"] # Filter the DataFrame to include only rows where the product column is Pink Morsel

df["sales"] = df["quantity"] * df["price"] # Create a new column called sales by multiplying the quantity and price columns

df = df[["sales", "date", "region"]] # Select only the sales, date, and region columns from the DataFrame

df.to_csv("processed_data.csv", index=False) # Save the processed DataFrame to a new CSV file 

print("Completed processing data and saved to processed_data.csv")
