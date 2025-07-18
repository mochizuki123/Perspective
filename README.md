# テキスト毒性分析アプリケーション

![Perspective API](https://www.gstatic.com/cloud/images/products/logos/perspective.png)

## 📝 プロジェクト概要

このプロジェクトは、Google Cloud の Perspective API を活用して、テキストの毒性（有害性）を分析するWebアプリケーションです。
入力されたテキストに対して、以下の観点から分析を行い、スコアを0-1の範囲で提供します：

- 毒性 (TOXICITY)
- 重度の毒性 (SEVERE_TOXICITY)
- アイデンティティ攻撃 (IDENTITY_ATTACK)
- 侮辱 (INSULT)
- 冒涜 (PROFANITY)
- 脅威 (THREAT)

## 🌟 主な機能

- テキスト入力フォームによる簡単な分析
- リアルタイムでの分析結果表示
- 6つの異なる評価基準による詳細な分析
- 直感的なユーザーインターフェース
- APIレスポンスの詳細表示

## 🛠 技術スタック

- **フロントエンド**
  - HTML/CSS
  - JavaScript
  - Bootstrap 5

- **バックエンド**
  - Python 3.8+
  - Flask
  - Google Cloud Perspective API

## 💻 使用方法

1. テキスト入力欄に分析したいテキストを入力
2. 「分析」ボタンをクリック
3. 各評価基準のスコアが表示されます
   - スコアは0-1の範囲で表示
   - 1に近いほど、その特性が強く検出されたことを示します

## 🔧 ローカルでの実行方法

1. 必要な環境の準備
   - Python 3.8以上
   - pip（Pythonパッケージマネージャー）

2. リポジトリのクローン
   ```bash
   git clone [your-repository-url]
   cd [repository-name]
   ```

3. 仮想環境の作成と有効化
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

4. 依存パッケージのインストール
   ```bash
   pip install -r requirements.txt
   ```

5. 環境変数の設定
   - `.env.example` を `.env` にコピー
   - Perspective API キーを取得（[Google Cloud Console](https://console.cloud.google.com/)）
   - `.env` ファイルにAPIキーを設定

6. アプリケーションの起動
   ```bash
   python app.py
   ```

7. ブラウザでアクセス
   ```
   http://localhost:5000
   ```

## 📊 分析スコアの解釈

各評価基準のスコアは以下のように解釈できます：

- **0.0-0.3**: 低リスク
- **0.3-0.7**: 中程度のリスク
- **0.7-1.0**: 高リスク

## ⚠️ 注意事項

- このアプリケーションは実験的な目的で作成されています
- 分析結果は参考値として扱ってください
- APIの利用制限にご注意ください
- センシティブな個人情報は入力しないでください

## 🔒 プライバシーとセキュリティ

- 入力されたテキストはPerspective APIに送信されます
- テキストデータはサーバー上に保存されません
- APIキーは適切に管理し、公開しないようご注意ください


## 🔗 参考リンク

- [Perspective API Documentation](https://developers.perspectiveapi.com/s/docs)
- [Google Cloud Console](https://console.cloud.google.com/)
- [Flask Documentation](https://flask.palletsprojects.com/) 
