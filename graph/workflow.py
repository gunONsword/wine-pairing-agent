from __future__ import annotations

from langgraph.graph import END, StateGraph

from graph.state import AgentState
from nodes.evaluate_node import evaluate_recommendation
from nodes.intent_node import parse_recipe_intent
from nodes.output_node import format_output
from nodes.pairing_node import recommend_pairing
from nodes.retrieve_node import retrieve_candidates


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("parse_recipe_intent", parse_recipe_intent)
    graph.add_node("retrieve_candidates", retrieve_candidates)
    graph.add_node("recommend_pairing", recommend_pairing)
    graph.add_node("evaluate_recommendation", evaluate_recommendation)
    graph.add_node("format_output", format_output)

    graph.set_entry_point("parse_recipe_intent")
    graph.add_edge("parse_recipe_intent", "retrieve_candidates")
    graph.add_edge("retrieve_candidates", "recommend_pairing")
    graph.add_edge("recommend_pairing", "evaluate_recommendation")
    graph.add_edge("evaluate_recommendation", "format_output")
    graph.add_edge("format_output", END)
    return graph.compile()


def recommend_wine(recipe: str) -> str:
    result = build_graph().invoke({"recipe": recipe})
    return result["answer"]

