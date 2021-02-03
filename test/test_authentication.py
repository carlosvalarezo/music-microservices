from os import environ
import unittest
from unittest import mock
from unittest.mock import call

from src.app import SpotifyToken


class TestSpotifyAuthentication(unittest.TestCase):

    @mock.patch.dict(environ, {"CLIENT_ID": "MY_CLIENT_ID"}, {"CLIENT_SECRET": "MY_CLIENT_SECRET"})
    @mock.patch('src.app.os')
    def test_checks_if_os_get_environ_was_called_twice_with_different_arguments(self, mock_os):
        calls = [call("CLIENT_ID"), call("CLIENT_SECRET")]
        token = SpotifyToken()

        token.get_spotify_token()

        mock_os.environ.get.assert_has_calls(calls, any_order=True)






