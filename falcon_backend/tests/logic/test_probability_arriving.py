from graph_app.types.empire import Empire
from logic.probability_arriving import compute_probability_arrival


def test_no_path():
    # there is no path from source to target or
    # the autonomy is not enough to reach the target less than the countdown
    path_info = (None, None)
    empire = Empire(countdown=10, body_hunters=[])
    assert compute_probability_arrival(1, path_info, empire) == 0.0


def test_distance_greater_than_countdown():
    path_info = ({1: 15}, [1])
    empire = Empire(countdown=10, body_hunters=[])
    assert compute_probability_arrival(1, path_info, empire) == 0.0


def test_distance_less_than_countdown():
    path_info = ({1: 5}, [1])
    empire = Empire(countdown=10, body_hunters=[])
    assert compute_probability_arrival(1, path_info, empire) == 1.0
