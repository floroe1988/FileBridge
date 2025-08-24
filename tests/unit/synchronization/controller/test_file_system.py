from tests.unit.synchronization.shared.base_test import BaseTest
from src.pages.synchronization.model.files import Folder
from src.pages.synchronization.controller.file_system import toggle_folder


class TestFileSystemController(BaseTest):

    def test_toggle_folder(self):
        folder = Folder(path=self.test_root, parent=None)
        assert folder.collapsed is True
        toggle_folder(folder=folder)
        assert folder.collapsed is False
        toggle_folder(folder=folder)
        assert folder.collapsed is True
