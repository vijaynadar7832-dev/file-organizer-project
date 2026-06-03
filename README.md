# Cross-Platform File Organizer

A robust command-line automation utility built in Python to cleanly sort chaotic workspace directories. The script reads file signatures dynamically and allocates them into distinct, dedicated system folders while managing system errors defensively.

## 🚀 Features
* **Expanded Extension Mapping:** Handles diverse asset workflows including development scripts, heavy archives, system extensions, and multimedia formats.
* **Smart Directory Generation:** Automatically builds missing host folders on the fly during runtime.
* **Fault-Tolerant Architecture:** Employs explicit `try-except` blocks to catch access constraints or system movement interruptions without killing the execution loop.
* **Platform Agnostic:** Formulates path structures dynamically, allowing seamless execution on Linux, macOS, and Windows.

## 🛠️ Tech Stack & Utilities
* **Language:** Python 3.x
* **Core Packages:** `os`, `shutil` (Built-in standard library utilities)
* **Environment:** Cross-Platform (Linux Terminal, Windows PowerShell, macOS Terminal)
* **Version Control:** Git & GitHub

## 📂 How It Works
Before execution:
```text
📁 Cluttered_Folder/
     organizer.py
     financial_report.pdf
     capture.png
     instructions.txt
     automation.py
```

After executing the script:
```text
📁 Cluttered_Folder/
    📄 organizer.py
    📁 Documents/
         financial_report.pdf
         instructions.txt
    📁 Images/
         capture.png
    📁 Scripts/
         automation.py
```

## 🗂️ Supported Classifications
The script intelligently parses and organizes files into seven distinct categories:
*  **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.psd`
*  **Audio & Video:** `.mp4`, `.mov`, `.avi`, `.mp3`, `.wav`
*  **Documents:** `.txt`, `.pdf`, `.docx`
*  **Archives & Data:** `.zip`, `.rar`, `.7z`, `.iso`
*  **Programming & Scripts:** `.py`, `.sh`, `.html`, `.htm`, `.css`, `.js`, `.php`, `.java`, `.cpp`, `.c`
*  **System & Executables:** `.exe`, `.dll`, `.sys`, `.bat`, `.cfg`, `.ini`
*  **Others:** Any unmapped or custom application extension.

## ⚙️ How to Use

### 1. Clone the Code Base
```bash
git clone https://github.com/vijaynadar7832-dev/file-organizer-project
cd YOUR_REPOSITORY_NAME
```

### 2. Run the Command
Place the script in the target folder you want to clean up and execute:

* **Linux / macOS Terminal:**
  ```bash
  python3 organizer.py
  ```
* **Windows Command Prompt / PowerShell:**
  ```powershell
  python organizer.py
  ```
