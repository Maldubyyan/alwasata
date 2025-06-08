from flask import Flask
import os


application = Flask(__name__)


@application.route('/')
def hello():
    return (
        '<h1>مرحباً بك في منصة الواسطة!</h1>'
        '<p>تم تشغيل التطبيق بنجاح على AWS Elastic Beanstalk.</p>'
    )


# هذا هو النقطة الرئيسية للتطبيق
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    application.run(host='0.0.0.0', port=port)
