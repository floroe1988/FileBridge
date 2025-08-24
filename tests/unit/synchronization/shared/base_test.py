import shutil
from pathlib import Path
import yaml


class BaseTest:

    def setup_method(self):
        # Create test data folder structure
        self.test_root = Path(
            "tests/unit/synchronization/test_data"
        )  # pylint: disable=W0201
        self.subfolder = self.test_root / "subfolder"  # pylint: disable=W0201
        self.test_root.mkdir(parents=True, exist_ok=True)
        self.subfolder.mkdir(parents=True, exist_ok=True)
        # Create files
        (self.test_root / "file1.txt").write_text("Root file")
        (self.subfolder / "file2.txt").write_text("Subfolder file 2")
        (self.subfolder / "file3.txt").write_text("Subfolder file 3")

        # Create a temporary config file pointing to the test folder
        self.config_path = (
            self.test_root.parent / "test_config.yaml"
        )  # pylint: disable=W0201
        config_data = {"folder_config": {"input_folder": str(self.test_root)}}
        with open(self.config_path, "w", encoding="utf-8") as f:
            yaml.dump(config_data, f)

    def teardown_method(self):
        # Remove test data folder and config file after test
        shutil.rmtree(self.test_root)
        if hasattr(self, "config_path") and self.config_path.exists():
            self.config_path.unlink()
