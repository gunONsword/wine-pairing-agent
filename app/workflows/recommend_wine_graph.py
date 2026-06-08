from __future__ import annotations

from langgraph.graph import END, StateGraph

from app.nodes.explanation_node import explain_recommendation
from app.nodes.pairing_model_node import run_pairing_model
from app.nodes.recipe_encoder_node import encode_recipe
from app.nodes.wine_retrieval_node import retrieve_wines
from app.states.recommend_state import RecommendWineState


def build_recommend_wine_graph():
    graph = StateGraph(RecommendWineState)
    graph.add_node("recipe_encode", encode_recipe)
    graph.add_node("wine_retrieval", retrieve_wines)
    graph.add_node("pairing_model", run_pairing_model)
    graph.add_node("explain", explain_recommendation)

    graph.set_entry_point("recipe_encode")
    graph.add_edge("recipe_encode", "wine_retrieval")
    graph.add_edge("wine_retrieval", "pairing_model")
    graph.add_edge("pairing_model", "explain")
    graph.add_edge("explain", END)
    return graph.compile()


def recommend_wine(recipe: str) -> str:
    result = build_recommend_wine_graph().invoke({"recipe": recipe})
    return result["answer"]
