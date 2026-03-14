# File Integrity Monitor (Python)

## Overview

This project implements a simple **File Integrity Monitor (FIM)** in Python. The tool scans a directory, calculates **SHA-256 cryptographic hashes** for all files, and compares them against a previously saved baseline to detect integrity changes.

The goal of the project is to demonstrate core security monitoring concepts used in defensive cybersecurity, particularly the detection of **unauthorized file modifications, additions, or deletions**.

File integrity monitoring is a fundamental technique used by security tools and host-based intrusion detection systems to identify potential tampering or malicious activity on a system.

---

## Objectives

This project was built to demonstrate practical understanding of several cybersecurity and programming concepts:

* Implementing **cryptographic hashing (SHA-256)** for file verification
* Building a **baseline of trusted file states**
* Detecting **file modifications, additions, and deletions**
* Automating filesystem analysis using Python
* Handling errors and edge cases in file processing
* Structuring a small security tool with clear and maintainable code

The project reflects foundational skills relevant to host-based security monitoring and integrity verification systems.

---

## How It Works

1. The program scans a target directory recursively.
2. Each file is hashed using the **SHA-256 algorithm**.
3. Hashes are stored in a dictionary mapping:

```
file_path → file_hash
```

4. On the first run, the program creates a **baseline snapshot** and stores it in `baseline.json`.
5. On later runs, the program compares the current scan with the baseline to identify:

   * **Modified files** (hash mismatch)
   * **New files** (not present in baseline)
   * **Deleted files** (missing from the current scan)

Changes are displayed in the console with color-coded alerts.

---

## Project Structure

```
.
├── fim.py
├── baseline.json
├── test_folder/
│   ├── file1.txt
│   └── file2.txt
└── README.md
```

* **fim.py** — main program
* **baseline.json** — stored baseline file hashes
* **test_folder/** — directory monitored by the script

---

## Installation

Requirements:

* Python 3.x

Clone the repository:

```
git clone https://github.com/SantaLauk/File-integrity-monitor.git
cd File-integrity-monitor
```

No additional dependencies are required.

---

## Usage

Run the script:

```
python fim.py
```

### First Run

If no baseline exists, the script creates one automatically:

```
No baseline found. Creating initial baseline...
Baseline saved to baseline.json
Baseline created. Run the script again to detect changes.
```

### Monitoring Changes

After the baseline exists, run the script again to detect changes.

Example output:

```
Modified: test_folder/file1.txt
Added: test_folder/file3.txt
Deleted: test_folder/file2.txt
```

Color-coded alerts:

* **Yellow** → modified files
* **Green** → added files
* **Red** → deleted files

---

## Example Test Scenario

1. Create test files

2. Run the script to create the baseline.

3. Modify a file

4. Run the script again to detect the modification.

---

## Security Concepts Demonstrated

This project demonstrates several concepts commonly used in defensive security tools:

* Cryptographic hashing for file verification
* Integrity baselining
* Change detection
* Basic host-based monitoring
* Structured error handling

Many enterprise security tools implement similar techniques internally for **tamper detection and system monitoring**.

---

## Possible Improvements

Future enhancements could include:

* Real-time monitoring using filesystem events
* Logging alerts to a file
* Email or webhook notifications
* Command-line arguments for directory selection
* Whitelisting trusted changes
* Integration with SIEM or security monitoring platforms

---

## Author

This project was created as part of a cybersecurity learning path focused on building practical security tools and demonstrating foundational knowledge in system monitoring and defensive security practices.

