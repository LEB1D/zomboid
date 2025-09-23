from main import Inventory  # Ваш клас Inventory у окремому файлі
import sys


def print_menu():
    print("\n--- Inventory CLI ---")
    print("1. Отримати предмет по ID")
    print("2. Пошук предмета по назві")
    print("3. Відсоток по стану всіх предметів")
    print("4. Відсоток по стану предметів певної назви")
    print("5. Вийти")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_csv>")
        return

    file_path = sys.argv[1]
    inv = Inventory(file_path)

    while True:
        print_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            id_ = int(input("ID предмета: "))
            print(inv.get_by_id(id_))

        elif choice == "2":
            name = input("Назва предмета: ")
            print(inv.search_by_name(name))

        elif choice == "3":
            print("--- Відсоток по стану всіх предметів ---")
            for cond, pct in inv.state_percentages().items():
                print(f"{cond}: {pct}%")

        elif choice == "4":
            name = input("Назва предмета: ")
            print(f"--- Відсоток по стану для '{name}' ---")
            for cond, pct in inv.state_percentages(name).items():
                print(f"{cond}: {pct}%")

        elif choice == "5":
            print("Вихід.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
