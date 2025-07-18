# Perspective API Text Analyzer

テキストの毒性を分析するWebアプリケーション

## セットアップ手順

1. リポジトリをクローン
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Python仮想環境を作成してアクティベート
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3. 必要なパッケージをインストール
```bash
pip install -r requirements.txt
```

4. 環境変数の設定
- `.env.example`ファイルを`.env`にコピー
- `.env`ファイルを開き、必要な環境変数を設定
  - `PERSPECTIVE_API_KEY`: Google Perspective APIのAPIキー

5. アプリケーションの起動
```bash
python app.py
```

## 注意事項
- `.env`ファイルには機密情報が含まれるため、絶対にGitにコミットしないでください
- 必要な環境変数の設定については`.env.example`を参照してください 