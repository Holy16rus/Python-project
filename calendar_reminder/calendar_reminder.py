import calendar
import datetime
import json
import os

EVENTS_FILE = "events.json"

def show_calendar(year, month):
    print(calendar.month(year, month))

def load_events():
    if not os.path.exists(EVENTS_FILE):
        return []
    with open(EVENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_events(events):
    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

def add_event(events):
    date_str = input("Введите дату события (ГГГГ-ММ-ДД): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Неверный формат даты!")
        return
    text = input("Введите описание события: ")
    events.append({"date": date_str, "text": text})
    save_events(events)
    print("Событие добавлено!")

def show_events(events):
    if not events:
        print("Нет событий.")
        return
    print("Список событий:")
    for event in events:
        print(f"{event['date']}: {event['text']}")

def main():
    events = load_events()
    while True:
        print("\n1. Показать календарь")
        print("2. Добавить событие")
        print("3. Показать события")
        print("4. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            year = int(input("Год: "))
            month = int(input("Месяц (1-12): "))
            show_calendar(year, month)
        elif choice == "2":
            add_event(events)
        elif choice == "3":
            show_events(events)
        elif choice == "4":
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()