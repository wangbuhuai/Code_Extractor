# Created by Dayu Wang (dwang@stchas.edu) on 2025-05-06

# Last updated by Dayu Wang (dwang@stchas.edu) on 2025-05-17


import tkinter as tk
from Constants import INITIAL_DIRECTORY, SUPPORTED_LANGUAGES
from LanguageDetector import LanguageDetector
from pyperclip import copy
from re import sub
from tkinter import filedialog
from typing import Literal


def main():
    # Let user select source code files.
    root: tk.Tk = tk.Tk()
    root.withdraw()
    file_paths: Literal[""] | tuple[str, ...] = filedialog.askopenfilenames(
        initialdir=INITIAL_DIRECTORY,
        title="Select Source Code Files",
        filetypes=([(
            "Source Code File",
            ["*.py", "*.java", "*.h", "*.c", "*.cpp", "*.cs", "*.html", "*.css", "*.js", "*.ts", "*.sql", "*.vb"]
        )])
    )
    if not file_paths: return  # User didn't select any file.
    code: str | None = None  # Code to input to the AI detector
    for file in file_paths:
        language: str | None = LanguageDetector(file).detect_language().lower()
        if language not in SUPPORTED_LANGUAGES: continue
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                # Only keep UTF-8 characters.
                line = sub(r"[^a-zA-Z0-9`~!@#$%^&*()-_=+|\\{}\[\];:'\",.<>/? ]", '', line)
                if len(line.strip()) == 0: continue  # Empty lines are ignored.
                # Check if the line contains any keywords that should be ignored.
                has_ignore_keyword: bool = False
                if SUPPORTED_LANGUAGES[language]:
                    for keyword in SUPPORTED_LANGUAGES[language]:
                        if line.startswith(keyword):
                            has_ignore_keyword = True
                            break
                if has_ignore_keyword: continue
                code = line if code is None else code + '\n' +line
    if code is None: print("No code detected.")
    else:
        copy("No Code" if code is None else code)
        print("Code copied to clipboard.")


if __name__ == "__main__":
    main()