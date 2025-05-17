# Created by Dayu Wang (dwang@stchas.edu) on 2025-05-17

# Last updated by Dayu Wang (dwang@stchas.edu) on 2025-05-17


class LanguageDetector:
    def __init__(self, filename: str | None = None) -> None:
        """ Creates a "LanguageDetector" object.
            :param filename: Filename of the source code file.
        """
        # Data field
        self._filename: str | None = filename

    def detect_language(self) -> str | None:
        """ Detects the language of the source code file.
            :returns: The detected language
        """
        if self._filename.endswith(r".py"):
            return r"python"
        elif self._filename.endswith(r".java"):
            return r"java"
        elif self._filename.endswith(r".h") or self._filename.endswith(r".c") or self._filename.endswith(r".cpp"):
            return r"c/c++"
        elif self._filename.endswith(r".cs"):
            return r"c#"
        elif self._filename.endswith(r".html"):
            return r"html"
        elif self._filename.endswith(r".css"):
            return r"css"
        elif self._filename.endswith(r".js"):
            return r"javascript"
        elif self._filename.endswith(r".ts"):
            return r"typescript"
        elif self._filename.endswith(r".sql"):
            return r"sql"
        elif self._filename.endswith(r".vb"):
            return r"visual basic"
        else:
            return None  # Unsupported language