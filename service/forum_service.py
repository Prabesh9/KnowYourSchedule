from repo.forum_repo import ForumRepo
from service.service import Service
from utils import generate_uuid, timestamp
import traceback


class ForumService(Service):

    def get_all_forums(self):
        try:
            forum_repo = ForumRepo()
            return forum_repo.fetch_forums()
        except Exception as e:
            traceback.print_exc()
            return None

    def delete(self, forum_id):
        try:
            forum_repo = ForumRepo()
            return forum_repo.delete(forum_id)
        except Exception as e:
            traceback.print_exc()
            return False

    def save(self, forum):
        forum.forum_id = generate_uuid()
        forum.created_at = timestamp()
        try:
            forum_repo = ForumRepo()
            if forum_repo.save(forum):
                return forum
        except Exception as e:
            traceback.print_exc()
            return None
