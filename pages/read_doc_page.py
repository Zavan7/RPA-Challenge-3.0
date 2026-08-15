from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = BASE_DIR / "downloads"

FILE_CHALLENGE = DOWNLOAD_DIR / "challenge.xlsx"


class ReadDocPage:
    def __init__(self):
        self.file = FILE_CHALLENGE

    def read_challenge(self) -> list[dict]:
        df = pd.read_excel(self.file)

        return df.to_dict(orient="records")


teste = ReadDocPage()
print(teste.read_challenge())