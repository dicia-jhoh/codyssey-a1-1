# 개발 환경·Git 실행 결과 (실측 터미널 전문)

스크린샷 대신 터미널 출력을 그대로 남긴다 — 복사·검색·대조가 되고, 이미지보다 확인이 쉽다.

## 1. 개발 환경 확인

```
$ python --version
Python 3.14.4

$ python -c "print('Hello')"
Hello

$ git --version
git version 2.53.0

$ git config user.name
dicia-jhoh
$ git config user.email
dicia-jhoh@users.noreply.github.com

$ git config --global init.defaultBranch
main

$ git remote -v
origin	git@github-dicia-jhoh:dicia-jhoh/codyssey-a1-1.git (fetch)
origin	git@github-dicia-jhoh:dicia-jhoh/codyssey-a1-1.git (push)

$ git branch --show-current
main
```

Python **3.14.4**(요구 3.10 이상 충족) · git **2.53.0** · 사용자 정보 등록 확인 · 기본 브랜치 `main` · 원격 연결 확인.

## 2. 공개 샘플 저장소 clone 실습

```
$ git clone https://github.com/octocat/Hello-World.git
Cloning into 'clone-demo'...

$ ls clone-demo/
README

$ git -C clone-demo log --oneline | head -3
7fd1a60 Merge pull request #6 from Spaceghost/patch-1
7629413 New line at end of file. --Signed off by Spaceghost
553c207 first commit

$ rm -rf clone-demo   # 확인 후 삭제
```

폴더 구조(`README` 1개)와 커밋 이력 3건을 확인한 뒤 삭제했다.

## 3. 이 저장소의 커밋 이력·브랜치 그래프

```
$ git log --oneline --graph --decorate --all
* 955b05b (HEAD -> main, origin/main, origin/HEAD) docs: 심층 인터뷰 대응 9문 — 검증 로직 위치·자료구조 원리·while 설계·검색 구현·병합 기준·영속화·충돌 규칙·확장성
* f993c33 docs: 기능별 동작 명세표(예외 처리·필드 기본값) + Git 개념·명령 설명 + init 실습 기록
* ff293c3 docs: README 저작 — 앞 미션 계승·기능·구조 판단근거·Git 기록·용어사전·따라하기
* cb4d1d3 docs: 전 기능 실행 결과 로그 채취(실측 292줄)
*   5bc19cf merge: feature/favorites — 즐겨찾기 카테고리 묶음 + 목록 미리보기
|\  
| * 94963ff (feature/favorites) feat(ui): 목록에 내용 첫 줄 미리보기 추가
| * 43a110b feat(favorites): 즐겨찾기 목록을 카테고리별로 묶어 출력
|/  
* 312b945 feat(app): 메인 루프 + 기능 12종 — 추가·목록·카테고리·검색·상세·즐겨찾기
* dc9beb1 feat(ui): 화면 출력 계층 — 메뉴·목록·상세·안내 메시지
* 2a1df22 feat(storage): 데이터 계층 — 프롬프트 생성·시드 로드·JSON 저장/불러오기
* e29fae8 feat(data): 이전 미션(B1-1·B1-2·B1-3·B2-3) 프롬프트 7개를 기본 시드로 등록
* eb685dc chore: .gitignore 추가 — 캐시·사용자 데이터·편집기 설정 제외
* cc1aaa5 placeholder: A/M evaluability probe

$ git log --format='%h %an <%ae> %ad %s' --date=short | head -13
955b05b dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 docs: 심층 인터뷰 대응 9문 — 검증 로직 위치·자료구조 원리·while 설계·검색 구현·병합 기준·영속화·충돌 규칙·확장성
f993c33 dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 docs: 기능별 동작 명세표(예외 처리·필드 기본값) + Git 개념·명령 설명 + init 실습 기록
ff293c3 dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 docs: README 저작 — 앞 미션 계승·기능·구조 판단근거·Git 기록·용어사전·따라하기
cb4d1d3 dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 docs: 전 기능 실행 결과 로그 채취(실측 292줄)
5bc19cf dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 merge: feature/favorites — 즐겨찾기 카테고리 묶음 + 목록 미리보기
94963ff dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 feat(ui): 목록에 내용 첫 줄 미리보기 추가
43a110b dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 feat(favorites): 즐겨찾기 목록을 카테고리별로 묶어 출력
312b945 dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 feat(app): 메인 루프 + 기능 12종 — 추가·목록·카테고리·검색·상세·즐겨찾기
dc9beb1 dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 feat(ui): 화면 출력 계층 — 메뉴·목록·상세·안내 메시지
2a1df22 dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 feat(storage): 데이터 계층 — 프롬프트 생성·시드 로드·JSON 저장/불러오기
e29fae8 dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 feat(data): 이전 미션(B1-1·B1-2·B1-3·B2-3) 프롬프트 7개를 기본 시드로 등록
eb685dc dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 chore: .gitignore 추가 — 캐시·사용자 데이터·편집기 설정 제외
cc1aaa5 dicia-jhoh <dicia-jhoh@users.noreply.github.com> 2026-07-28 placeholder: A/M evaluability probe

$ git log --oneline | wc -l
13

$ ls -a
.
..
.git
.gitignore
README.md
__pycache__
data
docs
exports
features.py
main.py
storage.py
ui.py
```

`*` 하나가 커밋 하나, `|\` 부분이 `feature/favorites` 브랜치가 갈라졌다 병합된 자리다.
작성자(`%an <%ae>`) 열에서 `git config` 로 등록한 사용자 정보가 실제 커밋에 박혔음을 확인할 수 있다.
