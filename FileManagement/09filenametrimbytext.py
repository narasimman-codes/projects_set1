import os
import re

def get_unique_filename(directory, base_name, extension):
    """Append a number to the filename if a collision occurs."""
    counter = 1
    new_filename = f"{base_name}{extension}"
    new_path = os.path.join(directory, new_filename)

    while os.path.exists(new_path):
        new_filename = f"{base_name}_{counter}{extension}"
        new_path = os.path.join(directory, new_filename)
        counter += 1

    return new_filename

def trim_substring_from_filenames(directory, substring_to_trim):
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)

            # Case-insensitive removal
            pattern = re.compile(re.escape(substring_to_trim), re.IGNORECASE)
            cleaned_name = pattern.sub('', name)

            if cleaned_name != name:
                new_filename = get_unique_filename(directory, cleaned_name, ext)
                new_path = os.path.join(directory, new_filename)

                try:
                    os.rename(old_path, new_path)
                    print(f"✅ Renamed: {filename} → {new_filename}")
                except Exception as e:
                    print(f"❌ Failed to rename {filename}: {e}")

if __name__ == "__main__":
    input_dir = input("Enter the full path of the directory: ").strip('"')
    substring = input("Enter the substring to remove from filenames (case-insensitive): ").strip()

    if not os.path.isdir(input_dir):
        print("❌ Invalid directory path. Check again.")
    elif not substring:
        print("❌ No substring entered. Nothing to trim.")
    else:
        trim_substring_from_filenames(input_dir, substring)
        print("\n🎉 Done! All filenames are trimmed and collision-free.")
