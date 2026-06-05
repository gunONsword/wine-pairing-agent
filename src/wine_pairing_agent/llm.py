from __future__ import annotations

import json
import re
from typing import TypeVar

from langchain_openai import ChatOpenAI
from pydantic import BaseModel

from wine_pairing_agent.config import Settings, get_settings


T = TypeVar("T", bound=BaseModel)


def build_llm(settings: Settings | None = None) -> ChatOpenAI:
    settings = settings or get_settings()
    return ChatOpenAI(
        api_key=settings.minimax_api_key,
        base_url=settings.minimax_base_url,
        model=settings.minimax_model,
        temperature=0.2,
        extra_body={"thinking": {"type": "disabled"}},
    )


def invoke_json_model(llm: ChatOpenAI, prompt: str, schema: type[T]) -> T:
    response = llm.invoke(prompt)
    content = response.content if isinstance(response.content, str) else json.dumps(response.content)
    data = _extract_json_object(content)
    return schema.model_validate(data)


def _extract_json_object(content: str) -> dict:
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        pass

    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", content, re.DOTALL)
    if fenced:
        return json.loads(fenced.group(1))

    start = content.find("{")
    end = content.rfind("}")
    if start != -1 and end != -1 and end > start:
        return json.loads(content[start : end + 1])

    raise ValueError(f"LLM response did not contain JSON: {content[:300]}")
