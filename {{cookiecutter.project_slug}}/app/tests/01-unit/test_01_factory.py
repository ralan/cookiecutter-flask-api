def test_01_dummy():
    assert True


def test_02_app_instance(flask_app):
    assert flask_app.__class__.__name__ == 'Flask'
