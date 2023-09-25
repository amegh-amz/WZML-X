#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '🛠️ Updates'
    ST_BN1_URL = 'https://t.me/+ksiDKBExcXVmYTU1'
    ST_BN2_NAME = '😘 Use Me'
    ST_BN2_URL = 'https://t.me/+ksiDKBExcXVmYTU1'
    ST_MSG = '''<b>✨ MT ➔ Mirror & Leech</b>\n\nℹ️ I Can Upload Files, Links, Torrents, etc. to Telegram, Google Drive, DDL Servers and Rclone Supported Sites!\n\n'''
    ST_BOTPM = '''<b>🕵️ Bot PM Initiated Successfully!\n\nℹ️ I will send all your files and links here.</b>'''
    ST_UNAUTH = '''<b>⚠️ Access Denied!</b>'''
    # ---------------------

    # async def stats(client, message):
    BOT_STATS = '''<b>🤖 <u>𝘽𝙤𝙩 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>
    
<b>⏰ Bot Uptime :</b> {bot_uptime}

┎<b>💽 RAM</b>
┠{ram_bar} » ({ram}%)
┖<b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎<b>👒 SWAP</b>
┠{swap_bar} » ({swap}%)
┖<b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎<b>📦 DISK</b>
┠{disk_bar} » ({disk}%)
┠<b>Total Disk Read :</b> {disk_read}
┠<b>Total Disk Write :</b> {disk_write}
┗<b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}

<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>
    
    '''
    SYS_STATS = '''<b>🛠 <u>𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>
    
┏<b>⏰ OS Uptime :</b> {os_uptime}
┠<b>☢️ OS Info :</b> {os_version}
┗<b>🔧 OS Arch :</b> {os_arch}

┏<b>🖥️ CPU</b>
┠{cpu_bar} » ({cpu}%)
┠<b>Frequency :</b> {cpu_freq}
┠<b>Average Load :</b> {sys_load}
┠<b>P-Cores :</b> {p_core} | <b>V-Cores :</b> {v_core}
┠<b>Total Cores :</b> {total_core}
┗<b>Usable CPUs :</b> {cpu_use}

┏<b>📶 Network Stats</b>
┠<b>Upload Data:</b> {up_data}
┠<b>Download Data:</b> {dl_data}
┠<b>Pkts Sent:</b> {pkt_sent}k
┠<b>Pkts Received:</b> {pkt_recv}k
┗<b>Total I/O Data:</b> {tl_data}

<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>
    '''
    REPO_STATS = '''<b>🧑‍💻 <u>𝙍𝙚𝙥𝙤 𝙎𝙩𝙖𝙩𝙞𝙨𝙩𝙞𝙘𝙨</u></b>
    
┏<b>♻️ Bot Updated :</b> {last_commit}
┠<b>🆔 Current Version :</b> {bot_version}
┠<b>🎈 Latest Version :</b> {lat_version}
┗<b>📝 ChangeLog :</b> {commit_details}

<b>💥 REMARKS :</b> <code>{remarks}</code>

<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>
    '''
    BOT_LIMITS = '''<b>❗<u>𝘽𝙤𝙩 𝙇𝙞𝙢𝙞𝙩𝙨</u></b>
    
┏<b>🎯 Direct :</b> <code>{DL} GB</code>
┠<b>🧲 Torrent :</b> <code>{TL} GB</code>
┠<b>☁️ GDrive :</b> <code>{GL} GB</code>
┠<b>📺 YT-DLP :</b> <code>{YL} GB</code>
┠<b>🎥 Playlist :</b> <code>{PL} Videos</code>
┠<b>Ⓜ️ Mega :</b> <code>{ML} GB</code>
┠<b>🎗️ Clone :</b> <code>{CL} GB</code>
┗<b>📂 Leech :</b> <code>{LL} GB</code>

┏<b>🔑 Token Validity :</b> {TV}
┠<b>🐢 Timeout :</b> {UTI}
┠<b>👤 User Tasks :</b> {UT}
┗<b>🚧 Total Tasks :</b> {BT}

<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<b>🔄 Restarting...</b>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<b>♻️ Restarted Successfully! 🎉</b>

┏<b>📅 Date:</b> {date}
┠<b>⏰ Time:</b> {time}
┠<b>🌍 TimeZone:</b> {timz}
┗<b>🆔 Version:</b> {version}

<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>'''
    RESTARTED = '''<b>🔄 Bot Restarted!</b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<b>🙄 Starting Ping...</b>'
    PING_VALUE = '<b>🏓 Pong:</b> <code>{value}ms</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b>🚧 Task Started</b>

┏<b>💠 Mode:</b> {Mode}
┗<b>👤 User:</b> {Tag}\n\n"""
    LINKS_SOURCE = """┏<b>💡 Source:</b>
┗<b>⏰ Time:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    L_PM_START =            "🏁 <b><u>Leech Started</u> :</b>\n\n<b>💡 Source :</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "🏁 <b><u>Leech Started</u> :</b>\n\n┏<b>👤 User :</b> {mention}\n┠<b>🆔 ID :</b> <code>{uid}</code>\n┗<b>💡 Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '┏<b>🏷️ Name:</b> <code>{Name}</code>\n'
    SIZE =                  '┠<b>💾 Size: </b>{Size}\n'
    ELAPSE =                '┠<b>⌛ Elapsed: </b>{Time}\n'
    MODE =                  '┠<b>💠 Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠<b>📂 Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '┠<b>💀 Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '┗<b>👤 User: </b>{Tag}\n\n'
    PM_BOT_MSG =            'ℹ️ <b><i>Files have been Sent Above!</i></b>'
    L_BOT_MSG =             'ℹ️ <b><i>Files have been Sent in Bot PM!</i></b>'
    L_LL_MSG =              'ℹ️ <b><i>Files have been Sent. Access via Links!</i></b>'
    
    # ----- MIRROR -------
    M_TYPE =                '┠<b>📜 Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '┠<b>🗂️ SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '┠<b>📂 Files: </b>{Files}\n'
    RCPATH =                '┠<b>🚩 Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '┗<b>👤 User: </b>{Tag}\n\n'
    M_BOT_MSG =             '🏁 <b><i>Links have been Sent in DM!</i></b>'
    
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📩 Save'
    RCLONE_LINK =     '®️ RClone Link'
    DDL_LINK =        '🚀 {Serv} Link'
    SOURCE_URL =      '💡 Source'
    INDEX_LINK_F =    '🚀 Index Link'
    INDEX_LINK_D =    '🚀 Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '🕵️ View in Bot PM'
    CHECK_LL =        '📦 View in Dump'
    MEDIAINFO_LINK =  '📜 MediaInfo'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '┏<b>🏷️ Name:</b> <code>{Name}</code>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┠{Bar}'
    PROCESSED =         '\n┠<b>🔄 Process:</b> <code>{Processed}</code>'
    STATUS =            '\n┠<b>✨ Status:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ETA:</b> <code>{Eta}</code>'
    SPEED =             '\n┠<b>📶 Speed:</b> <code>{Speed}</code>'
    ELAPSED =                                     ' | <b>Elapsed:</b> <code>{Elapsed}</code>'
    ENGINE =            '\n┠<b>⚙️ Engine:</b> <code>{Engine}</code>'
    STA_MODE =          '\n┠<b>💠 Mode:</b> {Mode}'
    SEEDERS =           '\n┠<b>🌱:</b> <code>{Seeders}</code> | '
    LEECHERS =                                           '<b>🪢:</b> <code>{Leechers}</code>'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠<b>💾 Size:</b> <code>{Size}</code>'
    SEED_SPEED =     '\n┠<b>📶 Speed:</b> <code>{Speed}</code> | '
    UPLOADED =                                     '<b>Uploaded:</b> <code>{Upload}</code>'
    RATIO =          '\n┠<b>🌀 Ratio:</b> <code>{Ratio}</code> | '
    TIME =                                         '<b>Time:</b> <code>{Time}</code>'
    SEED_ENGINE =    '\n┠<b>⚙️ Engine:</b> <code>{Engine}</code>'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠<b>💾 Size:</b> <code>{Size}</code>'
    NON_ENGINE =     '\n┠<b>⚙️ Engine:</b> <code>{Engine}</code>'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠<b>👤 User:</b> <code>{User}</code>'
    ID =                                                        '\n┠<b>🆔 ID:</b> <code>{Id}</code>'
    BTSEL =          '\n┠<b>✂️ Select:</b> {Btsel}'
    CANCEL =         '\n┗<b>🚫 Stop:</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⌬ <b><u>Bot Stats</u></b>\n'
    TASKS =  '┏<b>🚧 Tasks:</b> {Tasks}\n'
    BOT_TASKS = '┏<b>🚧 Tasks:</b> <code>{Tasks}/{Ttask}</code> | <b>👷 Available:</b> <code>{Free}</code>\n'
    Cpu = '┏<b>🖥️ CPU:</b> <code>{cpu}%</code> | '
    FREE =                      '<b>📭 Free:</b> <code>{free}</code>'
    Ram = '\n┠<b>💿 RAM:</b> <code>{ram}%</code> | '
    uptime =                     '<b>⏰ Uptime:</b> <code>{uptime}</code>'
    DL = '\n┗<b>🔻 DL:</b> <code>{DL}/s</code> | '
    UL =                        '<b>🔺 UL:</b> <code>{UL}/s</code>'

    ###--------BUTTONS-------
    PREVIOUS = '⏪'
    REFRESH = '📑 Page: {Page}'
    NEXT = '⏭️'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = '<b>🏷️ Name:</b> <code>{content}</code>\n<b>⚠️ This File/Folder is already available in Drive!</b>\n\n<b>📑 List Results:</b>'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>🎲 Counting:</b> <code>{LINK}</code>\n\n<b>⏳ Please Wait...</b>'
    COUNT_NAME = '┏<b>🏷️ Name:</b> <code>{COUNT_NAME}</code>\n'
    COUNT_SIZE = '┠<b>💾 Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠<b>📜 Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠<b>🗂️ SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠<b>📂 Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┗<b>👤 User: </b>{COUNT_CC}\n\n<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>🔍 Searching:</b> <code>{NAME}</code>'
    LIST_FOUND = '<b>ℹ️ Found {NO} Results For</b> <code>{NAME}</code>'
    LIST_NOT_FOUND = '<b>☹️ No Results Found For</b> <code>{NAME}</code>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<b>💩 No Active Tasks!</b>
    
⌬ <b><u>Bot Stats</u></b>
┏<b>🖥️ CPU:</b> <code>{cpu}%</code> | <b>💿 RAM:</b> <code>{ram}%</code>
┗<b>📭 Free:</b> <code>{free}</code> | <b>⏰ Uptime:</b> <code>{uptime}</code>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>User Settings</u></b>
        
┏<b>👤 Name :</b> {NAME}
┠<b>🔖 Username :</b> {USERNAME}
┠<b>🆔 ID :</b> <code>{ID}</code>
┠<b>🔮 DC :</b> <code>{DC}</code>
┗<b>🗣️ Language :</b> <code>{LANG}</code>

<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>'''

    UNIVERSAL = '''㊂ <b><u>Universal</u></b>

┏<b>📺 YT-DLP Options :</b> <code>{YT}</code>
┠<b>🚧 Daily Tasks :</b> <code>{DT}</code> per day
┠<b>🟢 Last Used :</b> <code>{LAST_USED}</code>
┠<b>📜 MediaInfo :</b> <code>{MEDIAINFO}</code>
┠<b>🕵️ Bot PM :</b> <code>{BOT_PM}</code>
┗<b>📩 Save Mode :</b> <code>{SAVE_MODE}</code>

<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>'''

    MIRROR = '''㊂ <b><u>Mirror/Clone</u></b>

┏<b>☁️ Daily Mirror :</b> <code>{DM}</code> per day</i>
┠<b>Ⓟ Prefix :</b> <code>{MPREFIX}</code>
┠<b>Ⓢ Suffix :</b> <code>{MSUFFIX}</code>
┠<b>🌈 Remname :</b> <code>{MREMNAME}</code>
┠<b>🧿 DDL Server(s) :</b> <code>{DDL_SERVER}</code>
┠<b>🎀 RClone :</b> <code>{RCLONE}</code>
┠<b>📮 User TD :</b> <code>{TMODE}</code>
┗<b>📝 TD Info:</b> <code>{USERTD}</code>

<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>'''

    LEECH = '''㊂ <b><u>Leech Settings</u></b>

┏<b>📂 Daily Leech  : </b><code>{DL}</code> per day
┠<b>⚙️ Leech Type :</b> <code>{LTYPE}</code>
┠<b>🖼️ Thumbnail :</b> <code>{THUMB}</code>
┠<b>♈ Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b>♐ Equal Splits :</b> <code>{EQUAL_SPLIT}</code>
┠<b>♒ Media Group :</b> <code>{MEDIA_GROUP}</code>
┠<b>📄 Caption :</b> <code>{LCAPTION}</code>
┠<b>Ⓟ Prefix :</b> <code>{LPREFIX}</code>
┠<b>Ⓢ Suffix :</b> <code>{LSUFFIX}</code>
┠<b>📦 Dump :</b> <code>{LDUMP}</code>
┗<b>🌈 Remname :</b> <code>{LREMNAME}</code>

<a href="https://t.me/+ksiDKBExcXVmYTU1"><b>♥️ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 MT LEECH</b></a>'''