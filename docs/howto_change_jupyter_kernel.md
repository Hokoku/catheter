# How to change jupyter kernel

1. 左下のボタンからinterpreterを変える
1. jupyter notebookを開いた画面で、右上のボタンからkernelを変える
1. VScodeを再起動する (kernelの再起動では不十分)
1. 以上

上は誤り。

```
import sys
from pprint import pprint
pprint(sys.path)
```

これでパスを確認すると、どの環境が用いられているかわかる。
