from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext  # 패스워드 암호화를 위한 패키지
from models import User
from schemas import UserCreate
from database import SessionLocal

router = APIRouter()

# 비밀번호 암호화 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 의존성: 데이터베이스 세션 생성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 비밀번호 해시화 함수
def hash_password(password: str):
    return pwd_context.hash(password)


@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # ID 중복 체크
    existing_user = db.query(User).filter(User.id == user.id).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="ID already exists")

    # 비밀번호 암호화
    hashed_password = hash_password(user.password)

    # 새로운 사용자 생성
    new_user = User(id=user.id, name=user.name, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user  # 등록된 사용자 정보 반환
