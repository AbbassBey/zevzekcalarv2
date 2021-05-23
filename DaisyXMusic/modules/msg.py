# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 Telegram Grupları ve Kanallarının sesli sohbetlerinde müzik çalmak için oluşturulmuş gelişmiş bir botum.\n\n✅ Yardım /help diyebilirsin."
      HELP_MSG = [
        ".",
f"""
**Tekrardan hoşgeldin :D {PROJECT_NAME}

⚪️ {PROJECT_NAME} grubunuzun sesli sohbetinde ve kanal sesli sohbetlerinde müzik çalabilirim.

⚪️ Asistanımın adı >> @{ASSISTANT_NAME}\n\nTalimatlar için ileriye tıklayın**
""",

f"""
**Kurulum**

1) Bot yöneticisi yap (Grup ve cplay kullanıyorsanız kanalda)
2) Sesli sohbet başlatın
3) Bir yönetici tarafından ilk kez /play [şarkı adını] deneyin.
*) Userbot müziğin keyfini çıkardıysa, grubunuza @{ASSISTANT_NAME} eklemeyin ve yeniden deneyin

**Kanal Müzik Çalma için**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group

**Komutlar**

**=>> Şarkı Çalma 🎧**

- /play: YouTube müziğini kullanarak şarkı çalın
- /play [yt url] : Verilen yt url'sini oynat
- /play [reply yo audio]: Yanıtlanan sesi çal
- /dplay: Deezer ile şarkı çal
- /splay: Jio saavn ile şarkı çal

**=>> Çalma komutları ⏯**

- /player:  Ayarlar menüsünü açar.
- /skip: Bir sonraki şarkıya geçer.
- /pause: Şarkıyı durdurur.
- /resume: Durdurulan şarkıyı devam ettirir.
- /end: Müzik botunu kapatır
- /current: Geçerli şarkıyı gösterir
- /playlist: playlist gösterir.
""",
        
f"""
**=>> Kanalda müzik çalma komutları 🛠**

⚪️ Yalnızca bağlantılı grup yöneticileri için:

- /cplay [song name] - istediğin şarkıyı çal
- /cdplay [song name] - deezer ile istediğin şarkıyı çal
- /csplay [song name] - jio saavn ile istediğin şarkıyı çal
- /cplaylist - Şimdi çalma listesini göster
- /cccurrent - Şimdi çalan göster
- /cplayer - müzik çalar ayarları panelini aç
- /cpause - şarkı çalmayı duraklat
- /cresume - şarkı çalmaya devam et
- /cskip - sonraki şarkıyı çal
- /cend - müzik çalmayı durdur
- /userbotjoinchannel - asistanı sohbetinize davet edin

c yerine kanal da kullanılabilir ( /cplay = /channelplay )

⚪️ Bağlı grupta oynamayı sevmiyorsanız:

1) Kanal kimliğinizi alın.
2) Başlığa sahip bir grup oluşturun: Channel Music: your_channel_id
3) Tam izinlere sahip kanal yöneticisi olarak bot ekleyin
4) @{ASSISTANT_NAME} öğesini kanala yönetici olarak ekleyin.
5) Grubunuza komutlar göndermeniz yeterlidir.

""",

f"""
**=>> Ek aralar 🧑‍🔧**

- /admincache: Grubunuzun yönetici bilgilerini günceller. Bot yöneticiyi tanımıyorsa deneyin
- /userbotjoin: @{ASSISTANT_NAME} Userbot'u sohbetinize davet edin

*Player cmd ve /play, /current ve /playlist dışındaki diğer tüm cmd'ler yalnızca grubun yöneticileri içindir.
"""
      ]
