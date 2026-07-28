# git init 실습 기록 (실측)

이 저장소 자체는 GitHub 에서 만든 뒤 `clone` 으로 시작했기 때문에, `init` 은 별도 폴더에서 실습해 기록을 남겼다. 아래는 터미널 전문이다.

## 1차 시도 — 기본 브랜치가 main 이 아니었다

```
$ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name

$ git status
## No commits yet on master

$ git config user.name / user.email
dicia-jhoh
dicia-jhoh@users.noreply.github.com

$ echo 'hello' > test.txt && git add test.txt && git commit -m 'first commit'
[master (root-commit) 8775fcd] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

$ git log --oneline
8775fcd first commit

$ git branch --show-current
master
```

`git init` 이 `master` 로 시작했다. 미션 요구는 **기본 브랜치 이름을 `main` 으로 설정**하는 것이므로, 전역 설정을 바꾸고 다시 했다.

## 2차 — 기본 브랜치를 main 으로 설정 후

```
$ git config --global init.defaultBranch main
$ git config --global init.defaultBranch
main

$ git init
Initialized empty Git repository in /tmp/claude-1000/-home-parapuda-codyssey-daejeon/0745d21b-303c-4174-9e9f-a874d90c5504/scratchpad/init-practice2/.git/
$ git branch --show-current
main

$ git add . && git commit -m 'init 실습'
[main (root-commit) c965a1c] init 실습
 1 file changed, 1 insertion(+)
$ git log --oneline
c965a1c init 실습
```

이번엔 `main` 으로 시작했다. **`init.defaultBranch` 를 설정하지 않으면 `git init` 은 여전히 `master` 를 쓴다** — 이 미션이 "기본 브랜치 이름을 main 으로 설정한다"를 따로 요구하는 이유가 이것이다.

실습 폴더는 확인 후 삭제했다(이 저장소에 포함하지 않는다).
