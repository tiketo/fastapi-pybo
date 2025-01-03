import datetime

from pydantic import BaseModel, field_validator

from domain.answer.answer_schema import Answer
from domain.user.user_schema import User
from dataclasses import field

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = field(default_factory=list)
    user: User | None
    modify_date: datetime.datetime | None = None
    voter: list[User] = field(default_factory=list)

#    구버전 pydantic V1 사용 시 설정 옵션
#    class Config:
#        orm_mode = True

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = field(default_factory=list)

class QuestionUpdate(QuestionCreate):
    question_id: int

class QuestionDelete(BaseModel):
    question_id: int

class QuestionVote(BaseModel):
    question_id: int

