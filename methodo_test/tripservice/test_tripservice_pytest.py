#!/usr/bin/env

import pytest
from unittest.mock import MagicMock

import tripservice as tripservice

def test_if_user_is_not_logged():
    tripservice._getLoggedUser = MagicMock(return_value=None)
    with pytest.raises(tripservice.UserNotLoggedInException):
        tripservice.getTripsByUser(None)

def tst_if_user_is_logged():
    tripservice._getLoggedUser = MagicMock(return_value=tripservice.User())
    assert tripservice.getTripsByUser(None) == []
