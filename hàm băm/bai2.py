from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)

# Trang HTML cho giao diện
html_template = """
<!doctype html>
<html lang="vi">
<head>
    <meta charset="utf-8">
    <title>Kiểm tra tính toàn vẹn tệp ảnh</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        input[type="file"],
        input[type="text"],
        input[type="submit"] {
            margin-top: 10px;
            padding: 10px;
            width: 100%;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #5cb85c;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #4cae4c;
        }
        p {
            font-size: 1.1em;
        }
    </style>
</head>
<body>
    <h1>Kiểm tra tính toàn vẹn của tệp ảnh</h1>
    <form method="post" enctype="multipart/form-data">
        <label for="file">Chọn tệp ảnh:</label>
        <input type="file" id="file" name="file" accept="image/*" required>
        
        <label for="saved_hash">Băm đã lưu:</label>
        <input type="text" id="saved_hash" name="saved_hash" required>
        
        <input type="submit" value="Kiểm tra">
    </form>

    {% if result is not none %}
    <h2>Kết quả:</h2>
    <p>{{ result }}</p>
    {% endif %}
</body>
</html>
"""

def calculate_hash(file):
    """Tính toán băm SHA-256 của tệp."""
    sha256_hash = hashlib.sha256()
    for byte_block in iter(lambda: file.read(4096), b""):
        sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['file']
        saved_hash = request.form['saved_hash']
        
        # Tính băm của tệp ảnh
        current_hash = calculate_hash(file.stream)
        
        if current_hash == saved_hash:
            result = "✅ Tệp ảnh không bị thay đổi."
        else:
            result = "⚠️ Tệp ảnh đã bị thay đổi."
    
    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)