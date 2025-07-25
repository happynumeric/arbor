

# Arbor 

[![Latest Release](https://img.shields.io/github/v/release/happynumeric/arbor?style=for-the-badge)](https://github.com/happynumeric/arbor/releases/latest)

A simple command-line tool for Windows to generate a visual, text-based representation of a directory structure.
It is inspired by commands like `tree` in Linux or `dir /s` in Windows, but with more visual output and convenient filtering options.
The result is saved to a `tree.txt` file, ideal for project documentation, archives, or sharing folder structure.

### Example Output:
```
/my-project/  
   ├── index.html
   ├── css/
   │   └── style.css
   └── js/ 
       ├── app.js 
       └── utils.js
```
## Main Features
- **Graphical Tree Output**: Displays a clear structure with connectors. 
- **Plain Text List**: An option `/t` to generate a simple list of file paths. 
- **File Filtering**: Include only files matching specific patterns (e.g., `*.py`, `*.md`). 
- **Standalone Executable**: `arbor.exe` is a single file that runs without needing Python installed. 
- **Built-in Help**: Comprehensive help system (`arbor /?`) and version command (`arbor /v`).

## 🚀 Download & Installation 
The easiest way to  get Arbor is  to download the latest executable for Windows. 
A detailed user guide is included in the download. 
**➡️ [Download the latest version from the Releases page](https://github.com/happynumeric/arbor/releases/latest) ⬅️**

## For Developers

If you have Python installed, you can run the script directly.

1.  Clone the repository:
    ```bash
    git clone https://github.com/happynumeric/arbor.git
    ```
2.  Navigate to the directory:
    ```bash
    cd arbor
    ```
3.  Run the script:
    ```bash
    python arbor.py [arguments]
    ```

## Usage
```bash
arbor.exe [path] [filters...] [/o OUTPUT_FILE] [/t]
```

### Examples

**1. Generate a tree of the current directory:**
```bash
arbor.exe
```
**2. Filter for Python and Markdown files in a specific project folder:**
```bash
arbor.exe "C:\MyProject" *.py *.md
```
**3. Generate a plain text list of files and save it to filelist.log:**
```bash
arbor.exe /t /o filelist.log
```

## License
this project is licensed under the MIT License. See the `LICENSE` file for details.

--- Copyright (c) 2025 happynumeric.com (hello@happynumeric.com)