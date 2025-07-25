

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

## Installation and Setup 
To use `arbor.exe` from  any location in your command prompt, it is recommended to place it in a dedicated folder and  add that folder to the Windows `PATH`. 

1.  **Create a Dedicated Folder** (e.g., `C:\Tools`). 
2. **Place the `arbor.exe` file**  into this new directory. 
3. **Add the Folder to the Windows PATH**: 
	*  Search  for "Edit the system environment variables". 
	* Click on "Environment Variables...". 
	* In the "User variables" section, select `Path` and click "Edit...". 
	* Click "New" and paste the path to your folder (`C:\Tools`). 
	* Confirm by clicking "OK" on  all windows. 
4. **Verify the Setup**: **Close  and reopen a new console window**. Type `arbor /?`. If the help message appears, you're all set! 

## Command Reference 
### General Syntax 
`arbor [path] [filter1] [filter2] ... [options]` 
### Arguments and Options 
- `[path]` (Optional) 
	- The path to the directory to analyze. If omitted, analyzes the **current directory**. 
	- If the path contains spaces, enclose it in quotes: `"C:\My Project"`. 

- `[filters]` (Optional) 
	- One or more patterns to filter which files to include (e.g., `*.txt`, `image_*.jpg`, `*.*`). 
	- If omitted, all files are included (`*.*`). 

- `/o, -o, --output <file>` (Optional) 
	- Specifies the output filename. If omitted, the default name is **`tree.txt`**. 

- `/t, -t` (Optional) 
	- Activates **text mode** (outputs a simple list of paths). 

- `/?, -h, --help` 
	- Displays the help message. 

- `/v, --version` 
	- Displays the program's version. 

## Usage Examples 
-  **Analyze the current directory (output to `tree.txt`)** 
`arbor *.*` 

-  **Include only HTML, CSS, and JavaScript files** 
`arbor *.html *.css *.js` 

-  **Analyze a specific directory and save the output to "report.txt"** 
`arbor "C:\MyProject" /o report.txt` 

-  **Generate a simple list of  all files in "file_list.log"** 
`arbor /t /o file_list.log` 

-  **Combine all options** 
`arbor "D:\Archives" *.zip *.rar /t /o archive_list.txt`

## License
this project is licensed under the MIT License. See the `LICENSE` file for details.

--- Copyright (c) 2025 happynumeric.com (hello@happynumeric.com)