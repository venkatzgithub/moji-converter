# moji-converter
# Convert hiragana to katakana and vice versa

## Installation
```
pip install mojiconverter==0.0.1
```

## Import

```python
from mojiconverter.app import katakana,hiragana

# or

from mojiconverter import app as convert

```

## usage
```python
from mojiconverter import app as convert

convert.katakana("こんにちは")
# output: "コンニチハ"

convert.hiragana("コンニチハ")
# output: "こんにちは"



### contributor: https://github.com/venkatzgithub