from config import run

app = run()

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
