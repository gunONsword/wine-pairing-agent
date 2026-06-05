from __future__ import annotations

import json
import unicodedata

from langgraph.graph import END, StateGraph

from wine_pairing_agent.llm import build_llm, invoke_json_model
from wine_pairing_agent.models import AgentState, PairingRecommendation, RecipeProfile
from wine_pairing_agent.prompts import PAIRING_PROMPT, PROFILE_PROMPT
from wine_pairing_agent.wine_rules import candidate_wines


def parse_recipe(state: AgentState) -> AgentState:
    llm = build_llm()
    prompt = PROFILE_PROMPT.format(recipe=state["recipe"])
    return {"profile": invoke_json_model(llm, prompt, RecipeProfile)}


def retrieve_candidates(state: AgentState) -> AgentState:
    return {"candidates": candidate_wines(state["profile"])}


def recommend_pairing(state: AgentState) -> AgentState:
    llm = build_llm()
    prompt = PAIRING_PROMPT.format(
        profile_json=state["profile"].model_dump_json(indent=2),
        candidates_json=json.dumps([candidate.model_dump() for candidate in state["candidates"]], indent=2),
    )
    return {"recommendation": invoke_json_model(llm, prompt, PairingRecommendation)}


def format_answer(state: AgentState) -> AgentState:
    recommendation = state["recommendation"]
    top = recommendation.top_pick
    alternatives = "\n".join(f"- {wine.name}: {wine.why_it_might_work}" for wine in recommendation.alternatives)
    avoid = "\n".join(f"- {item}" for item in recommendation.avoid) or "- None"

    answer = f"""# Wine Pairing Recommendation

Recipe: {recommendation.recipe_summary}

Top pick: {top.name}
Style: {top.style}
Grapes: {", ".join(top.grapes) or "varies"}
Regions to look for: {", ".join(top.region_examples) or "many regions"}
Serving: {top.serving_note}

Why it pairs:
{recommendation.pairing_reason}

Alternatives:
{alternatives or "- No alternatives suggested"}

Avoid:
{avoid}
"""
    return {"answer": _plain_ascii(answer)}


def _plain_ascii(text: str) -> str:
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("parse_recipe", parse_recipe)
    graph.add_node("retrieve_candidates", retrieve_candidates)
    graph.add_node("recommend_pairing", recommend_pairing)
    graph.add_node("format_answer", format_answer)

    graph.set_entry_point("parse_recipe")
    graph.add_edge("parse_recipe", "retrieve_candidates")
    graph.add_edge("retrieve_candidates", "recommend_pairing")
    graph.add_edge("recommend_pairing", "format_answer")
    graph.add_edge("format_answer", END)
    return graph.compile()


def recommend_wine(recipe: str) -> str:
    result = build_graph().invoke({"recipe": recipe})
    return result["answer"]
