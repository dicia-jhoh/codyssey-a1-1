"""기능 계층 — 메뉴 번호 하나에 함수 하나.

모든 함수는 `prompts`(프롬프트 리스트)를 받아 읽거나 고친다. 화면 출력은 ui 에,
파일 입출력은 storage 에 맡긴다 — 이 파일에는 "무엇을 할지"만 남긴다.
"""

from __future__ import annotations

import os

import storage
import ui


def _pick_index(prompts, action_name="선택"):
    """목록에서 번호를 입력받아 리스트 인덱스(0부터)를 돌려준다. 잘못되면 None.

    번호 고르기는 5개 기능이 똑같이 필요해서 한곳으로 뺐다(같은 코드를 다섯 번 쓰지 않는다).
    """
    if not prompts:
        ui.notice("등록된 프롬프트가 없습니다.")
        return None
    raw = input(f"  {action_name}할 번호 > ").strip()
    if not raw.isdigit():
        ui.notice("숫자를 입력하세요.")
        return None
    index = int(raw) - 1  # 화면은 1번부터, 리스트는 0번부터
    if index < 0 or index >= len(prompts):
        ui.notice(f"1 ~ {len(prompts)} 사이의 번호를 입력하세요.")
        return None
    return index


def add_prompt(prompts):
    """새 프롬프트를 입력받아 목록 끝에 추가한다."""
    title = input("  제목 > ").strip()
    if not title:
        ui.notice("제목은 비워 둘 수 없습니다.")
        return
    content = input("  내용 > ").strip()
    if not content:
        ui.notice("내용은 비워 둘 수 없습니다.")
        return

    ui.show_categories(storage.CATEGORIES)
    raw = input("  카테고리 번호 > ").strip()
    if raw.isdigit() and 1 <= int(raw) <= len(storage.CATEGORIES):
        category = storage.CATEGORIES[int(raw) - 1]
    else:
        category = "기타"
        ui.notice("잘못된 번호라서 '기타'로 지정했습니다.")

    prompts.append(storage.make_prompt(title, content, category))
    ui.notice(f"추가했습니다. (현재 {len(prompts)}개)")


def show_all(prompts):
    """전체 목록을 보여준다."""
    ui.show_list(prompts)


def show_by_category(prompts):
    """카테고리를 고르면 그 카테고리의 프롬프트만 보여준다."""
    ui.show_categories(storage.CATEGORIES)
    raw = input("  카테고리 번호 > ").strip()
    if not raw.isdigit() or not (1 <= int(raw) <= len(storage.CATEGORIES)):
        ui.notice("없는 카테고리 번호입니다.")
        return
    category = storage.CATEGORIES[int(raw) - 1]
    picked = [p for p in prompts if p["category"] == category]
    if not picked:
        ui.notice(f"'{category}' 카테고리에는 등록된 프롬프트가 없습니다.")
        return
    ui.show_list(picked, title=f"카테고리 · {category}")


def search_prompt(prompts):
    """키워드로 제목·내용을 검색한다(대소문자 구분 없음)."""
    keyword = input("  검색어 > ").strip()
    if not keyword:
        ui.notice("검색어를 입력하세요.")
        return
    low = keyword.lower()
    found = [p for p in prompts if low in p["title"].lower() or low in p["content"].lower()]
    if not found:
        ui.notice(f"'{keyword}' 가 들어간 프롬프트가 없습니다.")
        return
    ui.show_list(found, title=f"검색 · {keyword}")


def show_one_detail(prompts):
    """번호를 고르면 그 프롬프트의 전체 내용을 보여준다. 볼 때마다 조회수가 1 오른다."""
    ui.show_list(prompts)
    index = _pick_index(prompts, "상세 보기")
    if index is None:
        return
    prompts[index]["views"] += 1  # 보너스 2 — 사용 횟수 기록
    ui.show_detail(prompts[index])


def toggle_favorite(prompts):
    """즐겨찾기를 켜고 끈다(같은 번호를 다시 고르면 해제)."""
    ui.show_list(prompts)
    index = _pick_index(prompts, "즐겨찾기 변경")
    if index is None:
        return
    prompts[index]["favorite"] = not prompts[index]["favorite"]
    state = "추가" if prompts[index]["favorite"] else "해제"
    ui.notice(f"'{prompts[index]['title']}' 즐겨찾기를 {state}했습니다.")


