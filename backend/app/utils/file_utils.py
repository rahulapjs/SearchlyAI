from fastapi import UploadFile
from pathlib import Path
import shutil

ALLOWED_EXTENSIONS = {".pdf", ".txt"}


def validate_file(file: UploadFile) -> None:
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError("Unsupported file type")


def save_upload_file(file: UploadFile, destination: Path) -> Path:
    """
    Saves uploaded file to disk.
    """
    destination.mkdir(parents=True, exist_ok=True)
    file_path = destination / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
