import os
import shutil
import send2trash

f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()

print("Current working directory:")
print(os.getcwd())

print("\nFiles and directories in current directory:")
print(os.listdir())

print("\nFiles and directories in the parent Python Bootcamp directory:")
base_dir = os.getenv('BASE_DIR', '/default/path/to/Python_Bootcamp')
print(os.listdir(os.path.join(base_dir)))

print("\nMoving 'practice.txt' to 'move_test' directory:")
move_test_dir = os.path.join(base_dir, 'Section14_Advanced_Python_Modules/os/move_test')
print(shutil.move('practice.txt', move_test_dir))

print("\nMoving 'practice.txt' back from 'move_test' directory to current directory:")
practice_file_path = os.path.join(move_test_dir, 'practice.txt')
print(shutil.move(practice_file_path, os.getcwd()))

send2trash.send2trash('practice.txt')

print("\n" + "="*50)
print("OS.WALK EXAMPLES")
print("="*50)

# Example 1: Basic os.walk usage
print("\nExample 1: Basic os.walk() usage")
print("-" * 30)

for root, dirs, files in os.walk('.'):
    print(f"Current directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print()

# Example 2: Find all Python files
print("\nExample 2: Finding all .py files")
print("-" * 30)

python_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            full_path = os.path.join(root, file)
            python_files.append(full_path)
            print(f"Python file: {full_path}")

print(f"Total Python files found: {len(python_files)}")

# Example 3: Count total files and directories
print("\nExample 3: Counting files and directories")
print("-" * 30)

total_files = 0
total_dirs = 0

for root, dirs, files in os.walk('.'):
    total_files += len(files)
    total_dirs += len(dirs)

print(f"Total files: {total_files}")
print(f"Total directories: {total_dirs}")
