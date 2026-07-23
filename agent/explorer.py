from pathlib import Path

# explorer.py 所在位置
BASE_DIR = Path(__file__).resolve().parent.parent

WORKSPACE = BASE_DIR / "workspace"

def read_workspace_file(relative_path: str):

    # 去掉前面的 workspace/（如果有的話）
    if relative_path.startswith("workspace/"):
        relative_path = relative_path[len("workspace/"):]

    file = WORKSPACE / relative_path

    return file.read_text(encoding="utf-8")

def list_files():
    files = []

    for file in WORKSPACE.rglob("*"):
        if file.is_file():
            files.append(file)

    return files


def read_file(path):
    return Path(path).read_text(encoding="utf-8")