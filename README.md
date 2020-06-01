## 害獣判定アプリ（イノシシ、カラス、猿のみ）
画像データからどの害獣か推定するFlaskを使った簡易アプリです。



### 各ファイルについて
- animal_cnn_aug.py
- gen_data_augmented.py
- predictapp.py
- animal_aug.npy
- animal_cnn_aug.h5


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
