from typing import Any
from pathlib import Path
import yaml
from .files import FileSystem, FolderStatistics


class SyncPageData:

    def __init__(self, conf: Path) -> None:

        # Read configuration from config.yaml
        with open(conf, "r", encoding="utf-8") as file:
            config: dict[str, dict[str, Any]] = yaml.safe_load(file)

        input_folder = config.get("folder_config", {}).get("input_folder", "")
        self.file_system = FileSystem(path=Path(input_folder))

        self.folder_stats: FolderStatistics = self.file_system.statistics
