### メモ
pytestのインポート
- そのままpytestを実行するとライブラリ周りのエラーが出る
    - `pytest` これがダメ
- 以下のコマンドで実行すると、sys.pathがカレントディレクトリを追加して実行してくれるため、エラーが出ない
    - `python -m pytest`