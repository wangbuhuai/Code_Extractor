# Created by Dayu Wang (dwang@stchas.edu) on 2025-05-17

# Last updated by Dayu Wang (dwang@stchas.edu) on 2025-05-17


INITIAL_DIRECTORY: str = r"C:\Users\wangb\Downloads"


SUPPORTED_LANGUAGES: dict[str, set[str] | None] = {
    r"python": {r"import", r"from"},
    r"java": {r"import", r"package"},
    r"c/c++": {r"#ifndef", r"#define", r"#endif", r"#include", r"#pragma", r"using", r"[.ShellClassInfo]", r"LocalizedResourceName", r"IconResource"},
    "c#": {r"using"},
    "html": None,
    "css": None,
    "javascript": None,
    "typescript": None,
    "sql": None,
    "visual basic": None
}