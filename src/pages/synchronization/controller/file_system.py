from src.pages.synchronization.model.files import Folder


def toggle_folder(folder: Folder) -> None:
    folder.toggle()
