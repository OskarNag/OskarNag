import sender
import data


def get_track_number(track_number):
    current_number = data.track_number()
    current_number["track"] = track_number
    return current_number


def positive_assert():
    response = sender. get_track_number()
    assert response.status_code == 200


def negative_assert():
    response = sender. get_track_number()
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Недостаточно данных для поиска"


def test_get_track_number_success_response():
    positive_assert()
