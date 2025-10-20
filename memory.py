import json
from pathlib import Path
from typing import Any, Dict
from config import Config

class MemoryStore:
    def __init__(self, path: str = None):
        self.path = Path(path or Config.MEMORY_PATH)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._write({})
        self.data = self._read()

    def _read(self) -> Dict[str, Any]:
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _write(self, obj: Dict[str, Any]):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(obj, f, indent=2, default=str)

    def get(self, key: str, default=None):
        return self.data.get(key, default)

    def set(self, key: str, value: Any):
        self.data[key] = value
        self._write(self.data)

    def append_interaction(self, client_id: str, interaction: Dict[str, Any]):
        interactions = self.data.setdefault(client_id, {}).setdefault('interactions', [])
        interactions.append(interaction)
        self._write(self.data)
