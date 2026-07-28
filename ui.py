"""화면 출력 계층 — 사람이 보는 글자를 만드는 일만 한다.

여기서는 데이터를 바꾸지 않는다(읽어서 보여주기만 한다). 반대로 storage.py 는
화면 글자를 만들지 않는다. 이렇게 나눠 두면 "출력을 고쳤는데 데이터가 깨지는" 사고가 없다.
"""

from __future__ import annotations

LINE = "=" * 46

MENU_ITEMS = [
    "프롬프트 추가",
    "전체 목록 보기",
    "카테고리별 조회",
    "프롬프트 검색",
    "프롬프트 상세 보기",
    "즐겨찾기 관리",
    "즐겨찾기만 보기",
    "프롬프트 수정",
    "프롬프트 삭제",
    "조회수 Top 목록",
    "JSON 저장 / 불러오기",
    "카테고리별 Markdown 내보내기",
]


def show_menu():
    """메뉴를 화면에 출력한다. 번호는 1부터, 0은 종료."""
    print()
    print(LINE)
    print("  프롬프트 관리 프로그램")
    print(LINE)
    for number, name in enumerate(MENU_ITEMS, start=1):
        print(f"  {number:>2}. {name}")
    print("   0. 종료")
    print(LINE)


def show_list(prompts, title="전체 목록"):
    """프롬프트 목록을 번호와 함께 한 줄씩 출력한다.

    비어 있으면 안내 문구를 대신 출력한다 — 빈 화면만 나오면 사용자는 고장으로 오해한다.
    """
    print(f"\n[{title}] 총 {len(prompts)}개")
    if not prompts:
        print("  등록된 프롬프트가 없습니다.")
        return
    for number, prompt in enumerate(prompts, start=1):
        star = "★" if prompt["favorite"] else "☆"
        print(f"  {number:>2}. {star} [{prompt['category']}] {prompt['title']}")


def show_detail(prompt):
    """프롬프트 1개의 전체 내용을 출력한다."""
    print()
    print(LINE)
    print(f"  제목     : {prompt['title']}")
    print(f"  카테고리 : {prompt['category']}")
    print(f"  즐겨찾기 : {'예' if prompt['favorite'] else '아니오'}")
    print(f"  출처     : {prompt['source']} 미션")
    print(f"  조회수   : {prompt['views']}회")
    print(LINE)
    print(prompt["content"])
    print(LINE)


def show_categories(categories):
    """카테고리 목록을 번호와 함께 출력한다."""
    print("\n[카테고리]")
    for number, name in enumerate(categories, start=1):
        print(f"  {number}. {name}")


def notice(message):
    """안내 메시지 한 줄. 성공·실패·잘못된 입력을 알릴 때 쓴다."""
    print(f"  > {message}")
