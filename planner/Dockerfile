# 기본 이미지 저장
FROM python:3.10 

# 작업 디렉토리
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt /app/requiremnts.txt

# 패키지 설치
RUN pip install --upgrade pip && pip install -r /app/requiremnts.txt

# 포트 번호 설정
EXPOSE 8000

# 나머지 전체 파일 작업 디렉터리로 복사
COPY ./ /app

# 애플리케이션 실행
CMD ["python", "main.py"]