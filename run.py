# """
# 整个系统入口文件
# """

from app import create_app

app = create_app("development")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10200)
