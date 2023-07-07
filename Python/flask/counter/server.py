from flask import Flask
app = Flask(__name__)


if 'key_name' in session:
    print('key exists!')
else:
    print("key 'key_name' does NOT exist")

if __name__ == "__main__":
    app.run(debug=True, port=5001)