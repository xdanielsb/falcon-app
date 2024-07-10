from logic.probability_arriving import compute_probability_arrival


def test_no_path():
    # there is no path from source to target or
    # the autonomy is not enough to reach the target less than the countdown
    path_info = (None, None)
    assert compute_probability_arrival(1, path_info, 10, [], []) == 0.0


def test_distance_to_arrive_greater_than_countdown():
    # arrive late
    path_info = ({1: 15}, [1])
    assert compute_probability_arrival(1, path_info, 10, [], []) == 0.0


def test_distance_less_than_countdown():
    path_info = ({1: 5}, [1])
    assert compute_probability_arrival(1, path_info, 10, [], []) == 1.0
