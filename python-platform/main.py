import os
from dotenv import load_dotenv

load_dotenv()
# 환경 변수값
name = os.getenv("name")

print(name)