from KnowYourSchedule.repo import teacher_repo
from service.service import Service
from utils import generate_uuid, timestamp, password_hash, password_verify
import traceback


class AccountService(Service):

    def signin(self, email, password):
        try:
            use_repo = teacher_repo()
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
