import pandas as pd
from pathlib import Path
import sys
from .config import DATA_RAW, OUTPUT_TABLES

def load_state_files() -> pd.DataFrame:
    """Load all SC.txt state files into a single DataFrame."""
    files = sorted(DATA_RAW.glob("*.txt")) + sorted(DATA_RAW.glob("*.TXT"))
    print(f"Found {len(files)} files: {[f.name for f in files[:5]]}...")
    
    if not files:
        print("ERROR: No .txt or .TXT files found in", DATA_RAW)
        sys.exit(1)
    
    frames = []
    for f in files:
        try:
            print(f"Loading {f.name}...")
            df = pd.read_csv(
                f,
                header=None,
                names=["state", "sex", "year", "name", "count"],
                dtype={"state": "string", "sex": "string", "year": "int16",
                       "name": "string", "count": "int32"},
            )
            print(f"  Loaded {len(df)} rows from {f.name}")
            frames.append(df)
        except Exception as e:
            print(f"Failed to load {f}: {e}")
            continue

    if not frames:
        raise ValueError("No files could be successfully loaded")
    
    all_data = pd.concat(frames, ignore_index=True)
    print(f"Total dataset shape: {all_data.shape}")
    return all_data

def save_normalized(all_data: pd.DataFrame, path: Path = OUTPUT_TABLES / "all_data.parquet"):
    """Save normalized data for fast reloading."""
    path.parent.mkdir(parents=True, exist_ok=True)
    all_data.to_parquet(path, index=False)
    print(f"Saved normalized data to {path}")

def load_normalized(path: Path = OUTPUT_TABLES / "all_data.parquet") -> pd.DataFrame:
    """Load previously saved normalized data."""
    if not path.exists():
        raise FileNotFoundError(f"Normalized data not found at {path}. Run load_state_files() first.")
    return pd.read_parquet(path)

