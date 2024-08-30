import os

def cleanup_png_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".png"):
            file_path = os.path.join(folder, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")