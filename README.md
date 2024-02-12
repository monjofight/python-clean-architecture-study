# Python Clean Architecture Example

このプロジェクトは、Pythonでクリーンアーキテクチャを実装する方法を学習する為に作成したアプリケーションです。FastAPIを使用してRESTful APIを提供し、MySQLをデータストアとして使用します。アプリケーションは、ユーザーのサインアップ、ログイン、およびユーザー情報の取得のエンドポイントを提供します。

## 機能

- ユーザー登録
- ログインとJWTによる認証
- 認証済みユーザー情報の取得

## 技術スタック

- FastAPI
- SQLAlchemy
- Alembic
- PyMySQL
- PyJWT
- Docker

## プロジェクト構成

- `app/`: アプリケーションのソースコードを含むディレクトリ
  - `adapters/`: リクエストとレスポンスのアダプター
  - `application/`: ユースケースとインターフェイス
  - `domain/`: エンティティとドメインロジック
  - `infrastructure/`: データベースモデル、リポジトリ、外部サービスの統合
  - `utilities/`: 汎用的なユーティリティ関数
- `Dockerfile`と`docker-compose.yml`: Dockerを使用したアプリケーションのコンテナ化と実行

## 環境設定

`.env.example`ファイルを`.env`にコピーし、適切な値で設定します。

```bash
cp app/.env.example app/.env
```

設定は以下の通りです:

- データベース接続設定
- JWTの署名キー

## インストール方法

DockerとDocker Composeが必要です。

1. リポジトリをクローンします。

2. `.env`ファイルを設定します。（上記参照）

3. Dockerコンテナをビルドして起動します。

```bash
docker-compose up --build
```

## APIの使用方法

アプリケーションが起動したら、`http://localhost:8000/docs`にアクセスしてSwagger UIを介してAPIを探索できます。

- `/signup/`: ユーザーを新規登録します。
- `/login/`: 登録済みのユーザーでログインし、JWTトークンを取得します。
- `/me/`: JWTトークンを使用して認証済みユーザーの情報を取得します。

## 開発者向け情報

- テストの実行、DBマイグレーションなどの開発に関する詳細は、`Makefile`を参照してください。
- コード変更後は、Dockerコンテナを再ビルドする必要があります。
