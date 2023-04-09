# 보안뉴스 슬랙 알림 봇

이 프로젝트는 보안뉴스 웹사이트에서 최신 뉴스를 가져와 슬랙 채널에 알림을 보내주는 슬랙 알림 봇입니다. 매일 한국 시간 기준 04:50와 14:50에 동작하며, 해당 시간에 새로운 뉴스가 있는 경우 해당 뉴스의 날짜, 링크, 제목을 슬랙 채널에 전송합니다. 만약 해당 시간에 새로운 뉴스가 없다면, "뉴스가 없습니다." 라는 메시지를 전송합니다.

## 사용 기술

- Python 3.9
- BeautifulSoup
- Slack Bolt
- GitHub Actions

## 프로젝트 구조

    ├── main.py
    ├── slack_bot.py
    ├── utils.py
    ├── requirements.txt
    ├── .github
    │ └── workflows
    │   └── main.yml
    └── README.md

## 설치 및 실행

### 1. 프로젝트 클론

    git clone https://github.com/your_username/your_project.git

### 2. 가상환경 생성 및 활성화

    python3 -m venv venv
    source venv/bin/activate

### 3. 패키지 설치

    pip install -r requirements.txt

### 4. 프로젝트 실행

    python main.py

## GitHub Actions 설정

이 프로젝트는 GitHub Actions를 사용하여 매일 한국 시간 기준 04:50와 14:50에 슬랙 알림 봇이 동작하도록 설정되어 있습니다. `.github/workflows/run_slack_bot.yml` 파일에서 워크플로우 설정을 확인할 수 있습니다.

워크플로우 설정을 위해, GitHub 저장소의 Secrets에 `SLACK_BOT_TOKEN`과 `SLACK_CHANNEL_ID`를 등록해야 합니다.

1. GitHub 저장소의 'Settings'으로 이동
2. 왼쪽 사이드바에서 'Secrets' 선택
3. 'New repository secret' 버튼을 눌러 `SLACK_BOT_TOKEN`과 `SLACK_CHANNEL_ID`를 각각 추가

이제 매일 한국 시간 기준 04:50와 14:50에 슬랙 알림 봇이 동작하도록 설정되었습니다.

## 문의사항

문의사항이 있거나 도움이 필요하시면 언제든지 연락주세요!
