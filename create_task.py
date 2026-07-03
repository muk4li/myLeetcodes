import os
import sys
import json
import shutil
import requests
from datetime import datetime

# Konstanten
TEMPLATE_DIR = "0000_FolderTemplate"
TEMPLATE_FILE = os.path.join(TEMPLATE_DIR, "solutionTemplate.py")
API_URL = "https://leetcode.com/api/problems/all/"

def fetch_problem_data(problem_id):
    """Holt alle Aufgaben von LeetCode und sucht nach der übergebenen ID."""
    print(f"Lade Daten von LeetCode für Aufgabe {problem_id}...")
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        
        for problem in data["stat_status_pairs"]:
            if str(problem["stat"]["frontend_question_id"]) == str(problem_id):
                title = problem["stat"]["question__title"]
                slug = problem["stat"]["question__title_slug"]
                level = problem["difficulty"]["level"]
                tags = [tag["name"] for tag in problem.get("tags", [])]
                
                # Schwierigkeitsgrad mappen (1=Easy, 2=Medium, 3=Hard)
                difficulty_map = {1: "Easy", 2: "Medium", 3: "Hard"}
                difficulty = difficulty_map.get(level, "Unknown")
                
                return {
                    "title": title,
                    "slug": slug,
                    "difficulty": difficulty,
                    "tags": tags
                }
    except Exception as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
        return None
        
    print(f"Aufgabe {problem_id} nicht bei LeetCode gefunden!")
    return None

def sanitize_folder_name(name):
    """Macht den Titel ordnerkonform (keine Leer- oder Sonderzeichen)."""
    return name.replace(" ", "").replace("-", "")

def create_task_folder(problem_id):
    # 1. Daten abrufen
    problem_data = fetch_problem_data(problem_id)
    if not problem_data:
        return

    # 2. Ordnernamen generieren
    folder_name = f"{str(problem_id).zfill(4)}_{sanitize_folder_name(problem_data['title'])}"
    
    if os.path.exists(folder_name):
        print(f"Der Ordner '{folder_name}' existiert bereits!")
        return

    # 3. Ordner erstellen
    os.makedirs(folder_name)
    print(f"Ordner '{folder_name}' erstellt.")

    # 4. solution.py kopieren
    if os.path.exists(TEMPLATE_FILE):
        shutil.copy(TEMPLATE_FILE, os.path.join(folder_name, f"solution{problem_id}.py"))
        print("solution.py aus Template erstellt.")
    else:
        print("WARNUNG: Template-Datei nicht gefunden!")

    # 5. metadata.json erstellen
    now = datetime.now()
    date_str = now.strftime("%d.%m.%Y")
    time_str = now.strftime("%H:%M")

    metadata = {
        "problem": str(problem_id).zfill(4),
        "title": problem_data["title"],
        "url": f"https://leetcode.com/problems/{problem_data['slug']}/",
        "difficulty": problem_data["difficulty"],
        "tags": problem_data["tags"],
        "status": "in_progress",
        "started": {
            "time": time_str,
            "date": date_str
        },
        "finished": {
            "time": "00:00",
            "date": "01.01.2001"
        },
        "evalfin": {
            "time": "99:99",
            "date": "01.01.2001",
            "duration": "99"
        },
        "complexity_mine": {
            "time": "O(?)",
            "space": "O(?)"
        },
        "complexity_optimal": {
            "time": "O(?)",
            "space": "O(?)"
        }
    }

    metadata_path = os.path.join(folder_name, "metadata.json")
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
    
    print("metadata.json erstellt.")
    print("\n✅ Aufgabe erfolgreich angelegt! Viel Erfolg beim Lösen.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Benutzung: python create_task.py <Aufgaben-Nummer>")
        print("Beispiel: python create_task.py 1")
    else:
        create_task_folder(sys.argv[1])