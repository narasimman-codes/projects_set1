import os
import shutil

def move_matching_files(input_dir, output_dir, prefix_list):
    # Safety check
    if not os.path.exists(input_dir):
        print(f"Input directory does not exist: {input_dir}")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Normalize prefixes for case-insensitive match
    prefix_set = {prefix.lower() for prefix in prefix_list}

    moved_files = 0

    for filename in os.listdir(input_dir):
        if len(filename) < 7:
            continue  # skip invalid names

        file_prefix = filename[:7].lower()
        if file_prefix in prefix_set:
            src_path = os.path.join(input_dir, filename)
            dest_path = os.path.join(output_dir, filename)

            # Handle collisions
            if os.path.exists(dest_path):
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(output_dir, f"{base}_{counter}{ext}")
                    counter += 1

            shutil.move(src_path, dest_path)
            moved_files += 1

    print(f"✅ Moved {moved_files} file(s) to {output_dir}")

# === USAGE EXAMPLE ===
if __name__ == "__main__":
    input_directory = input("Enter input directory path: ").strip()
    output_directory = input("Enter output directory path: ").strip()
    
    print("Enter 7-character prefixes (comma-separated):")
    prefix_input = input().strip()
    prefixes = [p.strip() for p in prefix_input.split(",") if len(p.strip()) == 7]

    move_matching_files(input_directory, output_directory, prefixes)
