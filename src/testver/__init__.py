"Temporarily change the version of a package for testing purposes."
import ast
import astunparse
from pathlib import Path

__version__ = "0.1.0"


def modver(filepath: Path, suffix: str = "test"):
    filepath = Path(filepath)
    tree = ast.parse(filepath.read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and (
            node.targets[0].id == "__version__"
        ):
            new_value = node.value.value + f"-{suffix}"
            node.value.value = node.value.value + f"-{suffix}"
            break
    else:
        raise ValueError(
            "The specified file doesn't have a variable called __version__."
        )
    return (astunparse.unparse(tree), new_value)
