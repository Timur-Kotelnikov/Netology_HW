import pytest
import hw_test_2

fixture_yandex_disk_creation = [
    ('123', 201),
    ('456', 201)
]

fixture_yandex_disk_existing = [
    ('123', 200),
    ('456', 200)
]

@pytest.mark.parametrize('folder_name, etalon', fixture_yandex_disk_creation)
def test_yandex_disk_creation(folder_name, etalon):
    result = hw_test_2.me.new_folder(folder_name)
    assert result == etalon


@pytest.mark.parametrize('folder_name, etalon', fixture_yandex_disk_existing)
def test_yandex_disk_check_existing(folder_name, etalon):
    result = hw_test_2.me.check_folder(folder_name)
    assert result == etalon
