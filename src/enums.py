from enum import Enum
from typing import Optional


class SubjectBoxKeys(Enum):
    SUBJECT = 'subject'
    TEACHER = 'teacher'
    AVERAGE_MARK = 'average_mark'
    BC_1 = 'BC_1'
    BC_2 = 'BC_2'
    RATING = 'rating'
    EXAM = 'exam'
    COURSEWORK: Optional[str] = 'coursework'


class UserDataKeys(Enum):
    LOGIN = 'login'
    PASSWORD = 'password'
    PERIOD = 'period'
