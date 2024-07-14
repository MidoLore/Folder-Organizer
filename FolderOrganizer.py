from pathlib import Path
import shutil

# Define the folder paths
downloads_folder = Path.home() / "Downloads"
documents_folder = Path.home() / "Documents"
pictures_folder = Path.home() / "Pictures"
music_folder = Path.home() / "Music"
videos_folder = Path.home() / "Videos"

# Define file type categories
document_types = {".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt"}
image_types = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"}
audio_types = {".mp3", ".wav", ".aac", ".flac"}
video_types = {".mp4", ".avi", ".mkv", ".mov", ".wmv"}
executable_types = {".exe", ".msi", ".bat", ".sh", ".app"}
compressed_types = {".zip", ".rar", ".7z", ".tar", ".gz"}

# Created a function to move files based on fyletype
def organizeFiles():
    # Looks through each file in the downloads folder
    for file in downloads_folder.iterdir():
        # Get the file type
        file_type = file.suffix.lower()
        
        # Move the file to specific folder based of filetype
        if file_type in document_types:
            destination_folder = documents_folder
        elif file_type in image_types:
            destination_folder = pictures_folder
        elif file_type in audio_types:
            destination_folder = music_folder
        elif file_type in video_types:
            destination_folder = videos_folder
        else:
            # Skip unknown file types
            continue
        
        # Move the file
        try:
            shutil.move(str(file), str(destination_folder))
            print(f"Moved: {file.name} to {destination_folder}")
        except Exception as e:
            print(f"Error moving file {file.name}: {e}")

def removeExecutable():
    for file in downloads_folder.iterdir():
        file_type = file.suffix.lower()
        if file_type in executable_types:
            file.unlink
            
organizeFiles()
removeExecutable()
