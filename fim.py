
import os
import hashlib
import json

# Colors for console alerts
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Hash a single file
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        file = open(file_path, "rb")
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha256.update(chunk)
        file.close()

        return sha256.hexdigest()
    
    except Exception as e:
        print(f"Error hashing {file_path}: {e}")
        return None

# Scan all files in a directory
def scan_directory(directory):
    file_hashes = {}

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_hash(file_path)
            if file_hash is not None:
                file_hashes[file_path] = file_hash
        
    return file_hashes
    
target_directory = "test_folder"

# Save baseline to JSON
def save_baseline(file_hashes, filename="baseline.json"):
    try:
        with open(filename, "w") as f:
            json.dump(file_hashes, f, indent=4)
        print(f"Baseline saved to {filename}")
    except Exception as e:
        print(f"Error saving baseline: {e}")

# Load baseline from JSON
def load_baseline(filename="baseline.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"No baseline file found at {filename}.")
        return {}
    
    except Exception as e:
        print(f"Error loading baseline: {e}")
        return {}
    
# Compare scans
def compare_scans(baseline, current_scan):
    modified = []
    added = []
    deleted = []

    for path, old_hash in baseline.items():
        if path not in current_scan:
            deleted.append(path)
        elif current_scan[path] != old_hash:
            modified.append(path)

    for path in current_scan:
        if path not in baseline:
            added.append(path)

    return modified, added, deleted

# Main execution
if __name__ == "__main__":
    target_directory = "test_folder"
    baseline_file = "baseline.json"

baseline = load_baseline(baseline_file)

# If no baseline exists, create one
if not baseline:
        print("No baseline found. Creating initial baseline...")
        baseline = scan_directory(target_directory)
        save_baseline(baseline)
        print("Baseline created. Run the script again to detect changes.")
        exit()

# Scan current folder
current_scan = scan_directory(target_directory)

# Compare baseline with current scan
modified, added, deleted = compare_scans(baseline, current_scan)

# Print results with colors
for f in modified:
    print(f"{YELLOW}Modified: {f}{RESET}")

for f in added:
    print(f"{GREEN}Added: {f}{RESET}")

for f in deleted:
    print(f"{RED}Deleted: {f}{RESET}")