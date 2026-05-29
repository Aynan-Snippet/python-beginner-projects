import os
import shutil

# Define file type categories
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff'}
VIDEO_EXTENSIONS = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.mpeg'}
TEXT_EXTENSIONS  = {'.txt', '.pdf', '.docx', '.doc', '.csv', '.xlsx', '.pptx', '.odt'}

def sort_files(folder_path):
    # Check if folder exists
    if not os.path.exists(folder_path):
        print("❌ Folder not found. Please check the path.")
        return

    # Create output folders
    images_folder = os.path.join(folder_path, "Images")
    videos_folder = os.path.join(folder_path, "Videos")
    texts_folder  = os.path.join(folder_path, "Text_Files")

    os.makedirs(images_folder, exist_ok=True)
    os.makedirs(videos_folder, exist_ok=True)
    os.makedirs(texts_folder,  exist_ok=True)

    # Counters
    image_count = 0
    video_count = 0
    text_count  = 0
    other_count = 0

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders (including our newly created ones)
        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(filename)[1].lower()

        if ext in IMAGE_EXTENSIONS:
            shutil.move(file_path, os.path.join(images_folder, filename))
            image_count += 1

        elif ext in VIDEO_EXTENSIONS:
            shutil.move(file_path, os.path.join(videos_folder, filename))
            video_count += 1

        elif ext in TEXT_EXTENSIONS:
            shutil.move(file_path, os.path.join(texts_folder, filename))
            text_count += 1

        else:
            other_count += 1  # File stays in original folder

    # Print summary
    print("\n✅ Files sorted successfully!")
    print(f"📄 Text Files : {text_count}")
    print(f"🖼️  Images     : {image_count}")
    print(f"🎬 Videos     : {video_count}")
    print(f"❓ Others     : {other_count} (not moved)")


# ── Main ──────────────────────────────────────────────
folder = input("Enter the folder path: ").strip()
sort_files(folder)