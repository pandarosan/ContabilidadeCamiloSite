import re

with open("manual-pandarosan.html", "r", encoding="utf-8") as f:
    content = f.read()

print("Date check:", "Setembro / 2026" in content)
print("Justify check:", "text-align: justify" in content)
