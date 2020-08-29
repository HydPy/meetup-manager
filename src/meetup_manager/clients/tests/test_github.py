from unittest import TestCase, mock

from github.GithubException import GithubException

from ..github import GithubClient


def github_exception_side_effect(status=404, data="Exception raised"):
    mock_func = mock.Mock()
    mock_func.side_effect = GithubException(status=status, data=data)
    return mock_func


class TestGithubClient(TestCase):
    def setUp(self) -> None:
        self.api_client = GithubClient()

    @mock.patch("github.Github.get_repo")
    @mock.patch("github.Repository.Repository.get_issue")
    @mock.patch("github.Issue.Issue.create_comment")
    def test_notify_speaker_ok(self, create_comment, get_issue, get_repo):
        create_comment.return_value = mock.Mock()
        get_issue.return_value = mock.Mock()
        get_repo.return_value = mock.Mock()
        try:
            self.api_client.notify_speaker(issue_id=123, comment="A comment")
        except GithubException as ex:
            self.fail(f"Raised unexpected exception : {ex}")

    @mock.patch("github.Github.get_repo",
                side_effect=github_exception_side_effect())
    @mock.patch("github.Repository.Repository.get_issue")
    @mock.patch("github.Issue.Issue.create_comment")
    def test_notify_speaker_ko(self, create_comment, get_issue, get_repo):
        get_issue.return_value = mock.Mock()
        get_repo.return_value = mock.Mock()
        with self.assertRaises(GithubException) as e:
            self.api_client.notify_speaker(issue_id=123, comment="A comment")
            self.assertEqual(e.exception.status, 404)

    @mock.patch("github.Github.get_repo")
    @mock.patch("github.Repository.Repository.get_issues")
    def test_fetch_proposals_ok(self, get_issues, get_repo):
        get_issues.return_value = mock.Mock()
        get_repo.return_value = mock.Mock()
        try:
            self.api_client.fetch_proposals()
        except GithubException as ex:
            self.fail(f"Raised unexpected exception : {ex}")

    @mock.patch("github.Github.get_repo",
                side_effect=github_exception_side_effect())
    @mock.patch("github.Repository.Repository.get_issues")
    def test_fetch_proposals_ko(self, get_issues, get_repo):
        get_issues.return_value = mock.Mock()
        get_repo.return_value = mock.Mock()
        with self.assertRaises(GithubException) as e:
            self.api_client.fetch_proposals()
            self.assertEqual(e.exception.status, 404)
