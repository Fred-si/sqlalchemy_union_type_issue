# SQLAchemy Mapped typing issue on union
Reproduce the issue

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mypy --install-types --non-interactive main.py
```
You see
```
main.py:21: error: Argument 1 to "foo" has incompatible type "str"; expected "InstrumentedAttribute[Any]"  [arg-type]
``` 
