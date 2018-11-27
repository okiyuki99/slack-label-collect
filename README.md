# slack-label-collect
Collect anomaly label data through posting interective message in slack

## Image 

![image][doc/image.png]

## How to deploy

1. slack appでapplicationを作成 (例 : AnomalyLabeller)
    - `Interecive Components`で ボタンをクリックしたらPOSTメソッドをうける`Request URL`を設定（例：https://test.herokuapp.com）
    - `OAuth & Permissions`の`scope`にSend系のスコープを追加しておく
    - `Install App`で設定したいSlackのワークスペースにインストール 

1. `main.py`をWebサーバにデプロイする

    デプロイ先がherokuの場合
    1. `$ git init & git remote add heroku https://git.heroku.com/~~.git` にherokuのプロジェクトを追加
    1. `$ heroku config:set SLACK_BOT_TOKEN=[OAuth TOKEN] SLACK_VERTIFICATION_TOKEN=[VERTIFICATION TOKEN] --app ~~`でSlackの認証に関する環境変数を設定
    1. `$ git add Procfile app.py requirements.txt & git commit -m "~" & git push heroku master` でデプロイ完了
