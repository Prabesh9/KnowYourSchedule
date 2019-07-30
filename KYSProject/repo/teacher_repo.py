import traceback

from django.db import connection

from KnowYourSchedule.model.Teacher import Teacher


class TeacherRepo(object):

    def signin(self, email):
        query = "SELECT teacher_id, first_name, email, password FROM teacher WHERE email = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [email])
                row = cursor.fetchone()
                if row is None:
                    return None
                else:
                    teacher = Teacher()
                    teacher.teacher_id = row[0]
                    teacher.full_name = row[1]
                    teacher.email = row[3]
                    return {"user": teacher, "password": row[4]}
        except Exception:
            traceback.print_exc()
            return None