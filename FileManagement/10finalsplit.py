import os
import shutil

def move_invalid_length_files(source_root, mirror_root):
    if not os.path.exists(source_root):
        print("Source path does not exist.")
        return

    os.makedirs(mirror_root, exist_ok=True)

    for folder_name in os.listdir(source_root):
        folder_path = os.path.join(source_root, folder_name)
        if not os.path.isdir(folder_path):
            continue

        native_path = os.path.join(folder_path, "Native Files")
        if not os.path.exists(native_path):
            continue

        files_to_move = []

        # Collect files with name length not equal to 10
        for root, _, files in os.walk(native_path):
            for file in files:
                name_without_ext = os.path.splitext(file)[0]
                if len(name_without_ext) != 10:
                    files_to_move.append(os.path.join(root, file))

        # Only create the mirror folder if we have files to move
        if files_to_move:
            mirror_native_path = os.path.join(mirror_root, folder_name, "Native Files")
            os.makedirs(mirror_native_path, exist_ok=True)

            for src_file in files_to_move:
                file = os.path.basename(src_file)
                dst_file = os.path.join(mirror_native_path, file)

                # Handle duplicates in mirror folder
                if os.path.exists(dst_file):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while True:
                        dst_file = os.path.join(mirror_native_path, f"{base}_{counter}{ext}")
                        if not os.path.exists(dst_file):
                            break
                        counter += 1

                shutil.move(src_file, dst_file)
                print(f"Moved: {src_file} → {dst_file}")

    print("\n✅ Operation complete: Only invalid files moved, and empty folders avoided.")

if __name__ == "__main__":
    source = input("Enter the source folder path: ").strip()
    mirror = input("Enter the mirror folder path (will be created if it doesn't exist): ").strip()
    move_invalid_length_files(source, mirror)
