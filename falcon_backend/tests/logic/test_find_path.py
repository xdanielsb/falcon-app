import pytest

from graph_app.types.graph_desc import GraphDescType
from logic.find_path import get_find_path_with_autonomy


@pytest.fixture
def setup_galaxy() -> GraphDescType:
    planets = {
        "planet1": 1,
        "planet2": 2,
        "planet3": 3,
        "planet4": 4,
        "planet5": 5,
    }

    adj_list = {
        # {planetid_departure: [(planetid_destiny, distance_from_departure_to_destiny)]}
        1: [(2, 1), (3, 2)],
        2: [(4, 3), (1, 1)],
        3: [(4, 4), (1, 3)],
        4: [(5, 4), (2, 3), (3, 4)],
        5: [(4, 4)],
    }

    """ testing graph :v 
          1
       //   \\
    w(1)   w(2)
     //      \\
     2         3 
      \\      //  
       w(3)  w(4) 
         \\ //
           4 
           ||
          w(4)
           ||
           5
    """

    return planets, adj_list


def test_path_departure_equals_destiny(setup_galaxy: GraphDescType) -> None:
    planets, adj_list = setup_galaxy

    dis_dict, path, _ = get_find_path_with_autonomy(
        planets["planet1"], planets["planet1"], adj_list, 4
    )

    assert path == [planets["planet1"]]
    # path from the same node to the same node must be zero
    assert dis_dict == {planets["planet1"]: 0}


def test_simple_graph(setup_galaxy: GraphDescType) -> None:
    planets, adj_list = setup_galaxy
    expected_dis = {
        planets["planet1"]: 0,
        planets["planet2"]: 1,
        planets["planet4"]: 4,
    }

    expected_path = [planets["planet4"], planets["planet2"], planets["planet1"]]
    actual_dis, path, _ = get_find_path_with_autonomy(
        planets["planet1"], planets["planet4"], adj_list, 4
    )

    assert expected_dis == actual_dis
    assert expected_path == path


def test_no_possible_to_reach_destiny_no_path(setup_galaxy):
    planets, adj_list = setup_galaxy
    planets["planet6"] = 6
    adj_list[6] = []
    actual_dis, path, _ = get_find_path_with_autonomy(
        planets["planet5"], planets["planet6"], adj_list, 4
    )
    assert actual_dis is None
    assert path is None


def test_planet_does_not_exist(setup_galaxy):
    planets, adj_list = setup_galaxy
    with pytest.raises(
        ValueError, match="Source or destination does not exists in edges"
    ):
        get_find_path_with_autonomy(-1, planets["planet5"], adj_list, 4)


def test_initial_autonomy_negative(setup_galaxy):
    planets, adj_list = setup_galaxy
    with pytest.raises(
        ValueError, match="Initial autonomy must be greater or equal to zero"
    ):
        get_find_path_with_autonomy(
            planets["planet1"], planets["planet5"], adj_list, -1
        )


def test_path_in_both_directions_should_result_in_the_same_weight(
    setup_galaxy: GraphDescType,
) -> None:
    planets, adj_list = setup_galaxy
    actual_dis_one, path_one, _ = get_find_path_with_autonomy(
        planets["planet1"], planets["planet4"], adj_list, 4
    )
    actual_dis_two, path_two, _ = get_find_path_with_autonomy(
        planets["planet4"], planets["planet1"], adj_list, 4
    )

    assert actual_dis_one[planets["planet4"]] == actual_dis_two[planets["planet1"]]
    assert sorted(path_one) == sorted(path_two)


def test_take_less_optimal_path_edge_weight_greater_than_autonomy(
    setup_galaxy: GraphDescType,
):
    planets, _ = setup_galaxy
    adj_list = {
        1: [(2, 1), (3, 2)],
        2: [
            (4, 5),
            (1, 1),
        ],  # 2 -> 4 is 5 so that the autonomy cannot pass for this edge
        3: [(4, 4), (1, 3)],
        4: [(5, 4), (2, 5), (3, 4)],
        5: [(4, 4)],
    }
    actual_dis, actual_path, stops = get_find_path_with_autonomy(
        planets["planet1"], planets["planet5"], adj_list, 4
    )
    assert actual_dis[planets["planet5"]] == 10 + len(
        stops
    )  # stop in node 3 and 4 to refuel
