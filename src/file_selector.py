import os


def select_json_file(directory="../input"):
    json_files = [f for f in os.listdir(directory) if f.endswith(".json")]

    if not json_files:
        print("⚠️ No JSON files found.")
        return None

    print("\n🗂 Available JSON files:")
    for i, file in enumerate(json_files, start=1):
        print(f"{i}. {file}")

    while True:
        try:
            choice = int(input("\n🔍 Select a JSON file by number: ")) - 1
            if 0 <= choice < len(json_files):
                return os.path.join(directory, json_files[choice])
        except ValueError:
            pass
        print("🚫 Invalid choice. Try again.")
