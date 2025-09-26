import csv
from collections import Counter


class Item:
    def __init__(self, id, name, type_, condition, amount):
        self.id = int(id)
        self.name = name
        self.type = type_
        self.condition = condition
        self.amount = int(amount) if amount else 0

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.type}, {self.condition}) x{self.amount}"


class Inventory:
    def __init__(self, path):
        self.items = []
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.items.append(Item(
                    row["ID"], row["Name"], row["Type"], row["Condition"], row["Amount"]
                ))

    def show_page(self, page, page_size=10):
        start = (page - 1) * page_size
        end = start + page_size
        for item in self.items[start:end]:
            print(item)

    def get_by_id(self, id_):
        return [i for i in self.items if i.id == id_]

    def search_by_name(self, name):
        name = name.lower()
        return [i for i in self.items if name in i.name.lower()]

    def state_percentages(self, name_filter=None):
        filtered = self.items
        if name_filter:
            filtered = [i for i in self.items if name_filter.lower()
                        in i.name.lower()]
        total = sum(i.amount for i in filtered)
        if total == 0:
            return {}
        counter = Counter()
        for i in filtered:
            counter[i.condition] += i.amount
        return {cond: round(amt/total*100, 2) for cond, amt in counter.items()}


inv = Inventory("data\items.csv")

print("=== Search by name'Nails'===")
print(inv.search_by_name("Nails"))

print("=== Search by ID ===")
print(inv.get_by_id(3))

percent_all = inv.state_percentages()
print("Відсоток по стану всіх предметів:")
for cond, pct in percent_all.items():
    print(f"{cond}: {pct}%")


percent_nails = inv.state_percentages("Nails")
print("\nВідсоток по стану предметів з назвою 'Nails':")
for cond, pct in percent_nails.items():
    print(f"{cond}: {pct}%")
