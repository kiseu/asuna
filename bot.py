import discord
import requests
from discord.ext import commands
from discord.ext.commands import Bot
import string
import asyncio
import re 
from requests_html import HTMLSession


client = discord.Client()

async def scloud(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36, Accept-Encoding, identity'}
    r = requests.get(f"https://soundcloud.com/{value}",headers=headers)
    requests.get(f"https://soundcloud.com/{value}",headers=headers)
    if r.status_code == 404:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="SoundCloud", url="https://soundcloud.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648397262971469824/soundcloud.png")
        embed.add_field(name= "Available ✅", value= value + " is available on SoundCloud.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="SoundCloud", url="https://soundcloud.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648397262971469824/soundcloud.png")
        embed.add_field(name= "Taken ❌", value= value + " is taken on SoundCloud.", inline=True)
        embed.add_field(name= "Profile", value= "https://soundcloud.com/" + value, inline=True)
        await message.channel.send(embed=embed)

async def steamid(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36, Accept-Encoding, identity'}
    r = requests.get(f"https://steamcommunity.com/id/{value}",headers=headers)
    s = "The specified profile could not be found."
    requests.get(f"https://steamcommunity.com/id/{value}",headers=headers)
    if s in r.text:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="Steam ID", url="https://steamcommunity.com/id/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648402262519185408/steam.png")
        embed.add_field(name= "Available ✅", value= "ID " + value + " is available on Steam.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="Steam ID", url="https://steamcommunity.com/id/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648402262519185408/steam.png")
        embed.add_field(name= "Taken ❌", value= "ID " + value + " is taken on Steam.", inline=True)
        embed.add_field(name= "Profile", value= "https://steamcommunity.com/id/" + value, inline=True)
        
        await message.channel.send(embed=embed)

async def steamgroup(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36, Accept-Encoding, identity'}
    r = requests.get(f"https://steamcommunity.com/groups/{value}",headers=headers)
    g = "No group could be retrieved for the given URL."
    requests.get(f"https://steamcommunity.com/groups/{value}",headers=headers)
    if g in r.text:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="Steam Group", url="https://steamcommunity.com/groups/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648402262519185408/steam.png")
        embed.add_field(name= "Available ✅", value= "Group " + value + " is available on Steam.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="Steam Group", url="https://steamcommunity.com/groups/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648402262519185408/steam.png")
        embed.add_field(name= "Taken ❌", value= "Group " + value + " is taken on Steam.", inline=True)
        embed.add_field(name= "Profile", value= "https://steamcommunity.com/groups/" + value, inline=True)
        await message.channel.send(embed=embed)

async def twitter(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36, Accept-Encoding, identity'}
    r = requests.get(f"https://twitter.com/{value}",headers=headers)
    t = "errorpage-footer"
    t2 = "Account Suspended"
    requests.get(f"https://twitter.com/{value}",headers=headers)
    if t in r.text and t2 not in r.text:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="Twitter", url="https://twitter.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648401267374424064/twitter.png")
        embed.add_field(name= "Available ✅", value= value + " is available on Twitter.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="Twitter", url="https://twitter.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648401267374424064/twitter.png")
        embed.add_field(name= "Taken ❌", value= value + " is taken on Twitter.", inline=True)
        embed.add_field(name= "Profile", value= "https://twitter.com/" + value, inline=True)
        await message.channel.send(embed=embed)

async def instagram(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0, Accept-Encoding, identity'}
    r = requests.get(f"https://www.instagram.com/{value}",headers=headers)
    s = "Page Not Found"
    requests.get(f"https://www.instagram.com/{value}",headers=headers)
    if s in r.text:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="Instagram", url="https://instagram.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648399635664207882/instagramsquare.png")
        embed.add_field(name= "Available ✅", value= value + " is available on Instagram.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="Instagram", url="https://instagram.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648399635664207882/instagramsquare.png")
        embed.add_field(name= "Taken ❌", value= value + " is taken on Instagram.", inline=True)
        embed.add_field(name= "Profile", value= "https://instagram.com/" + value, inline=True)
        await message.channel.send(embed=embed)

async def github(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0, Accept-Encoding, identity'}
    r = requests.get(f"https://www.github.com/{value}",headers=headers)
    s = "Page Not Found"
    requests.get(f"https://www.github.com/{value}",headers=headers)
    if r.status_code == 404:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="GitHub", url="https://www.github.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648478254373797891/GitHub-Mark.png")
        embed.add_field(name= "Available ✅", value= value + " is available on GitHub.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="GitHub", url="https://www.github.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648478254373797891/GitHub-Mark.png")
        embed.add_field(name= "Taken ❌", value= value + " is taken on GitHub.", inline=True)
        embed.add_field(name= "Profile", value= "https://github.com/" + value, inline=True)
        await message.channel.send(embed=embed)

async def weheartit(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0, Accept-Encoding, identity'}
    r = requests.get(f"https://weheartit.com/{value}",headers=headers)
    s = "Page Not Found"
    requests.get(f"https://weheartit.com/{value}",headers=headers)
    if r.status_code == 404:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="WeHeartIt", url="https://weheartit.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648481033544531999/original.png")
        embed.add_field(name= "Available ✅", value= value + " is available on WeHeartIt.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="WeHeartIt", url="https://weheartit.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648481033544531999/original.png")
        embed.add_field(name= "Taken ❌", value= value + " is taken on WeHeartIt.", inline=True)
        embed.add_field(name= "Profile", value= "https://weheartit.com/" + value, inline=True)
        await message.channel.send(embed=embed)

async def lastfm(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0, Accept-Encoding, identity'}
    r = requests.get(f"https://www.last.fm/user/{value}",headers=headers)
    s = "Page Not Found"
    requests.get(f"https://www.last.fm/user/{value}",headers=headers)
    if r.status_code == 404:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="Last.fm", url="https://www.last.fm/user/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648483115496636428/lastfm_avatar_twitter.66cd2c48ce03.png")
        embed.add_field(name= "Available ✅", value= value + " is available on Last.fm.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="Last.fm", url="https://www.last.fm/user/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648483115496636428/lastfm_avatar_twitter.66cd2c48ce03.png")
        embed.add_field(name= "Taken ❌", value= value + " is taken on Last.fm.", inline=True)
        embed.add_field(name= "Profile", value= "https://www.last.fm/user/" + value, inline=True)
        await message.channel.send(embed=embed)

async def youtube(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0, Accept-Encoding, identity'}
    r = requests.get(f"https://www.youtube.com/{value}",headers=headers)
    s = "Page Not Found"
    requests.get(f"https://www.youtube.com/{value}",headers=headers)
    if r.status_code == 404:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="YouTube", url="https://www.youtube.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648485884718743571/de1c91788be0d791135736995109272a.png")
        embed.add_field(name= "Available ✅", value= value + " is available on YouTube.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="YouTube", url="https://www.youtube.com/" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648485884718743571/de1c91788be0d791135736995109272a.png")
        embed.add_field(name= "Taken ❌", value= value + " is taken on YouTube.", inline=True)
        embed.add_field(name= "Profile", value= "https://www.youtube.com/" + value, inline=True)
        await message.channel.send(embed=embed)

async def mastodon(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0, Accept-Encoding, identity'}
    r = requests.get(f"https://mastodon.social/@{value}",headers=headers)
    s = "Page Not Found"
    requests.get(f"https://mastodon.social/@{value}",headers=headers)
    if r.status_code == 404:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="Mastodon", url="https://mastodon.social/@" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648792486029819905/apple-touch-icon.png")
        embed.add_field(name= "Available ✅", value= value + " is available on Mastodon.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="Mastodon", url="https://mastodon.social/@" + value, icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648792486029819905/apple-touch-icon.png")
        embed.add_field(name= "Taken ❌", value= value + " is taken on Mastodon.", inline=True)
        embed.add_field(name= "Profile", value= "https://mastodon.social/@" + value, inline=True)
        await message.channel.send(embed=embed)

async def minecraft(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0, Accept-Encoding, identity'}
    r = requests.get(f"https://namemc.com/name/{value}",headers=headers)
    a = "Available*"
    ua = "Unavailable"
    requests.get(f"https://namemc.com/name/{value}",headers=headers)
    if a in r.text:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="Minecraft", url="https://namemc.com/name/" + value, icon_url="https://cdn.discordapp.com/attachments/648799510897754122/648799701361098793/apps.45782.9007199266731945.debbc4f1-cde0-491b-8c6f-b6b015eecab6.png")
        embed.add_field(name= "Available ✅", value= value + " is available on Minecraft, *unless blocked.*", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="Minecraft", url="https://namemc.com/name/" + value, icon_url="https://cdn.discordapp.com/attachments/648799510897754122/648799701361098793/apps.45782.9007199266731945.debbc4f1-cde0-491b-8c6f-b6b015eecab6.png")
        embed.add_field(name= "Taken ❌", value= value + " is taken on Minecraft.", inline=True)
        #embed.add_field(name= "Profile", value= "https://namemc.com/name/" + value, inline=True)
        await message.channel.send(embed=embed)

async def tumblr(message, value):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0, Accept-Encoding, identity'}
    r = requests.get(f"https://{value}.tumblr.com",headers=headers)
    s = "Page Not Found"
    requests.get(f"https://{value}.tumblr.com",headers=headers)
    if r.status_code == 404:
        embed=discord.Embed(color=0x80ff80)
        embed.set_author(name="Tumblr", url="https://" + value + ".tumblr.com", icon_url="https://cdn.discordapp.com/attachments/649552591839035392/649554287600467979/Tumblr-symbol.jpg")
        embed.add_field(name= "Available ✅", value= value + " is available on Tumblr.", inline=True)
        await message.channel.send(embed=embed)
    else:
        embed=discord.Embed(color=0xe15b5b)
        embed.set_author(name="Tumblr", url="https://" + value + ".tumblr.com", icon_url="https://cdn.discordapp.com/attachments/649552591839035392/649554287600467979/Tumblr-symbol.jpg")
        embed.add_field(name= "Taken ❌", value= value + " is taken on Tumblr.", inline=True)
        embed.add_field(name= "Profile", value= "https://" + value + ".tumblr.com", inline=True)
        await message.channel.send(embed=embed)




@client.event
async def on_message(message):
    print(message.content)
    if "!soundcloud" in message.content:
        left, soundcloud, wordstr = message.content.partition("!soundcloud") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 45:
                await message.channel.send("`SoundCloud URL limit is 45.`")
                return
            else:
                await scloud(message, value)

    elif "!steamgroup" in message.content:
        left, soundcloud, wordstr = message.content.partition("!steamgroup") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 14:
                await message.channel.send("`Steam Group URL limit is 32.`")
                return
            else:            
                await steamgroup(message, value)

    elif "!steam" in message.content:
        if "!steamgroup" in message.content:
            return
        left, soundcloud, wordstr = message.content.partition("!steam") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 14:
                await message.channel.send("`Steam ID limit is 32.`")
                return
            else:        
                await steamid(message, value)



    elif "!instagram" in message.content:
        left, soundcloud, wordstr = message.content.partition("!instagram") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 14:
                await message.channel.send("`Instagram URL limit is 14.`")
                return
            else:
                await instagram(message, value)

    elif "!twitter" in message.content:
        left, soundcloud, wordstr = message.content.partition("!twitter") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 15:
                await message.channel.send("`Twitter URL limit is 15.`")
                return
            else:
                await twitter(message, value)
            
        
    elif "!github" in message.content:
        left, soundcloud, wordstr = message.content.partition("!github") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 24:
                await message.channel.send("`GitHub URL limit is 24.`")
                return
            else:
                await github(message, value)

    elif "!weheartit" in message.content:
        left, soundcloud, wordstr = message.content.partition("!weheartit") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 25:
                await message.channel.send("`WeHeartIt URL limit is 25.`")
                return
            else:
                await weheartit(message, value)

    elif "!lastfm" in message.content:
        left, soundcloud, wordstr = message.content.partition("!lastfm") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 20:
                await message.channel.send("`Last.fm URL limit is 20.`")
                return
            else:
                await lastfm(message, value)

    elif "!youtube" in message.content:
        left, soundcloud, wordstr = message.content.partition("!youtube") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 13:
                await message.channel.send("`YouTube URL limit is 13.`")
                return
            else:
                await youtube(message, value)

    elif "!mastodon" in message.content:
        left, soundcloud, wordstr = message.content.partition("!mastodon") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 8:
                await message.channel.send("`Mastodon URL limit is 8.`")
                return
            else:
                await mastodon(message, value)

    elif "!minecraft" in message.content:
        left, soundcloud, wordstr = message.content.partition("!minecraft") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 16:
                await message.channel.send("`Minecraft name limit is 16.`")
                return
            else:
                await minecraft(message, value)

    elif "!tumblr" in message.content:
        left, soundcloud, wordstr = message.content.partition("!tumblr") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
            if len(value) > 32:
                await message.channel.send("`Tumblr name limit is 32.`")
                return
            else:
                await tumblr(message, value)

    elif "!help" in message.content:
        embed=discord.Embed(color=0x5ba4ec)
        embed.set_author(name="Help", url="https://discord.gg/KTfVx4A", icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648406636884525057/squid_1f991.png")
        embed.add_field(name="!check", value="checks all urls", inline=False)
        embed.add_field(name="!soundcloud", value="checks soundcloud url", inline=False)
        embed.add_field(name="!instagram", value="checks instagram url", inline=False)
        embed.add_field(name="!twitter", value="checks twitter url", inline=False)
        embed.add_field(name="!steam", value="checks steam id", inline=False)
        embed.add_field(name="!steamgroup", value="checks steam group url", inline=False)
        embed.add_field(name="!github", value="checks github url", inline=False)
        embed.add_field(name="!weheartit", value="checks weheartit url", inline=False)
        embed.add_field(name="!lastfm", value="checks last.fm url", inline=False)
        embed.add_field(name="!youtube", value="checks youtube url", inline=False)
        embed.add_field(name="!mastodon", value="checks mastodon url", inline=False)
        embed.add_field(name="!minecraft", value="checks minecraft url", inline=False)
        embed.add_field(name="!tumblr", value="checks tumblr url", inline=False)               
        embed.set_footer(text="made with 💕 by @kiseu#4727")
        await message.author.send(embed=embed)

    elif "!hhelp" in message.content:
        embed=discord.Embed(color=0x5ba4ec)
        embed.set_author(name="Help", url="https://discord.gg/KTfVx4A", icon_url="https://cdn.discordapp.com/attachments/647827325643128900/648406636884525057/squid_1f991.png")
        embed.add_field(name="!check", value="checks all urls", inline=False)
        embed.add_field(name="!soundcloud", value="checks soundcloud url", inline=False)
        embed.add_field(name="!instagram", value="checks instagram url", inline=False)
        embed.add_field(name="!twitter", value="checks twitter url", inline=False)
        embed.add_field(name="!steam", value="checks steam id", inline=False)
        embed.add_field(name="!steamgroup", value="checks steam group url", inline=False)
        embed.add_field(name="!github", value="checks github url", inline=False)
        embed.add_field(name="!weheartit", value="checks weheartit url", inline=False)
        embed.add_field(name="!lastfm", value="checks last.fm url", inline=False)
        embed.add_field(name="!youtube", value="checks youtube url", inline=False)
        embed.add_field(name="!mastodon", value="checks mastodon url", inline=False)
        embed.add_field(name="!minecraft", value="checks minecraft url", inline=False)
        embed.add_field(name="!tumblr", value="checks tumblr url", inline=False)               
        embed.set_footer(text="made with 💕 by @kiseu#4727")
        await message.channel.send(embed=embed)

    elif "!check" in message.content:
        left, soundcloud, wordstr = message.content.partition("!check") 
        words: list = wordstr.split()
        for value in words:
            value = "".join(re.split("[^a-zA-Z0-9_]*", value)) 
        await twitter(message, value)
        await scloud(message, value)
        await instagram(message, value)
        await steamid(message, value)
        await steamgroup(message, value)
        await github(message, value)
        await weheartit(message, value)
        await lastfm(message, value)
        await youtube(message, value)
        await mastodon(message, value)
        await minecraft(message, value)
        await tumblr(message, value)


import os 
client.run('NjQ3Nzc1MDAzMDM0Nzc5NjQ5.Xd-_5w.bouU5Ssubhyv6MejSyW7WsSZLXU')