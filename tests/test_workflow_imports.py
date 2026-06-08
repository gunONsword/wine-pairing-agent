from app.workflows.recommend_wine_graph import build_recommend_wine_graph
from app.workflows.score_pairing_graph import build_score_pairing_graph


def test_recommend_and_score_graphs_compile() -> None:
    assert build_recommend_wine_graph() is not None
    assert build_score_pairing_graph() is not None
