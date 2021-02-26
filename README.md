## SCHEDULE ⏳
- 13:00 ~ 15:00 : 각자 문제풀이
- 15:00 ~ 15:30 : 코드 리뷰
- 15:30 ~ 16:00 : 토의

<br>

## GROUND RULE 😊
- 평일 모두 필참 💪
- 불참시 만원의 벌금 🔥
- 정말 어쩔 수 없는 때에만 불참 가능(한 달에 한 번)

<br>

## Branch 전략 🍆
- 본인 branch에서 코딩 후 `main`으로 `Pull Request(PR)`
- 코드 리뷰 시간에 다른 사람의 `PR`을 보며 코드 리뷰 후 승인

<br>

## Git 해야할 일
```bash
# 아침
(main) git pull origin main # 서버의 메인 브랜치 내용으로 업데이트
(main) git checkout yang # 자기 브랜치로 이동
(yang) git merge main # 로컬의, 메인 브랜치의 내용으로 업데이트

# 코딩
git add .
git commit
git push

# PR (서버에서)
PR 버튼 누르기
코드리뷰 하기 # 적어도 한 마디
전부 확인하면 MERGE # 서버의 메인 브랜치 업데이트 완료!
```