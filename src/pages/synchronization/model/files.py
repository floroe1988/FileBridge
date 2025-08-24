from pathlib import Path
from pydantic import BaseModel, Field


class FolderStatistics(BaseModel):
    total_folders: int = Field(default=0, description="Total number of folders")
    total_files: int = Field(default=0, description="Total number of files")
    unsynced_folders: int = Field(default=0, description="Number of unsynced folders")
    unsynced_files: int = Field(default=0, description="Number of unsynced files")

    @property
    def synced(self) -> bool:
        return self.unsynced_folders == 0 and self.unsynced_files == 0


class File:

    def __init__(self, parent: "Folder", path: Path, name: str) -> None:
        self.parent: "Folder" = parent
        self.path: Path = path
        self.name: str = name
        self.synced: bool = False


class Folder:

    def __init__(self, path: Path, parent: "Folder|None") -> None:
        self.parent: "Folder|None" = parent
        self.path: Path = path
        self.statistics: FolderStatistics = FolderStatistics()
        self.folders: list["Folder"] = []
        self.files: list[File] = []
        self.collapsed: bool = True

        self.collect_contents()

    def collect_contents(self) -> None:
        for item in self.path.iterdir():
            if item.is_dir():
                subfolder = Folder(path=item, parent=self)
                self.folders.append(subfolder)
                # Aggregate subfolder statistics
                self.statistics.total_folders += 1  # Count this subfolder
                self.statistics.unsynced_folders += (
                    1 if not subfolder.statistics.synced else 0
                )
                self.statistics.total_folders += subfolder.statistics.total_folders
                self.statistics.unsynced_folders += (
                    subfolder.statistics.unsynced_folders
                )
                self.statistics.total_files += subfolder.statistics.total_files
                self.statistics.unsynced_files += subfolder.statistics.unsynced_files
            elif item.is_file():
                file = File(parent=self, path=item, name=item.name)
                self.files.append(file)
                self.statistics.total_files += 1
                if not file.synced:
                    self.statistics.unsynced_files += 1

    def toggle(self) -> None:
        self.collapsed = not self.collapsed

        if self.collapsed:
            for folder in self.folders:
                if not folder.collapsed:
                    folder.toggle()


class FileSystem(Folder):

    def __init__(self, path: Path) -> None:
        super().__init__(path=path, parent=None)
