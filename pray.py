import PyPDF2
from pathlib import Path
path = Path('Badget cycles.pdf').read_text()
import os

print(path.exists())
