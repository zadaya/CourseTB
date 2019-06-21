# 环境变量
运行前设置以下环境变量：
- export FLASK_APP=run.py

开发模式设置以下环境变量：
-  export FLASK_ENV=development
-  export FLASK_CONFIG=development

产品模式设置以下变量
-  export FLASK_ENV=production
-  export FLASK_CONFIG=production

# 数据库设置
1. flask db init
2. flask db migrate
3. flask db upgrade