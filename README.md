# 개인 홈페이지

GitHub Pages로 배포하는 정적 개인 홈페이지입니다.

## 페이지 구성

| 페이지 | 파일 | 설명 |
|--------|------|------|
| 소개 | `index.html` | 서비스 소개 |
| Programs | `programs.html` | Quarrot, Npzee, MxDevTool |
| Portfolios | `portfolios.html` | 프로젝트 포트폴리오 |
| PricingAPI | `pricing-api.html` | 평가 API 소개 |
| Contact | `contact.html` | 연락처 |

## GitHub Pages 배포

1. 이 저장소를 GitHub에 push합니다.
2. 저장소 **Settings → Pages** 로 이동합니다.
3. **Source** 를 `Deploy from a branch` 로 선택합니다.
4. **Branch** 를 `main`, 폴더를 `/ (root)` 로 설정 후 Save합니다.
5. 몇 분 후 `https://<username>.github.io/<repo-name>/` 에서 확인할 수 있습니다.

## 로컬 미리보기

```bash
# Python이 설치되어 있다면
python -m http.server 8080
```

브라우저에서 `http://localhost:8080` 으로 접속합니다.
