import os

files_to_export = []

def filter_conveter_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            # get only files for converter step
            if "_tot_all_features_mets.npz" in file or "_features_mets.npz" in file:
                files_to_export.append((root, file))

    files_to_export_ordered = sorted(files_to_export)

    return files_to_export_ordered


files = filter_conveter_files("/mnt/nvme1n2/git/uniovi-simur-wearablepermed-data/input")

print(files)