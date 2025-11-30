# 6 Лабораторная.
# 1  Анализатор данных о продажах

import csv
import json


totl_revenue = 0
unique_prod = {}

# читаем данные из файла
with open("sales.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        product = row.get("product_name")
        qty = int(row.get("quantity"))
        price = int(row.get("price_per_unit"))

        revenue = qty * price

        if product not in unique_prod:
            unique_prod[product] = {"quantity": 0, "revenue": 0}

        unique_prod[product]["quantity"] += qty
        unique_prod[product]["revenue"] += revenue
        totl_revenue += revenue


best_sell_key, best_sell_stats = max(unique_prod.items(), key=lambda x: x[1]["quantity"])
most_profit_key, most_profit_stats = max(unique_prod.items(), key=lambda x: x[1]["revenue"])

summary = {
    "total_revenue": totl_revenue,
    "best_selling_product": {
        "name": best_sell_key,
        "quantity": best_sell_stats["quantity"],
        "revenue": best_sell_stats["revenue"],
    },
    "most_profitable_product": {
        "name": most_profit_key,
        "quantity": most_profit_stats["quantity"],
        "revenue": most_profit_stats["revenue"],
    }
}

with open("sales_summary.json", "w", encoding="utf-8") as json_file:
    json.dump(summary, json_file, indent=4, ensure_ascii=False)
