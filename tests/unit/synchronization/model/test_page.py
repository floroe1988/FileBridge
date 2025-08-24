from tests.unit.synchronization.shared.base_test import BaseTest
from src.pages.synchronization.model.page import SyncPageData


class TestSyncPageData(BaseTest):

    def test_initialization(self) -> None:

        page = SyncPageData(conf=self.config_path)

        assert page.file_system.path == self.test_root
        assert page.folder_stats.total_files == 3  # 1 in root, 2 in subfolder
        assert page.folder_stats.total_folders == 1  # 1 subfolder
