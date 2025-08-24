from tests.unit.synchronization.shared.base_test import BaseTest
from src.pages.synchronization.model.files import (
    FolderStatistics,
    Folder,
    File,
    FileSystem,
)


class TestFolderStatistics:

    def test_initialization(self) -> None:
        stats = FolderStatistics(
            total_folders=5, total_files=10, unsynced_folders=2, unsynced_files=3
        )
        assert stats.total_folders == 5
        assert stats.total_files == 10
        assert stats.unsynced_folders == 2
        assert stats.unsynced_files == 3

    def test_synced(self) -> None:
        # Unsynced folder: unsynced_folders and unsynced_files > 0
        stats = FolderStatistics(
            total_folders=2, total_files=4, unsynced_folders=1, unsynced_files=2
        )
        assert stats.synced is False

        # Update to synced: unsynced_folders and unsynced_files == 0
        stats.unsynced_folders = 0
        stats.unsynced_files = 0
        assert stats.synced is True


class TestFile(BaseTest):

    def test_initialization(self) -> None:
        parent = Folder(path=self.test_root, parent=None)
        file = File(parent=parent, path=self.test_root / "file1.txt", name="file1.txt")
        assert file.parent == parent
        assert file.path == self.test_root / "file1.txt"
        assert file.name == "file1.txt"
        assert file.synced is False


class TestFolder(BaseTest):

    def test_initialization(self) -> None:
        folder = Folder(path=self.test_root, parent=None)
        # Check root folder files
        file_names = [file.name for file in folder.files]
        assert "file1.txt" in file_names
        # Check subfolders
        subfolder_names = [subfolder.path.name for subfolder in folder.folders]
        assert "subfolder" in subfolder_names
        # Check files in subfolder
        subfolder_obj = next(f for f in folder.folders)
        subfolder_file_names = [file.name for file in subfolder_obj.files]
        assert "file2.txt" in subfolder_file_names
        assert "file3.txt" in subfolder_file_names

    def test_toggle(self) -> None:
        folder = Folder(path=self.test_root, parent=None)

        initial_collapsed = folder.collapsed
        for subfolder in folder.folders:
            assert subfolder.collapsed is True

        # Toggle collapsed state of parent
        folder.toggle()

        assert folder.collapsed != initial_collapsed
        for subfolder in folder.folders:
            assert subfolder.collapsed is True
            subfolder.toggle()
            assert subfolder.collapsed is False

        # Toggle collapsed state of parent
        folder.toggle()

        assert folder.collapsed == initial_collapsed
        for subfolder in folder.folders:
            assert subfolder.collapsed is True


class TestFileSystem(BaseTest):

    def test_initialization(self) -> None:
        file_system = FileSystem(path=self.test_root)
        assert file_system.path == self.test_root
        assert file_system.parent is None
