from flask import Flask, render_template, request, redirect, url_for, jsonify
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드
app = Flask(__name__)

# MySQL 연결 설정
conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_NAME"),
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
# .env 파일 불러오기 (환경변수에서 DB 정보 가져옴)
load_dotenv()

# Flask 앱 생성
app = Flask(__name__)

# MySQL 연결 설정 (환경변수 사용)
conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_NAME"),
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor  # 결과를 딕셔너리 형태로 반환
)

# 홈 페이지 - 전체 질문 목록 보기
@app.route('/')
def index():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM questions ORDER BY id DESC")
        questions = cursor.fetchall()  # 모든 질문 가져오기
    return render_template('index.html', questions=questions)

# 질문 상세 페이지
@app.route('/question/<int:question_id>')
def detail(question_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM questions WHERE id = %s", (question_id,))
        question = cursor.fetchone()  # 하나의 질문만 가져오기
    return render_template('detail.html', question=question)

# 질문 등록 페이지 (폼 표시 및 POST 처리)
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        title = request.form['title']
        answer = request.form['answer']
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO questions (title, answer) VALUES (%s, %s)", (title, answer))
            conn.commit()
        return redirect(url_for('index'))  # 등록 후 홈으로 이동
    return render_template('form.html')  # GET 요청 시 폼 페이지 보여줌

# 질문 삭제 기능 (POST 방식)
@app.route('/delete/<int:question_id>', methods=['POST'])
def delete(question_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM questions WHERE id = %s", (question_id,))
        conn.commit()
    return redirect(url_for('index'))

# JSON API로 질문 목록 반환
@app.route('/api/questions')
def api_questions():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM questions ORDER BY id DESC")
        questions = cursor.fetchall()
    return jsonify(questions)  # JSON 형태로 반환

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)



