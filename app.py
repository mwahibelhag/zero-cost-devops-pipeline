from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # محاكاة قراءة بيانات من البيئة أو قاعدة البيانات
    db_host = os.environ.get('DB_HOST', 'Local_Dev_DB')
    return f"""
    <html>
        <head><title>DevOps Project</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1 style="color: #2c3e50;">🚀 نظام الأتمتة المالي الذكي يعمل بنجاح!</h1>
            <p style="font-size: 18px; color: #7f8c8d;">هذا التطبيق تم فحص أمانه ونشره تلقائياً بالكامل بدون أي تكلفة سحابية.</p>
            <div style="background: #ecf0f1; display: inline-block; padding: 10px 20px; border-radius: 5px;">
                <strong>حالة قاعدة البيانات:</strong> متصل بـ {db_host}
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)