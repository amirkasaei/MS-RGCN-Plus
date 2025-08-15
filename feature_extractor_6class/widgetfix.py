import nbformat as nbf

path = "/home/user01/MS-RGCN-Plus/feature_extractor_6class/ResNet.ipynb"  # <- change if needed
nb = nbf.read(path, as_version=4)

if "widgets" in nb.metadata:
    del nb.metadata["widgets"]  # remove ONLY the broken widget metadata

nbf.write(nb, path)
print("Cleaned metadata.widgets and kept all outputs:", path)
