from datetime import datetime

entries = []

def add_entry(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entries.append({"timestamp": timestamp, "text": text})

def view_entries():
    for entry in entries:
        print(f"[{entry['timestamp']}] {entry['text']}")

if __name__ == "__main__":
    add_entry("Started learning Python today!")
    add_entry("Had a great workout session.")
    view_entries()
