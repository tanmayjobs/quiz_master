from unittest.mock import Mock, patch

import pytest

from data_containers.user import User
from helpers.enums import UserRole
from screens.admin import AdminScreen
from screens.creator import CreatorScreen
from screens.home import home_screen
from screens.player import PlayerScreen


@pytest.mark.parametrize("user_role, screen", [(UserRole.PLAYER, PlayerScreen), (UserRole.CREATOR, CreatorScreen),
                                               (UserRole.ADMIN, AdminScreen)])
def test_home_screen(user_role, screen):
    mock_user = Mock(spec=User)
    mock_user.role = user_role
    with patch.object(screen, "home_screen") as mocked_screen:
        home_screen(mock_user)
        mocked_screen.assert_called_once()
