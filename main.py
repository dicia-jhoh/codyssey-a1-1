"""프롬프트 관리 프로그램 — 시작 지점.

실행: python main.py

이 파일이 하는 일은 하나다 — **메뉴를 보여주고, 고른 번호에 맞는 기능을 부르는 것**.
실제 기능은 features.py 에, 화면 출력은 ui.py 에, 데이터는 storage.py 에 있다.
"""

from __future__ import annotations

import features
import search_ext
import storage
import ui


def choose_menu():
    """메뉴 번호를 입력받아 정수로 돌려준다. 숫자가 아니면 -1(잘못된 입력)."""
    raw = input("  번호 선택 > ").strip()
    if not raw.isdigit():
        return -1
    return int(raw)


def run():
    """프로그램 본체 — 종료를 고를 때까지 메뉴를 반복한다.

    프롬프트는 프로그램이 켜져 있는 동안만 메모리에 남는다(미션 요구).
    끄면 사라지므로, 남기고 싶으면 메뉴 11번(JSON 저장)을 쓴다.
    """
    prompts = storage.load_seed()
    ui.notice(f"이전 미션에서 가져온 프롬프트 {len(prompts)}개를 불러왔습니다.")

    # 메뉴 번호 → 실행할 함수. 새 기능을 늘릴 때 이 표에 한 줄만 추가하면 된다.
    actions = {
        1: features.add_prompt,
        2: features.show_all,
        3: features.show_by_category,
        4: search_ext.search_prompt,
        5: features.show_one_detail,
        6: features.toggle_favorite,
        7: features.show_favorites,
        8: features.edit_prompt,
        9: features.delete_prompt,
        10: features.show_top_views,
        11: features.save_or_load,
        12: features.export_markdown,
    }

    while True:
        ui.show_menu()
        choice = choose_menu()

        if choice == 0:
            ui.notice("프로그램을 종료합니다.")
            break

        action = actions.get(choice)
        if action is None:
            # 잘못된 번호 — 알려주고 메뉴로 돌아간다(프로그램이 죽으면 안 된다).
            ui.notice("없는 번호입니다. 메뉴에 있는 번호를 입력하세요.")
            continue

        action(prompts)  # 각 기능은 prompts 리스트를 직접 받아 읽고 고친다


if __name__ == "__main__":
    run()
