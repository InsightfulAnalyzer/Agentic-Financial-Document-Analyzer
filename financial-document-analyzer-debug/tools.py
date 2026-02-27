# tools.py

import pdfplumber
from crewai.tools import BaseTool


class ReadFinancialDocumentTool(BaseTool):
    name: str = "read_financial_document"
    description: str = "Reads a financial PDF document and returns cleaned text content."

    def _run(self, path: str) -> str:
        full_report = ""

        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_report += text + "\n"

        return full_report