import os
import glob

def check_files():
    target_dir = os.path.abspath("captured_xmls")
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        return

    files = glob.glob(os.path.join(target_dir, "*.xml"))
    print(f"Found {len(files)} files in {target_dir}:")
    for f in files:
        print(os.path.basename(f))
        
if __name__ == "__main__":
    check_files()
