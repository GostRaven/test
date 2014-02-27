import os

for root, dirs, files in os.walk("/"):
    for f in files:
        print(root)
