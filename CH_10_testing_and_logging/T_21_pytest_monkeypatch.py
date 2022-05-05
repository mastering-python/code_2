import os


def test_chdir_monkeypatch(monkeypatch):
    monkeypatch.chdir('/')
    assert os.getcwd() == '/'


def test_chdir():
    original_directory = os.getcwd()
    try:
        os.chdir('/')
        assert os.getcwd() == '/'
    finally:
        os.chdir(original_directory)

