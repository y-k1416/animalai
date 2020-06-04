## 害獣判定アプリ（イノシシ、カラス、猿のみ）
画像データからどの害獣か推定するFlaskを使った簡易アプリです。
<br>

### 各ファイルについて
- animal_cnn_aug.py: 
単純な畳み込みのtrainファイル
- gen_data_augmented.py: 
データの水増し用のファイル
- predictapp.py: 
Flaskで作成した簡易推定アプリケーション
- animal_aug.npy: 
学習に利用した水増しずみの画像データ
- animal_cnn_aug.h5: 
学習ずみのh5ファイル


※今回学習に使う画像データは掲載していませんので、悪しからず。ちなみに学習用の画像データはFlickrAPIを利用し収集しました。


### 使い方
    # MAC
    export FLASK_APP = predictapp.py
    python -m flask run
    
    # WINDOWS
    set FLASK_APP = predictapp.py
    python -m flask run
    
    
    # flask起動後表示されたURLへ飛ぶ
    
画像選択でカラスorイノシシor猿の画像ファイル選択→推定ボタン
推定結果が画面切り替わり表示されます

### 使ったライブラリ
    pip install tensorflow #2.2.0
    pip install pillow
    pip install flask
    pip install sklearn
