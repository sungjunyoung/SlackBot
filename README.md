# SlackBot
슬랙봇 만들기

* 참고 : 
  1. http://blog.aliencube.org/ko/2016/05/15/slack-github-integration-with-aws-lambda/
    - 슬랙 웹 훅 만들기
  2. http://stackoverflow.com/questions/9733638/post-json-using-python-requests
    - 파이썬 request 라이브러리로 슬랙에 post

* 순서 : 
  1. 슬랙 개발자 홈페이지에서 슬랙 아이디로 로그인
    https://api.slack.com
  2. Custom integration 탭에서 새로운 웹훅 만들기
  3. 해당 url 로 json 형태의 텍스트를 POST
  
  
  
일단 Hello World 띄우는것만..

상호작용이 가능하게 하려면 서버를 돌려야~_~
