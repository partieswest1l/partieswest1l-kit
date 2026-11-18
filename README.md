# partieswest1l-kit

Sort a folder of files into per-type subfolders.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m partieswest1l_kit.cli --help
```

```python
from partieswest1l_kit.core import Partieswest1lTool

tool = Partieswest1lTool()
print(tool)
```

## Layout

```
partieswest1l_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 partieswest1l
