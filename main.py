from sys import path

with open("brands.txt", "r") as f:
    brands = f.read()
brands = brands.split("\n")
print(brands)
with open("run.py", "r") as f:
        code = f.read()
for brand in brands:
    #print(brand)
    path.append(f"{brand}/")
    code = f"path.append('{brand}/')\nimport {brand}\n{code}"
with open("run.py", "w") as f:
        f.write(code)