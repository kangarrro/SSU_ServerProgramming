-- interview_db 데이터베이스 생성 (이미 있으면 생략해도 됨)
CREATE DATABASE IF NOT EXISTS interview_db DEFAULT CHARACTER SET utf8mb4;

-- 해당 DB 사용
USE interview_db;

-- questions 테이블 생성
CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    answer TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);