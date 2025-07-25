
# Arbor 

A simple yet powerful command-line tool to generate graphical or plain text directory trees. Perfect for documentation and project overviews.

## Features

- **Graphical Tree Output**: Generates a visually appealing tree structure, similar to the `tree` command.
- **Plain Text List**: Can output a simple, clean list of file paths.
- **File Filtering**: Easily filter which files to include using glob patterns (e.g., `*.py`, `*.md`).
- **Custom Output File**: Specify the name of the output file.
- **Cross-Platform**: Written in Python, runs on Windows, macOS, and Linux.

## Installation

### For End-Users (Recommended)

1.  Go to the [**Releases**](https://github.com/happynumeric/arbor/releases) page.
2.  Download the latest `arbor.exe` file from the assets.
3.  Place `arbor.exe` in a folder that is in your system's PATH, or run it directly from its location.

### For Developers

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

This project is licensed under the MIT License

----------

Copyright (c) 2025 happynumeric.com (hello@happynumeric.com)