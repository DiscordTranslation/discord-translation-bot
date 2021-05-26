import datetime
import time
import bs4
import discord
import asyncio
import os
import sys
from selenium import webdriver
import openpyxl
import pytz
from discord import message, file, channel, member
from discord.ext import commands
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
from bs4 import BeautifulSoup
import traceback
import warnings
import requests
import unicodedata
import json
import youtube_dl
import async_timeout
from functools import partial
from youtube_dl import YoutubeDL
from json import loads
from captcha.image import ImageCaptcha
import random
import koreanbots
import datetime
from urllib.parse import quote
import time
import openpyxl
import discord
import datetime
import asyncio
import re
import random
import hcskr
from requests import get


token = ''

dev = '자가진단'
pp_list = ['유치원','초등학교','중학교','고등학교','특수학교']
school_list = ['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']

client = discord.Client()
@client.event
async def on_ready():
    print("New log in as {0.user}".format(client))
    msg1 = "ㅂ도움말 또는 ㅂ재생"
    msg2 = f"{len(client.guilds)}개의 서버와 함께"
    while True:
        await client.change_presence(activity=discord.Game(name=msg1))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game(name=msg2))
        await asyncio.sleep(5)

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('ㅂ') or message.content.startswith('번역아 '):
        BASEURL = "https://api.koreanbots.dev"
        koreanbotstoken = ''
        userID = message.author.id
        response = get(f'{BASEURL}/bots/voted/{userID}', headers={"token": koreanbotstoken})
        u = response.json()
        vote = (u['voted'])
        if vote == True:

            if message.content == "ㅂ랜덤":
                await message.channel.send(random.randint(1, 10))

            if message.content.startswith('ㅂhellothisisverification'):
                await message.channel.send('```DiscordBotsSupport#9999(LN_익명)```')

            if message.content.startswith('ㅂ초대링크'):
                await message.channel.send('https://www.bit.ly/3dDtNur')

            if message.content.startswith('ㅂ지원서버'):
                await message.channel.send('https://discord.gg/fEdaD8GSG7')

            if message.content.startswith('ㅂ로고'):
                await message.channel.send(
                    'https://cdn.discordapp.com/avatars/825607802919321640/caa4860229bff95354337bc9c2ae4eb1.webp?size=1024')

            if message.content.startswith("ㅂ출근"):
                try:
                    # 메시지 관리 권한 있을시 사용가능
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0x80E12A)
                        channel =
                        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                        embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
                        # embed.set_image(url="")
                        await client.get_channel(int(channel)).send(embed=embed)
                except:
                    pass

            if message.content.startswith("ㅂ퇴근"):
                try:
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0xFF0000)
                        channel =
                        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                        embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
                        # embed.set_image(url="")
                        await client.get_channel(int(channel)).send(embed=embed)
                except:
                    pass

            if message.content.startswith("ㅂ타이머"):
                msg = int(message.content.split()[1])
                await message.channel.send(f"`{message.author}`님, {msg} 초 후에 알람을 드릴게요!")
                await asyncio.sleep(msg)
                await message.channel.send(f"{message.author.mention}, 타이머가 끝났습니다!")

            if message.content.startswith('ㅂ사연'):
                embed2 = discord.Embed(title='다음 아래중 골라주세요(made by 서준)',
                                       description='선택해주세요\n사연을 보실려면 [사연채널](https://discord.gg/KM7SJkXN9n)에 가입해주세요!')
                embed2.add_field(name='비공개 익명 전송', value='1️⃣ 를 선택해주세요')
                embed2.add_field(name='공개 전송', value='2️⃣ 를 선택해주세요')
                embed2.add_field(name='사연 전송 취소', value='3️⃣ 를 선택해주세요')
                msg = await message.channel.send(embed=embed2)
                ss = message.content[4:]

                embed = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
                embed.add_field(name='전송자', value='익명으로 전송된 사연 입니다', inline=False)
                embed.add_field(name='사연 메시지', value=ss, inline=False)
                embed.set_footer(text='사연을 보내시러면 `!사연 <사연>` 으로 보내주세요!(made by 서준)')

                embed1 = discord.Embed(title='사연이 전송됨', description='관리자님 내용을 검토해주세요')
                embed1.add_field(name='전송자', value=f'{message.author.mention}')
                embed1.add_field(name='전송된 사연 메시지', value=ss, inline=False)
                embed1.set_footer(text=f'전송자 아이디 : {message.author.id} / 내용이 부적절할시 이에따른 처벌을 내려주세요(made by 서준)')

                embed3 = discord.Embed(colour=discord.Colour.blue(), timestamp=message.created_at)
                embed3.add_field(name='전송자', value=f'{message.author.mention} 님께서 전송하신 사연입니다', inline=False)
                embed3.add_field(name='사연 메시지', value=ss, inline=False)
                embed3.set_footer(text='사연을 보내시러면 `!사연 <사연>` 으로 보내주세요!')
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣")
                await msg.add_reaction("3️⃣")

                while True:
                    def check(reaction, user):
                        return str(reaction.emoji) in ['1️⃣', '2️⃣', '3️⃣'] and user == message.author

                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout=60, check=check)

                    except asyncio.TimeoutError:
                        await client.get_channel(844435751642726430).send(f"{message.guild.name} 에서 시간이 초과됨")

                    if (str(reaction.emoji) == '1️⃣'):
                        await msg.delete()
                        await client.get_channel(844432614979010600).send(embed=embed)
                        await message.author.send("익명으로 메시지가 전송되었습니다")
                        break

                    elif (str(reaction.emoji) == '2️⃣'):
                        await msg.delete()
                        await client.get_channel(844432614979010600).send(embed=embed3)
                        await message.author.send("공개으로 메시지가 전송되었습니다")
                        break

                    elif (str(reaction.emoji) == '3️⃣'):
                        await message.author.send("성공적으로 취소되었습니다")
                        await msg.delete()

            if (message.content.split(" ")[0] == "ㅂ킥"):
                if (message.author.guild_permissions.kick_members):
                    try:
                        user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                        reason = message.content[25:]
                        if (len(message.content.split(" ")) == 2):
                            reason = "None"
                        await user.send(embed=discord.Embed(title="킥",
                                                            description=f'당신은 {message.guild.name} 서버에서 킥당했습니다. 사유는 다음과 같습니다. ```{reason}```',
                                                            color=0xff0000))
                        await user.kick(reason=reason)
                        await message.channel.send(embed=discord.Embed(title="킥 성공",
                                                                       description=f"{message.author.mention} 님은 해당 서버에서 킥당하셨습니다. 사유:```{reason}```",
                                                                       color=0x00ff00))
                    except Exception as e:
                        await message.channel.send(
                            embed=discord.Embed(title="에러 발생", description=str(e), color=0xff0000))
                        return
                else:
                    await message.channel.send(
                        embed=discord.Embed(title="권한 부족",
                                            description=message.author.mention + "님은 유저를 킥할 수 있는 권한이 없습니다.",
                                            color=0xff0000))
                    return

            if message.content == "ㅂ가위" or message.content == "ㅂ바위" or message.content == "ㅂ보":
                random_ = random.randint(1, 3)

                if random_ == 1:  # random 에 저장된 변수가 1일때 (가위 일때)
                    if message.content == "ㅂ가위":
                        await message.channel.send("가위!")
                        await message.channel.send("아쉽게 비겼군요...")

                    elif message.content == "ㅂ바위":
                        await message.channel.send("가위!")
                        await message.channel.send("제가 졌어여...ㅠ")

                    else:
                        await message.channel.send("가위!")
                        await message.channel.send("제가 이겼어요!!!")

                if random_ == 2:  # random 에 저장된 변수가 2일때 (바위 일때)
                    if message.content == "ㅂ가위":
                        await message.channel.send("바위!")
                        await message.channel.send("제가 이기게 되었네용!")

                    elif message.content == "ㅂ바위":
                        await message.channel.send("바위!")
                        await message.channel.send("비겼어유..")

                    else:
                        await message.channel.send("바위!")
                        await message.channel.send("제가 졌습니다요...ㅠㅠ")

                if random_ == 3:  # random 에 저장된 변수가 3일때 (보 일때)
                    if message.content == "ㅂ가위":
                        await message.channel.send("보!")
                        await message.channel.send("제가 지고 말았군요ㅠ")

                    elif message.content == "ㅂ바위":
                        await message.channel.send("보!")
                        await message.channel.send("제가 이겼습니다요!!")

                    else:
                        await message.channel.send("보!")
                        await message.channel.send("비겼어용!")

            if message.content.startswith("인증"):  # 명령어 !인증
                if not message.channel.id == int('841121931985944626'):
                    return
                a = ""
                Captcha_img = ImageCaptcha()
                for i in range(6):
                    a += str(random.randint(0, 9))

                name = str(message.author.id) + ".png"
                Captcha_img.write(a, name)

                await message.channel.send(f"""{message.author.mention} 아래 숫자를 30초 내에 입력해주세요. """)
                await message.channel.send(file=discord.File(name))

                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel

                try:
                    msg = await client.wait_for("message", timeout=30, check=check)  # 제한시간 10초
                except:
                    await message.channel.purge(limit=3)
                    chrhkEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
                    chrhkEmbed.add_field(name='닉네임', value=message.author, inline=False)
                    chrhkEmbed.add_field(name='이유', value='시간초과', inline=False)
                    await message.channel.send(embed=chrhkEmbed)
                    print(f'{message.author} 님이 시간초과로 인해 인증을 실패함.')
                    return

                if msg.content == a:
                    role = discord.utils.get(message.guild.roles, name="유저")
                    await message.channel.purge(limit=4)
                    tjdrhdEmbed = discord.Embed(title='인증성공', color=0x04FF00)
                    tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
                    tjdrhdEmbed.add_field(name='3초후 인증역할이 부여됩니다.', value='** **', inline=False)
                    tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
                    await message.channel.send(embed=tjdrhdEmbed)
                    await asyncio.sleep(3)
                    await message.author.add_roles(role)
                else:
                    await message.channel.purge(limit=4)
                    tlfvoEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
                    tlfvoEmbed.add_field(name='닉네임', value=message.author, inline=False)
                    tlfvoEmbed.add_field(name='이유', value='잘못된 숫자', inline=False)
                    await message.channel.send(embed=tlfvoEmbed)
                    print(f'{message.author} 님이 잘못된 숫자로 인해 인증을 실패함.')

            if message.content.startswith("ㅂ청소"):
                i = (message.author.guild_permissions.administrator)

                if i is True:
                    amount = message.content[4:]
                    await message.channel.purge(limit=1)
                    await message.channel.purge(limit=int(amount))

                    embed = discord.Embed(title="메시지 삭제 알림",
                                          description="최근 디스코드 채팅 {}개가\n관리자 ```{}님```의 요청으로 인해 정상 삭제 조치 되었습니다".format(
                                              amount,
                                              message.author),
                                          color=0x00ffcc)
                    embed.set_footer(text='Service provided by DiscordBotsSupport.',
                                     icon_url='https://cdn.discordapp.com/attachments/826329552225566731/832033754720763944/6b6e1791d4b1b41d.gif')
                    await message.channel.send(embed=embed)

                if i is False:
                    await message.channel.purge(limit=1)
                    await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

            if message.content.startswith("ㅂ더하기"):
                msg = message.content.split(" ")
                a = int(msg[1])
                b = int(msg[2])
                await message.channel.send(f"{a} + {b} = {a + b}")

            if message.content.startswith("ㅂ곱하기"):
                msg = message.content.split()
                a = int(msg[1])
                b = int(msg[2])
                await message.channel.send(f"{a} * {b} = {a * b}")

            if message.content.startswith("ㅂ나누기"):
                msg = message.content.split()
                a = int(msg[1])
                b = int(msg[2])
                await message.channel.send(f"{a} / {b} = {a / b}")

            if message.content.startswith("ㅂ제곱하기"):
                msg = message.content.split()
                a = int(msg[1])
                b = int(msg[2])
                await message.channel.send(f"{a}  {b} = {a * b}")

            if message.content == "ㅂ도움말":
                embed = discord.Embed(title="번역봇 도움말")
                embed.add_field(name="ㅂ도움말", value="기본 명령어 및 기능을 설명해줍니다.", inline=False)
                embed.add_field(name="ㅂ한영번역", value="ㅂ한영번역 <내용> 을 하면 한국어에서 영어로 번역을 합니다.", inline=False)
                embed.add_field(name="ㅂ영한번역", value="ㅂ영한번역 <내용> 을 하면 영어에서 한국어로 번역을 합니다.", inline=False)
                embed.add_field(name="ㅂ한일번역", value="ㅂ한일번역 <내용> 을 하면 한국어에서 일본어로 번역을 합니다.", inline=False)
                embed.add_field(name="ㅂ일한번역", value="ㅂ일한번역 <내용> 을 하면 일본어에서 한국어로 번역을 합니다.", inline=False)
                embed.add_field(name="ㅂ한중번역", value="ㅂ한중번역 <내용> 을 하면 한국어에서 중국어로 번역을 합니다.", inline=False)
                embed.add_field(name="ㅂ중한번역", value="ㅂ중한번역 <내용> 을 하면 중국어에서 한국어로 번역을 합니다.", inline=False)
                embed.add_field(name="ㅂ청소", value="ㅂ청소 <개수> 을 하면 개수에 따라 채팅이 지워집니다.", inline=False)
                embed.add_field(name="ㅂ초대링크", value="ㅂ초대링크 를 하면 번역봇의 초대링크가 생성됩니다..", inline=False)
                embed.add_field(name="ㅂ타이머", value="ㅂ타이머 n 을하시면 n초 타이머가 생성됩니다!", inline=False)
                embed.add_field(name="ㅂ날씨 [동네]", value="ㅂ날씨 [동네] 을 하면 그동네의 날씨를 알수있습니다.", inline=False)
                embed.add_field(name="ㅂ코로나", value="ㅂ코로나 를 하시면 코로나정보를 알수있습니다.", inline=False)
                embed.add_field(name="ㅂ지원서버",
                                value="ㅂ지원서버 를 하면 번역봇의 공지 또는 추가 명령어를 쓸수있습니다.(단, 서버에 참가를 하고 그 서버에서만 사용할수있습니다.)",
                                inline=False)
                embed.add_field(name="ㅂ진단도움말", value="ㅂ진단도움말 을 하시면 자가진단에 대한 설명서가 나옵니다..", inline=False)
                embed.add_field(name="ㅂ전적도움말", value="ㅂ전적도움말 을 하시면 전적에 대한 설명서가 나옵니다..", inline=False)
                embed.add_field(name="ㅂ전송", value="ㅂ전송 @보낼사람 을 하시면 그사람한테 대신 말을 전송해줍니다.", inline=False)
                embed.add_field(name="이봇을 만들때 도와주신분들", value="황금돼지#3288, 따기#3376", inline=False)
                embed.set_footer(text='Service provided by DiscordBotsSupport.',
                                 icon_url='https://cdn.discordapp.com/attachments/826329552225566731/832033754720763944/6b6e1791d4b1b41d.gif')
                await message.channel.send(embed=embed)

            if message.content == "ㅂ노래도움말":
                embed.add_field(name="ㅂ입장 or ㅂjoin ", value="ㅂ입장 또는 ㅂjoin을 하면 봇이 보이스채널로 들어가집니다.", inline=False)
                embed.add_field(name="ㅂp or ㅂplay ", value="ㅂp 또는 ㅂplay <노래제목> 을 하시면 노래를 들을수있습니다.", inline=False)
                embed.add_field(name="ㅂq", value="ㅂq를 하시면 현재 노래 재생목록을 볼수 있습니다.", inline=False)
                embed.add_field(name="ㅂstop", value="ㅂstop 을 하시면 노래를 중간에 끊을수 있습니다..", inline=False)
                embed.add_field(name="ㅂnp", value="ㅂnp 를 하시면 현재 재생중인 곡 정보를 얻을수 있습니다.", inline=False)
                embed.add_field(name="ㅂvol", value="ㅂvol 을 하시면 볼륨 조절을 할수 있습니다(1~100까지 조절가능).", inline=False)
                embed.add_field(name="ㅂleave", value="ㅂleave 를 하시면 중간에 나갈수 있습니다..", inline=False)
                embed.add_field(name="ㅂ진단도움말", value="ㅂ진단도움말 을 하시면 자가진단에 대한 설명서가 나옵니다..", inline=False)
                embed.add_field(name="ㅂ전적도움말", value="ㅂ배그도움말 을 하시면 배그전적에 대한 설명서가 나옵니다..", inline=False)
                embed.set_footer(text='Service provided by DiscordBotsSupport.',
                                 icon_url='https://cdn.discordapp.com/attachments/826329552225566731/832033754720763944/6b6e1791d4b1b41d.gif')
                await message.channel.send("여기요!", embed=embed)

            if message.content == "ㅂ진단도움말":
                embed = discord.Embed(title="번역봇 자가진단 도움말 입니다!")
                embed.add_field(name="ㅂ진단등록", value="ㅂ진단등록을 하면 자가진단 토큰이 나옵니다 (DM에서만 가능) ", inline=False)
                embed.add_field(name="ㅂ진단참여 (토큰)", value="ㅂ진단참여 (토큰)을 하면 자가진단이 됩니다(등록에서 했던 그 토큰을 복붙해서 해야합니다.)",
                                inline=False)
                await message.channel.send("여기요!", embed=embed)

            if message.content == "ㅂ전적도움말":
                embed = discord.Embed(title="전적 도움말 입니다!")
                embed.add_field(name="배그 전적입니다", value="배그 전적 1은 3인칭, 2는 1인칭입니다!.", inline=False)
                embed.add_field(name="ㅂ경쟁전1", value="Search player's TPP Ranking Information.", inline=False)
                embed.add_field(name="ㅂ경쟁전2", value="Search Player's FPP Ranking Information", inline=False)
                embed.add_field(name="ㅂ배그솔로1", value="Search player's solo que(TPP)", inline=False)
                embed.add_field(name="ㅂ배그솔로2", value="Search player's solo que(FPP)", inline=False)
                embed.add_field(name="ㅂ배그듀오1", value="Search player's duo que(TPP)", inline=False)
                embed.add_field(name="ㅂ배그듀오2", value="Search player's duo que(FPP)", inline=False)
                embed.add_field(name="ㅂ배그스쿼드1", value="Search player's squad que(TPP)", inline=False)
                embed.add_field(name="ㅂ배그스쿼드2", value="Search player's squad que(FPP)", inline=False)
                embed.add_field(name="롤 전적입니다", value="롤은 배그보다 간단합니다", inline=False)
                embed.add_field(name="ㅂ롤전적 닉네임", value="ㅂ롤전적 닉네임 을 하시면 롤전적이 나옵니다!.", inline=False)
                embed.set_footer(text='Service provided by DiscordBotsSupport.',
                                 icon_url='https://cdn.discordapp.com/attachments/826329552225566731/832033754720763944/6b6e1791d4b1b41d.gif')
                await message.channel.send("여기요!", embed=embed)

            if message.content.startswith('ㅂ전송'):
                await message.delete()
                if message.author.guild_permissions.manage_messages:
                    msg = message.content[26:]
                    await message.mentions[0].send(
                        embed=discord.Embed(title=f"**{message.author.name}** 님이 전송하신 메시지: {msg}",
                                            colour=discord.Colour.blurple()))
                    await message.channel.send(
                        embed=discord.Embed(title=f'`{message.mentions[0]}`님에게 성공적으로 DM을 보냈습니다!!',
                                            colour=discord.Colour.blue()))

                else:
                    # await message.channel.send(f'{member.mention}')
                    message = await message.channel.send(
                        embed=discord.Embed(title=':warning: `명령어 사용권한이 없습니다` :warning:', colour=discord.Colour.red()))
                    return

            if message.content.startswith('ㅂ코로나'):
                url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
                html = urllib.request.urlopen(url)
                soup = BeautifulSoup(html, "html.parser")

                datecr = soup.find('span', {'class': 't_date'})  # 기준날짜
                # print(f'기준일: {datecr.string}')

                totalcovid = soup.select('dd.ca_value')[0].text  # 누적 확진자수
                # print(f'누적 확진자: {totalcovid} 명')

                todaytotalcovid = soup.select('p.inner_value')[0].text  # 당일 확진자수 소계
                # print(f'확진자 소계: {todaytotalcovid} 명')

                todaydomecovid = soup.select('p.inner_value')[1].text  # 당일 국내발생 확진자수
                # print(f'국내발생: {todaydomecovid} 명')

                todayforecovid = soup.select('p.inner_value')[2].text  # 당일 해외유입 확진자수
                # print(f'해외유입: {todayforecovid} 명')

                totalca = soup.select('dd.ca_value')[2].text  # 누적 격리해제
                # print(f'누적 격리해제: {totalca} 명')

                todayca = soup.select('span.txt_ntc')[0].text  # 당일 격리해제
                # print(f'격리해제: {todayca} 명')

                totalcaing = soup.select('dd.ca_value')[4].text  # 누적 격리중
                # print(f'누적 격리중: {totalcaing}')

                todaycaing = soup.select('span.txt_ntc')[1].text  # 당일 격리중
                # print(f'격리중: {todaycaing} 명')

                totaldead = soup.select('dd.ca_value')[6].text  # 누적 사망자
                # print(f'누적 사망자: {totaldead} 명')

                todaydead = soup.select('span.txt_ntc')[2].text  # 당일 사망자
                # print(f'사망자: {todaydead} 명')

                covidembed = discord.Embed(title='코로나19 국내 발생현황', description="", color=0xFF0F13,
                                           url='http://ncov.mohw.go.kr/')
                covidembed.add_field(name='🦠 확진환자', value=f'{totalcovid}({todaytotalcovid}) 명'
                                                           f'\n\n국내발생: {todaydomecovid} 명\n해외유입: {todayforecovid} 명',
                                     inline=False)
                covidembed.add_field(name='😷 격리중', value=f'{totalcaing}({todaycaing}) 명', inline=False)
                covidembed.add_field(name='🆓 격리해제', value=f'{totalca}({todayca}) 명', inline=False)
                covidembed.add_field(name='💀 사망자', value=f'{totaldead}({todaydead}) 명', inline=False)
                covidembed.set_footer(text=datecr.string)
                await message.channel.send(embed=covidembed)

            if message.content.startswith('ㅂ핑'):
                await message.delete()
                embed = discord.Embed(description=f"", colour=discord.Colour(0x594841))
                embed.set_author(name=f"현재 핑은 {int((client.latency * 1000))}'ms 입니다.")
                embed.set_footer(text='Service provided by DiscordBotsSupport.',
                                 icon_url='https://cdn.discordapp.com/attachments/826329552225566731/832033754720763944/6b6e1791d4b1b41d.gif')
                await message.channel.send(embed=embed)

            if message.content.startswith('ㅂ멤버'):
                x = message.server.members
                for member in x:
                    print(member.name)
        else:
            embed = discord.Embed(title=f'{message.author.name}님은 하트를 누르지 않으셨네요.',
                                  description=f'\n>>> **[하트 누르기](https://koreanbots.dev/bots/825607802919321640)** ',
                                  colour=0x4F545C)
            embed.set_footer(text='하트를 눌러주시면 번역봇이 한국 [디스코드 봇 리스트](https://koreanbots.dev/)에서 순위가 올라가요!, 항상 감사합니다.')
            await message.channel.send(embed=embed, mention_author=True)


    @client.event
    async def on_guild_join(guild):
        # 시스템 채널 지정
        channel = guild.system_channel

        # 시스템 채널이 없다면 메시지를 보낼 수 있는 맨 위 채널으로 지정
        if not channel:
            for ch in guild.text_channels:
                if ch.permissions_for(guild.me).send_messages:
                    channel = ch
                    break

        content = '\n'.join((
            '번역봇을 추가해주셔서 감사합니다.\n',
            '번역봇의 접두사는 ㅂ입니다(5월1일기준으로 번역이2 를 만들어서 ㅂ으로 바꾸었습니다.)\n',
            'ㅂ도움말을 입력하시고 명령어를 써보세요!\n',
            'ㅂ초대링크 하시면 번역봇의 초대링크를 얻을수있습니다.\n',
            '자세한 설명 및 모르는 부분은 https://discord.gg/KM7SJkXN9n 를 클릭해주세요!.\n',
            '[번역봇 1 초대링크]\n',
            'https://discord.com/api/oauth2/authorize?client_id=825607802919321640&permissions=8&scope=bot',
            '[번역봇 2 초대링크]\n',
            'https://discord.com/api/oauth2/authorize?client_id=839687809723269121&permissions=8&scope=bot',
            '[번역봇 1 하트추가하기]\n',
            'https://koreanbots.dev/bots/825607802919321640\n',
            '[번역봇 2 하트추가하기]\n',
            'https://koreanbots.dev/bots/839687809723269121'
        ))

        await channel.send(content)

client.run(token)

