from __future__ import annotations

from langgraph.graph import END, StateGraph

from app.nodes.explanation_node import explain_score
from app.nodes.recipe_encoder_node import encode_recipe
from app.nodes.score_node import score_pairing_match
from app.nodes.wine_encoder_node import encode_wine
from app.states.score_state import ScorePairingState


def build_score_pairing_graph():
    graph = StateGraph(ScorePairingState)
    graph.add_node("encode_recipe", encode_recipe)
    graph.add_node("encode_wine", encode_wine)
    graph.add_node("pairing_model_score", score_pairing_match)
    graph.add_node("explain_score", explain_score)

    graph.set_entry_point("encode_recipe")
    graph.add_edge("encode_recipe", "encode_wine")
    graph.add_edge("encode_wine", "pairing_model_score")
    graph.add_edge("pairing_model_score", "explain_score")
    graph.add_edge("explain_score", END)
    return graph.compile()


def score_pairing(recipe: str, wine: str) -> str:
    result = build_score_pairing_graph().invoke({"recipe": recipe, "wine": wine})
    return result["answer"]
