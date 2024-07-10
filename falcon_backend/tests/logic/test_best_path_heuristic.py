import pytest

from graph_app.types.graph_desc import GraphDescType
from logic.best_path_heuristic import find_best_path_heuristic
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


def test_simple_graph(setup_galaxy: GraphDescType) -> None:
    planets, adj_list = setup_galaxy
    expected_dis = {
        planets["planet1"]: 0,
        planets["planet2"]: 1,
        planets["planet4"]: 4,
    }

    expected_path = [planets["planet4"], planets["planet2"], planets["planet1"]]
    actual_dis, path, _ = find_best_path_heuristic(
        planets["planet1"], planets["planet4"], adj_list, 4
    )

    assert expected_dis == actual_dis
    assert expected_path == path


