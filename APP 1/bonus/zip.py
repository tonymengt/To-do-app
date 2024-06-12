import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname = filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=['APP 1/bonus/bonus1.py', 'APP 1/bonus/bonus2.py'], dest_dir='APP 1/bonus/dest')