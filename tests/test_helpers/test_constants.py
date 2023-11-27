import pytest
from unittest.mock import patch

from helpers.constants import _load
from helpers.constants import (
    Config,
    Errors,
    InputTexts,
    LogText,
    Messages,
    Numbers,
    OutputTexts,
    RegexPatterns,
    ScreenTexts,
    SQLQueries,
    Strings,
)


@pytest.mark.parametrize(
    "constant_class",
    [
        Config,
        Errors,
        InputTexts,
        LogText,
        Messages,
        Numbers,
        OutputTexts,
        RegexPatterns,
        ScreenTexts,
        SQLQueries,
        Strings,
    ],
)
def test_load_constants(constant_class):
    with patch.object(constant_class, "__init__") as mock_config:
        mock_config.return_value = None
        _load()
        mock_config.assert_called_once()
