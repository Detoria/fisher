from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8080) ## threaded 开启多线程模式，process开启多进程模式
    # 单进程、单线程
