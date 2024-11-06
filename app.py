from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
bcrypt = Bcrypt(app)
CORS(app)

# Giả lập cơ sở dữ liệu trong bộ nhớ
users = {}

# Route cho trang đăng nhập (trả về giao diện login.html)
@app.route('/')
def index():
    return render_template('login.html')

# Route cho trang đăng ký (trả về giao diện register.html)
@app.route('/register')
def register_page():
    return render_template('register.html')

# API xử lý đăng ký
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Kiểm tra nếu email đã tồn tại
    if email in users:
        return jsonify({"message": "Email đã tồn tại!"}), 400

    # Mã hóa mật khẩu và lưu người dùng mới vào "cơ sở dữ liệu"
    users[email] = bcrypt.generate_password_hash(password).decode('utf-8')
    return jsonify({"message": "Đăng ký thành công!"}), 201

# API xử lý đăng nhập
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Kiểm tra email và mật khẩu
    if email in users and bcrypt.check_password_hash(users[email], password):
        session['user'] = email
        return jsonify({"message": "Đăng nhập thành công!"}), 200
    else:
        return jsonify({"message": "Sai email hoặc mật khẩu!"}), 401

# Route cho trang profile sau khi đăng nhập thành công
@app.route('/profile')
def profile():
    if 'user' in session:
        return f"Xin chào, {session['user']}!"
    return redirect(url_for('index'))

# Route đăng xuất
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
