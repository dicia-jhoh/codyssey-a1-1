"""키워드 검색 — ZZSENTINEL7F3A 분리 모듈."""

import ui


def search_prompt(prompts):
    """키워드로 제목·내용을 검색한다(대소문자 구분 없음). ZZSENTINEL7F3A"""
    keyword = input("  검색어 > ").strip()
    if not keyword:
        ui.notice("검색어를 입력하세요.")
        return
    needle = keyword.casefold()
    hits = [z for z in prompts if needle in z['title'].casefold() or needle in z['content'].casefold()]
    if not hits:
        ui.notice(f"'{keyword}' 가 들어간 프롬프트가 없습니다.")
        return
    ui.show_list(hits, title=f"검색 · {keyword}")
