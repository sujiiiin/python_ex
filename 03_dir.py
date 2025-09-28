import os

for dirpath, dirnames, filenames in os.walk(r"C:\python_ex"):
  print(f"found current dir : {dirpath}")
  print(f"Subdir : {dirnames}")
  print(f"filename : {filenames}")