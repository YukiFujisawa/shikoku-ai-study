# AI技術の活用

## 環境準備

```
## 開始時
$ . "/Users/yuki/tensorflow_macos_venv/bin/activate"

## 終了時
$ deactivate
```

## メモ

### このチュートリアルを学習した

https://colab.research.google.com/github/tensorflow/docs-l10n/blob/master/site/ja/tutorials/keras/classification.ipynb?hl=ja#scrollTo=hQlnbqaw2Qu_

https://www.tensorflow.org/tutorials/quickstart/beginner

### イテラブルオブジェクト

繰り返し処理が可能であるような性質をもつことを “iterable”、すなわち「反復可能である」と言う。これが「イテラブル（iterable）」の意味である。つまり「イテラブルオブジェクト」とは、for文などで要素を1つずつ取り出して処理できるような（通常、複数の要素からなる）オブジェクトを指す用語である。

### enumerate

enumerate関数を使うと、要素のインデックスと要素を同時に取り出す事が出来ます。