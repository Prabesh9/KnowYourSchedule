import traceback

from KYSProject.service.service import Service
from KYSProject.repo.teacher_repo import TeacherRepo


class AccountService(Service):

    def signin(self, email, password):
        try:
            use_repo = TeacherRepo()
            user_detail = use_repo.signin(email)
            if user_detail is None:
                return None
            else:
                if password_verify(password, user_detail["password"]):
                    return user_detail["user"]
                else:
                    return None
        except Exception:
            traceback.print_exc()
            return None
