# 취업 면접 질문 공유 웹사이트 (프로젝트명 미정)

이 프로젝트는 취업 면접 준비를 위한 질문 & 답변을 공유하는 Flask 기반 웹 애플리케이션입니다.  

---

#  과제에서 충족해야 하는 필수 요소입니다. 

- Flask Framework, MySQL, Redirect, JSON 반드시 사용
- 신규 데이터 생성, 수정, 삭제, 전체 조회 기능 구현한 Web 화면 포함할 것
1. Create : 면접 질문 생성
2. Read : 현재까지 등록된 질문 조회
3. Update : 질문 수정, 답변 등록 / 수정
4. Delete : 질문, 답변 삭제

---

#  0. 필수 설치 요소

- Pycharm Professional (https://www.jetbrains.com/pycharm/download/?section=windows)
- MySQL (https://dev.mysql.com/downloads/installer/)
- Git (https://git-scm.com/downloads/win)

---

#  1. 프로젝트 실행 방법

1. 터미널에서 프로젝트를 클론합니다.

git clone https://github.com/rest-point/interview-app.git

cd interview-app

2. 터미널에서 가상환경 생성 및 패키지를 설치합니다. ( requirements.txt 에 PyMySQL, python-dotenv 등과 같은 패키지의 버전을 맞출 수 있도록 추가하였습니다.)

pip install -r requirements.txt

3. interview_html 폴더에 .env 파일 생성 후 하단 내용 기입 ( app.py 에 mysql 에서 설정한 root 의 비밀번호 등이 공유되지 않기 위해 생성하였습니다. .gitignore로 보호되어 있으니 각자 로컬에 직접 작성 부탁드립니다.)

.env

DB_HOST=localhost

DB_USER=root

DB_PASSWORD=본인의비밀번호

DB_NAME=interview_db

4. 터미널에서 MySQL DB 및 테이블 생성 ( setting.sql 에 DB 초기 세팅이 있습니다.)

mysql -u root -p < setting.sql (powershell 에서 동작하지 않을 수 있습니다. Command Prompt 사용을 권장합니다.)

