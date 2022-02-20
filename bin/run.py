from pathlib import Path
import os
import sys

path = Path(os.path.realpath(__file__)).parent.parent.absolute()
sys.path.append(str(path))
from src.app.main import app

if __name__ == '__main__':
    app.run(debug=True, port=8080)
