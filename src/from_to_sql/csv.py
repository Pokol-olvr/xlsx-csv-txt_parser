from pathlib import Path

path = Path("data/MOCK_DATA.csv")


with open(path) as file:
    contents = file.read()

print(contents)


