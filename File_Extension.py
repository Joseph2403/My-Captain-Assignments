import pathlib

expansion = {
    '.py': 'python',
    '.cpp': 'c++',
    '.txt': 'text',
    '.c': 'c',
    '.ipynb': 'jupyter notebook',
    '.xlsx': 'excel'
}

filename = input("Enter file name: ")
file_extension = pathlib.Path(filename).suffix

print(f"The extension of the file is '{expansion.get(file_extension)}'")
