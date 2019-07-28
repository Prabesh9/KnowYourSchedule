from django.db import connection
import traceback

from model.forum import Forum
from model.user import User
from utils import to_date


class ForumRepo(object):


    def fetch_forums(self):
        query = "SELECT f.forum_id, f.title, f.tag, f.body, f.created_at, u.user_id, u.full_name, f.forum_image FROM forum as f INNER JOIN user as u ON f.user_id = u.user_id order by f.created_at DESC"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows is None:
                    return None
                else:
                    forums = list()
                    for row in rows:
                        forum = Forum()
                        forum.forum_id = row[0]
                        forum.title = row[1]
                        forum.tag = row[2]
                        forum.body = row[3]
                        forum.created_at = row[4]
                        forum.created_date = to_date(row[4])
                        user = User()
                        user.user_id = row[5]
                        user.full_name = row[6]
                        forum.forum_image = row[7]
                        forum.user = user
                        forums.append(forum)
                    return forums
        except Exception as e:
            traceback.print_exc()
            return None

    def delete(self, forum_id):
        query = "DELETE FROM forum WHERE forum_id = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [forum_id])
                return True
        except Exception as e:
            traceback.print_exc()
            return False

    def save(self, forum):
        query = "INSERT INTO forum(forum_id, title, tag, body, user_id, created_at, forum_image) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [forum.forum_id, forum.title, forum.tag, forum.body, forum.user.user_id, forum.created_at, forum.forum_image])
                return True
        except Exception as e:
            traceback.print_exc()
            return False