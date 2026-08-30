from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "SMSSpamCollection"


def load_data(path=DATA_PATH):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Run: python download_dataset.py"
        )
    df = pd.read_csv(path, sep="\t", header=None, names=["label", "message"], encoding="utf-8")
    df["label"] = df["label"].str.lower().str.strip()
    df["message"] = df["message"].astype(str).str.strip()
    df = df.dropna().drop_duplicates().reset_index(drop=True)
    return df
