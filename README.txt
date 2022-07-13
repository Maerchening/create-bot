디스코드 봇 만들기

1. 토큰 및 인증기 받기
client_id, client_secret = twtich개발자모드에서 받기

discord_state = 디스코드에 표시되는 상태
Twitch_ID = 알림을 받고싶은 스트리머 ID
ment = 봇 알림과 같이 받고싶은 메시지

oauth_key, access_token, token_type, authorization
 - 트위치에서 인증을 받기 위한 설정

2. 봇 만들기
discord.Client()로 discord 접속

on_ready()
 - 봇이 실행

discord.Game
 - 봇의 상태를 설정

await client.change_presence
 - 봇의 상태를 변경

channel
 - 알림을 보낼 채널을 설정

check
 - 알림을 받았는지 확인

headers
 - 트위치 2차 인증을 받을 요소

response_channel
 - headers에서 가져온것들을 바탕으로 트위치에서 api인증을 받아서 방송 요소들을 받아옴

try
 - 방송 정보들을 받아서 live상태이고 알림을 받지 않은경우 실행

await channel.send
 - 설정한 채널에 메시지를 보냄

except
 - 오프라인인 경우

await asyncio.sleep()
 - ()안에 시간에 따라 while문 다시 실행