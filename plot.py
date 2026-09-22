import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("exported_books.csv")

plt.scatter(df["price"], df["rating"])

plt.title("Book Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Rating")

plt.savefig("price_vs_rating.png")

plt.show()