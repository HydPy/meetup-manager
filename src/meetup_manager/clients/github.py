import logging
import os
from typing import List

from django.conf import settings
from django.core.cache import cache
from github import Github, GithubException
from github.Label import Label
from github.PaginatedList import PaginatedList

from .base import BaseIntegrationClient

ACCESS_TOKEN_KEY = "GITHUB_ACCESS_TOKEN"

logger = logging.getLogger(__name__)
TALK_PROPOSAL = "talk-proposal"


class GithubClient(BaseIntegrationClient):
    """
    Integration client for github interactions using Github V3 API through
    PyGithub (https://pygithub.readthedocs.io).
    """
    api_endpoint = "https://api.github.com"

    @staticmethod
    def access_token():
        """
        Return access token configured from cache. Set token to cache if not
        set previously.
        Access token should be configured through environment variables
        return: Github access token configured.
        """
        access_token = cache.get(
            ACCESS_TOKEN_KEY, default=os.getenv(ACCESS_TOKEN_KEY, "")
        )
        cache.set(ACCESS_TOKEN_KEY, access_token)
        return access_token

    def __init__(self):
        super(GithubClient, self).__init__()
        self.client = Github(GithubClient.access_token())

    def notify_speaker(self, issue_id: int, comment: str):
        """
        To notify speaker by commenting on the talk proposal issue.
        :param issue_id: Talk proposal Issue id
        :param comment: Notification content as raw string.
        """
        try:
            repo = self.client.get_repo(settings.CFP_REPO)
            issue = repo.get_issue(number=issue_id)
            issue.create_comment(body=comment)
            logger.info(f"Notified talk proposal issue {issue_id}")
        except GithubException as ex:
            logger.exception("An error occurred while adding notifying "
                             "speaker through github")
            raise

    def fetch_proposals(self) -> PaginatedList:
        """
        Fetch proposals (open issues in cfp repo).
        :return List of github issues as a list.
        """
        try:
            repo = self.client.get_repo(settings.CFP_REPO)
            return repo.get_issues()
        except GithubException as ex:
            logger.exception(f"An error occured while fetching proposals "
                             "with labels {labels}")
            raise

    def create_event(self, *args, **kwargs):
        pass

    def update_event(self, *args, **kwargs):
        pass

    def notify_attendees(self, *args, **kwargs):
        pass