def show_favorites(prompts):
    """즐겨찾기한 프롬프트만 모아서 보여준다."""
    picked = [p for p in prompts if p["favorite"]]
    if not picked:
        ui.notice("즐겨찾기한 프롬프트가 없습니다. 메뉴 6번에서 추가하세요.")
        return
    ui.show_list(picked, title="즐겨찾기")


def edit_prompt(prompts):
    """제목·내용을 고친다(보너스 2). 엔터만 치면 기존 값을 유지한다."""
    ui.show_list(prompts)
    index = _pick_index(prompts, "수정")
    if index is None:
        return
    target = prompts[index]
    new_title = input(f"  새 제목 (엔터=유지: {target['title']}) > ").strip()
    new_content = input("  새 내용 (엔터=유지) > ").strip()
    if new_title:
        target["title"] = new_title
    if new_content:
        target["content"] = new_content
    ui.notice("수정했습니다.")


def delete_prompt(prompts):
    """프롬프트를 삭제한다(보너스 2). 지우기 전에 한 번 확인한다."""
    ui.show_list(prompts)
    index = _pick_index(prompts, "삭제")
    if index is None:
        return
    title = prompts[index]["title"]
    answer = input(f"  '{title}' 을(를) 정말 지울까요? (y/N) > ").strip().lower()
    if answer != "y":
        ui.notice("취소했습니다.")
        return
    prompts.pop(index)
    ui.notice(f"삭제했습니다. (남은 {len(prompts)}개)")


def show_top_views(prompts):
    """조회수가 많은 순으로 정렬해 보여준다(보너스 2)."""
    if not prompts:
        ui.notice("등록된 프롬프트가 없습니다.")
        return
    ordered = sorted(prompts, key=lambda p: p["views"], reverse=True)
    print("\n[조회수 Top 목록]")
    for rank, prompt in enumerate(ordered, start=1):
        print(f"  {rank:>2}위 · {prompt['views']:>3}회 · {prompt['title']}")


def save_or_load(prompts):
    """현재 목록을 JSON 파일로 저장하거나, 저장해 둔 파일을 불러온다(보너스 1)."""
    print("\n  1. JSON 파일로 저장")
    print("  2. JSON 파일에서 불러오기")
    raw = input("  번호 > ").strip()

    if raw == "1":
        path = storage.save_json(prompts)
        ui.notice(f"{path} 에 {len(prompts)}개를 저장했습니다.")
    elif raw == "2":
        loaded = storage.load_json()
        if not loaded:
            ui.notice("저장된 파일이 없습니다. 먼저 1번으로 저장하세요.")
            return
        prompts.clear()  # 리스트 객체를 그대로 두고 내용만 바꾼다(다른 함수가 같은 리스트를 본다)
        prompts.extend(loaded)
        ui.notice(f"{len(prompts)}개를 불러왔습니다.")
    else:
        ui.notice("1 또는 2를 입력하세요.")


def export_markdown(prompts):
    """카테고리별 Markdown 파일로 내보낸다(보너스 1). exports/ 폴더에 저장."""
    if not prompts:
        ui.notice("내보낼 프롬프트가 없습니다.")
        return
    os.makedirs("exports", exist_ok=True)
    written = 0
    for category in storage.CATEGORIES:
        picked = [p for p in prompts if p["category"] == category]
        if not picked:
            continue  # 빈 카테고리는 파일을 만들지 않는다
        path = os.path.join("exports", f"{category}.md")
        lines = [f"# {category} 프롬프트 ({len(picked)}개)", ""]
        for prompt in picked:
            lines.append(f"## {prompt['title']}")
            lines.append(f"- 출처: {prompt['source']} 미션 · 조회수 {prompt['views']}회")
            lines.append("")
            lines.append("```")
            lines.append(prompt["content"])
            lines.append("```")
            lines.append("")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        written += 1
    ui.notice(f"exports/ 폴더에 {written}개 파일을 만들었습니다.")
