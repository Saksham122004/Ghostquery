# GhostQuery

GhostQuery is a terminal-based OSINT-style Google search query constructor built in Python.

It provides an interactive, animated command-line interface that helps users generate advanced Google search queries using supported search operators.

This version runs entirely in a single terminal interface and does not require any external dependencies.

---

## Features

- Single all-in-one terminal interface
- OSINT-style animated startup
- ANSI-based hacker terminal color theme
- Advanced Google search operator support
- Optional direct browser launch
- No external libraries required
- Cross-platform (Windows / Linux / macOS)

---

## Supported Search Operators

GhostQuery supports the following Google search operators:

- `site:example.com`  
  Restrict results to a specific domain.

- `filetype:pdf`  
  Search for specific file extensions.

- `inurl:keyword`  
  Require keyword to appear in URL.

- `intitle:keyword`  
  Require keyword to appear in page title.

- `"exact phrase"`  
  Match an exact phrase.

- `-keyword`  
  Exclude results containing a specific keyword.

---

## Requirements

- Python 3.8 or higher
- No external dependencies

Uses only Python standard library modules:
- webbrowser
- urllib.parse
- sys
- time
- os

---

## Installation

Clone the repository:
git clone https://github.com/Saksham122004/Ghostquery.git

cd GhostQuery

Or simply download `ghostquery.py`.

---

## Usage

Run the tool:
python ghostquery.py


After launch:

1. The system initializes with animated OSINT-style startup.
2. Select an option:
   - 1 → Build Query
   - 2 → Clear Screen
   - 3 → Exit
3. Enter any combination of supported search filters.
4. The generated query will be displayed.
5. Optionally open the query directly in your browser.

---

## Example

Input:
Exact phrase: cybersecurity report
Site: example.com
Filetype: pdf


## Disclaimer

This tool is intended for educational, research, and authorized OSINT usage only.

The developer is not responsible for misuse or unauthorized activities performed using this tool.




