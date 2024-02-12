# Docker Composeコマンドのショートカット
DC = docker-compose

# .PHONY宣言: Makeがファイル名として解釈しないターゲット名を指定
.PHONY: build up down restart logs ps migrate-generate migrate-up migrate-down

# コンテナをビルドする
build:
	$(DC) build

# コンテナをバックグラウンドで起動する
up:
	$(DC) up -d

# コンテナを停止し、コンテナとネットワークを削除する
down:
	$(DC) down

# コンテナを再起動する
restart:
	$(DC) down
	$(DC) up -d

# コンテナのログを表示する
logs:
	$(DC) logs

# 現在起動しているコンテナの一覧を表示する
ps:
	$(DC) ps

# Alembicを使用して新しいマイグレーションを生成する
# 使用例: make migrate-generate message="add new table"
migrate-generate:
	$(DC) exec web sh -c "cd app && alembic revision --autogenerate -m \"$(message)\""

# Alembicを使用して最新のマイグレーションにアップグレードする
migrate-up:
	$(DC) exec web sh -c "cd app && alembic upgrade head"

# Alembicを使用してすべてのマイグレーションをロールバックする
migrate-down:
	$(DC) exec web sh -c "cd app && alembic downgrade base"