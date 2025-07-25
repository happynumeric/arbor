# -*- coding: utf-8 -*-
import os
import sys
import argparse
import fnmatch
import datetime
import textwrap
# --- Program Metadata ---
VERSION = "1.0.0" # First English release
CURRENT_YEAR = 2025 # As requested
COPYRIGHT = f"Copyright (c) {CURRENT_YEAR} happynumeric.com (hello@happynumeric.com)"
# --- Constants for GRAPHICAL tree drawing ---
T_CONNECTOR = "├── "
L_CONNECTOR = "└── "
LINE_PREFIX = "│   "
BLANK_PREFIX = "    "
def generate_graphical_tree(directory_path, filters, prefix=""):
    """
    Generates the graphical tree and returns it as a list of lines.
    """
    lines = []
    try:
        all_items = os.listdir(directory_path)
    except PermissionError:
        lines.append(f"{prefix}{T_CONNECTOR} [Access Denied]\n")
        return lines
    dirs = sorted([d for d in all_items if os.path.isdir(os.path.join(directory_path, d))])
    files = sorted([f for f in all_items if os.path.isfile(os.path.join(directory_path, f))])
    filtered_files = [f for f in files if any(fnmatch.fnmatch(f.lower(), p.lower()) for p in filters)]
    items_to_display = dirs + filtered_files
    for i, item_name in enumerate(items_to_display):
        is_last = (i == len(items_to_display) - 1)
        connector = L_CONNECTOR if is_last else T_CONNECTOR
        item_path = os.path.join(directory_path, item_name)
        if os.path.isdir(item_path):
            lines.append(f"{prefix}{connector}{item_name}/\n")
            new_prefix = prefix + (BLANK_PREFIX if is_last else LINE_PREFIX)
            lines.extend(generate_graphical_tree(item_path, filters, new_prefix))
        else:
            lines.append(f"{prefix}{connector}{item_name}\n")
    return lines
def generate_text_list(start_dir, filters):
    """
    Generates a simple list of paths and returns it as a list of lines.
    """
    lines = []
    for root, dirs, files in os.walk(start_dir, topdown=True):
        dirs.sort()
        files.sort()
        relative_path_from_parent = os.path.relpath(root, os.path.dirname(start_dir))
        if root == start_dir:
            lines.append(f"./{os.path.basename(start_dir)}/\n")
        for file in files:
            if any(fnmatch.fnmatch(file.lower(), p.lower()) for p in filters):
                display_file_path = os.path.join(".", relative_path_from_parent, file)
                lines.append(f"{display_file_path.replace(os.sep, '/')}\n")
    return lines
if __name__ == "__main__":
    help_epilog = textwrap.dedent(f"""
    -----------------
    Usage Examples:
    -----------------
    1. Analyze the current directory (output to tree.txt):
       arbor.exe
    2. Display to screen AND save to file:
       arbor.exe *.*
    3. Specify an output filename with a filter:
       arbor.exe *.py /o python_report.txt
    4. Analyze a specific directory with multiple filters:
       arbor.exe "C:\\Projects" *.py *.md
    5. Generate plain text output and name the file:
       arbor.exe /t /o file_list.log
    {COPYRIGHT}
    """)
    parser = argparse.ArgumentParser(
        description="Generates a file and directory tree structure.",
        epilog=help_epilog,
        add_help=False,
        prefix_chars='-/',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "args", nargs='*',
        help="Path to the directory and/or filters (e.g., *.txt, *.js)."
    )
    parser.add_argument(
        '-o', '/o', '--output',
        dest='output_filename',
        metavar='FILE',
        help="Specifies the output filename (default: tree.txt)."
    )
    parser.add_argument(
        '-t', '/t', dest='text_mode', action='store_true',
        help="Generate output in plain text mode (list of paths)."
    )
    parser.add_argument(
        '-h', '--help', '-?', '/?', '/help', action='help',
        help="Show this help message and exit."
    )
    parser.add_argument(
        '-v', '--version', '/v', action='version',
        version=f'%(prog)s {VERSION}\\n{COPYRIGHT}',
        help="Show program's version number and exit."
    )
    if not sys.argv[1:]:
        parser.print_help()
        sys.exit(0)
    parsed_args = parser.parse_args()
    target_dir = "."
    filters = []
    non_flag_args = [arg for arg in parsed_args.args if not arg.startswith(tuple(parser.prefix_chars))]
    if non_flag_args:
        if os.path.isdir(non_flag_args[0]):
            target_dir = non_flag_args[0]
            filters = non_flag_args[1:]
        else:
            filters = non_flag_args
    if not filters:
        filters = ['*.*']
    abs_target_dir = os.path.abspath(target_dir)
    output_filename = parsed_args.output_filename if parsed_args.output_filename else "tree.txt"
    tree_lines = []
    if parsed_args.text_mode:
        tree_lines = generate_text_list(abs_target_dir, filters)
    else:
        tree_lines.append(f"\\n/{os.path.basename(abs_target_dir)}/\\n")
        tree_lines.extend(generate_graphical_tree(abs_target_dir, filters))
    print("".join(tree_lines))
    try:
        with open(output_filename, "w", encoding="utf-8") as output_file:
            output_file.writelines(tree_lines)
        print("-" * 20) 
        print(f"[v] Tree successfully generated in: {os.path.abspath(output_filename)}\\n")
    except Exception as e:
        print(f"[x] An error occurred: {e}", file=sys.stderr)
