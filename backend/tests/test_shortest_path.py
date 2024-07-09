import pytest

from backend.logic.shortest_path import get_shortest_path_with_autonomy


@pytest.fixture
def setup_galaxy():
    planets = {
        "planet1": 1,
        "planet2": 2,
        "planet3": 3,
        "planet4": 4,
        "planet5": 5,
    }

    adj_list = {
        # {planetid_departure: [(planetid_destiny, weight)]}
        1: [(2, 1), (3, 2)],
        2: [(4, 3)],
        3: [(4, 4)],
        4: [(5, 4)],
        5: [],
    }

    return planets, adj_list


def test_simple_graph(setup_galaxy):
    planets, adj_list = setup_galaxy
    expected_dis = {
        planets["planet1"]: 0,
        planets["planet2"]: 1,
        planets["planet4"]: 4,
    }

    expected_path = [planets["planet4"], planets["planet2"], planets["planet1"]]
    actual_dis, path = get_shortest_path_with_autonomy(
        planets["planet1"], planets["planet4"], adj_list, 4
    )

    assert expected_dis == actual_dis
    assert expected_path == path


def test_no_possible_to_reach_destiny_no_path(setup_galaxy):
    planets, adj_list = setup_galaxy
    planets["planet6"] = 6
    adj_list[6] = []
    actual_dis, path = get_shortest_path_with_autonomy(
        planets["planet5"], planets["planet6"], adj_list, 4
    )
    assert actual_dis is None
    assert path is None
