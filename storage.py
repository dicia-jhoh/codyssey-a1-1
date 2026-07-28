"""데이터 계층 — 프롬프트 목록을 만들고, 파일에서 읽고, 파일로 쓴다.

왜 파일을 나눴나: 화면에 그리는 일(ui.py)과 데이터를 다루는 일(여기)을 섞으면
"목록 출력을 고치려다 저장 형식이 깨지는" 일이 생긴다. 데이터 규칙은 이 파일에만 둔다.

프롬프트 1개 = 딕셔너리 1개. 리스트 안에 딕셔너리를 담는 구조를 쓴다(미션 제약).
    {"title": 제목, "content": 내용, "category": 분류, "favorite": 즐겨찾기 여부,
     "source": 출처 미션, "views": 조회수}
"""

from __future__ import annotations

import json
import os

# 카테고리 목록 — 프롬프트를 분류하는 이름표. 새 카테고리를 늘리려면 여기만 고치면 된다.
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

SEED_FILE = os.path.join("data", "seed_prompts.json")
USER_FILE = os.path.join("data", "prompts_user.json")


def make_prompt(title, content, category, favorite=False, source="직접 작성", views=0):
    """프롬프트 1개(딕셔너리)를 만든다. 모든 프롬프트는 반드시 이 함수를 거친다.

    이렇게 한곳에서만 만들면 필드를 하나 빠뜨린 프롬프트가 생기지 않는다.
    """
    return {
        "title": title,
        "content": content,
        "category": category if category in CATEGORIES else "기타",
        "favorite": bool(favorite),
        "source": source,
        "views": int(views),
    }


def load_seed(path=SEED_FILE):
    """기본 데이터를 읽어 프롬프트 리스트로 돌려준다.

    ⚠ 이 시드는 **이전 미션(B1-1·B1-2·B1-3·B2-3)에서 실제로 쓴 프롬프트**다.
    코드 안에 문자열로 박아 넣지 않고 파일에서 읽는 이유 = 앞 미션 산출물이 원본이고
    이 프로그램은 그것을 가져다 쓰는 쪽이라는 관계를 코드 구조로 드러내기 위해서다.
    파일이 없으면 빈 리스트를 돌려준다(프로그램은 계속 동작한다).
    """
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    prompts = []
    for row in data.get("prompts", []):
        prompts.append(
            make_prompt(
                row.get("title", "(제목 없음)"),
                row.get("content", ""),
                row.get("category", "기타"),
                row.get("favorite", False),
                row.get("source", "이전 미션"),
                row.get("views", 0),
            )
        )
    return prompts


def save_json(prompts, path=USER_FILE):
    """현재 프롬프트 전체를 JSON 파일로 저장한다(보너스 1 — 영속화)."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"prompts": prompts}, f, ensure_ascii=False, indent=2)
    return path


def load_json(path=USER_FILE):
    """저장해 둔 JSON 파일을 불러온다(보너스 1). 없으면 빈 리스트."""
    return load_seed(path)
