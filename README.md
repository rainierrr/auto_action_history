# auto_action_history
一週間の行動履歴の一部を自動で入力します
## 環境
- Ubuntu
- Chrome 78.0.3904.108
- ChromeDriver
- Python
- selenium
Python は Anacondaを使っています

## インストール
### selenium
```
conda install selenium
```
(pipでも可)
### ChromeDriver
[公式から](http://chromedriver.chromium.org/downloads)OSやchromeのバージョン（これをしっかりやらないと死ぬ）にあったものをダウンロード。zipファイルなどで解答してパスを通す。Ubuntuなどは/usr/local/binに移動でも大丈夫です。

##　実行方法
```
python main.py
```
をすると学生番号とパスワード、自動入力したい週の日曜日が聞かれるのでそれらを入力すると自動でやってくれる

## 参考
[Python + Selenium で Chrome の自動操作を一通り](https://qiita.com/memakura/items/20a02161fa7e18d8a693)