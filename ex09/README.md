# ft_package

A sample test package providing `count_in_list(items, value)`.

Build the distributions from this directory:

```sh
python -m pip install build
python -m build
```

Install either distribution:

```sh
pip install ./dist/ft_package-0.0.1.tar.gz
```

```sh
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Use the installed package:

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```

Inspect the installation with `pip list` and `pip show -v ft_package`.
