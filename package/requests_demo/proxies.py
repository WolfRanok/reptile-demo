import random

import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Cookie': 'BAIDUID=FDC94E6D08897017C9BDA37B7682927F:FG=1; BIDUPSID=05C48591C626E5CE264B69C58FAC7E45; BDUSS=kFSWFhrUVJOYURyb0J4M0otSi1OdEJFTFp-TDlXUnRBMC12OXcyTDYxRi1YckJpRVFBQUFBJCQAAAAAAQAAAAEAAABKN1EjxsbSuVlRWQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH7RiGJ-0YhiU; PSTM=1653197404; BD_UPN=13314752; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ZFY=WZDt62awEhs9BN8nmAxMedvC7rmz8nhghgAIaZ4lpcs:C; COOKIE_SESSION=29_3_7_6_15_9_0_1_5_5_0_5_179_7_159_38_1671970868_1671970747_1671970709%7C9%23263032_36_1671970709%7C9; BD_HOME=1; H_PS_PSSID=36552_37974_37647_37517_37910_37623_36921_37872_37948_37938_37953_37902_26350_37788_37881; BDRCVFR[Hp1ap0hMjsC]=mk3SLVN4HKm; delPer=0; PSINO=3; baikeVisitId=547a9003-4d89-4dc7-ab32-53fdbff2cb34; B64_BOT=1; BA_HECTOR=0l8k04ak840k800g2g808hl11hqgevl1i; H_PS_645EC=f08dIUHmIUnsqhZjD%2FyExtFDFT7CTD5riheGmZjq7pIpUxuFhtm14UZ17%2B4DO9EJHo%2BH; BD_CK_SAM=1; shifen[1763008_91638]=1671970745; BCLID=11772016815945600091; BCLID_BFESS=11772016815945600091; BDSFRCVID=NoPOJeC62RB6nA5jmaede7z7qH5GinJTH6ao9nIn3YHUjlQ6JFX-EG0PKU8g0Kub9dAAogKKKgOTHItF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=NoPOJeC62RB6nA5jmaede7z7qH5GinJTH6ao9nIn3YHUjlQ6JFX-EG0PKU8g0Kub9dAAogKKKgOTHItF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tb4O_CIMtKD3H48k-4QEbbQH-UnLqb_LJgOZ04n-ah02bt_lXP6V-tLmbHJEtbo-W23JbnOm3UTdsq76Wh35K5tTQP6rLtJxfnT4KKJxbInbeU5LQ4KBbM_FhUJiBMnMBan7a4bIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_9D6KhjjJ-epJf-K63KC5QBRj85bT2KROvhjRdQj0gyxomtjDJBDbl-Ub_aRjqqbK626JabtTX0n3nLUkqKCOAaR7DBh6sMxcIQjJaMP5XQttjQUrOfIkja-5tWRvMsR7TyURvbU47y-rJ0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRLeoIPafCt5hDvPKITD-tFO5eT22-us-2JJ2hcHMPoosItwK6QcM4u_bq3-tbIf-CTia-bxKMbUoqRHXnJi0btQDPvxBf7pK2kO_l5TtUJMb-3T3q6P-6FOLtQyKMniWKv9-pnYbpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDT0WjjcQDNLs5JtXKD600PK8Kb7VbpnTQxnkbJkXhPtjqRDDBKQL3R5J5C30MPjNyURM0-t7Qbrr0xRfyNReQIO13hcdSROje5opQT8r5a7fKhQz3Du80pjpab3vOpvTXpO1yJ0zBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjtjfnI8oI8hf-csjJ6pMbOMKKCShUFsWtRTB2Q-5KL-Lq_-DlDGM4cHbt08jpCfbxkt3K5XafbdJJjobJrVh6bZyhLqhbLqBf5vHmTxoUJcQCnJhhvG-6rfLf_ebPRiB-b9QgbALpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHj-Mj6Q03f; H_BDCLCKID_SF_BFESS=tb4O_CIMtKD3H48k-4QEbbQH-UnLqb_LJgOZ04n-ah02bt_lXP6V-tLmbHJEtbo-W23JbnOm3UTdsq76Wh35K5tTQP6rLtJxfnT4KKJxbInbeU5LQ4KBbM_FhUJiBMnMBan7a4bIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_9D6KhjjJ-epJf-K63KC5QBRj85bT2KROvhjRdQj0gyxomtjDJBDbl-Ub_aRjqqbK626JabtTX0n3nLUkqKCOAaR7DBh6sMxcIQjJaMP5XQttjQUrOfIkja-5tWRvMsR7TyURvbU47y-rJ0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRLeoIPafCt5hDvPKITD-tFO5eT22-us-2JJ2hcHMPoosItwK6QcM4u_bq3-tbIf-CTia-bxKMbUoqRHXnJi0btQDPvxBf7pK2kO_l5TtUJMb-3T3q6P-6FOLtQyKMniWKv9-pnYbpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDT0WjjcQDNLs5JtXKD600PK8Kb7VbpnTQxnkbJkXhPtjqRDDBKQL3R5J5C30MPjNyURM0-t7Qbrr0xRfyNReQIO13hcdSROje5opQT8r5a7fKhQz3Du80pjpab3vOpvTXpO1yJ0zBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqjtjfnI8oI8hf-csjJ6pMbOMKKCShUFsWtRTB2Q-5KL-Lq_-DlDGM4cHbt08jpCfbxkt3K5XafbdJJjobJrVh6bZyhLqhbLqBf5vHmTxoUJcQCnJhhvG-6rfLf_ebPRiB-b9QgbALpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHj-Mj6Q03f; ab_sr=1.0.1_M2QxMjEzZjVlMGJiY2M3NjQ0NTg0NmM0M2QyNDljMTI3NzMwMTc5Y2FjMWE0YTkyMWIxYWQxMDMxNDJmMWZjMDMwNDlkMTg2NjhmMmFmNTg1Y2RmMjA4YWU0YTA4YWRmNmZlYTZiMDk3NGQwMzdmZGMxMzU3ZDFhNjFhOTE2MzQyMjJlNDI1YjgwNDBhZTY2OTU5MzEwNjgzZGNkZjQ0Yw==; shifen[353782017477_3302]=1671970711; shifen[324252443258_68419]=1671970739; shifen[353811924966_64982]=1671970746',

}

data = {
    'wd': 'ip'
}
# url?????????????????????????????????????????????????????????
proxies_list = [
    {'https': '120.24.76.81:8123'},
]

proxies = random.choice(proxies_list)


with requests.get(url=url, headers=headers, params=data,proxies=proxies) as response:
    content = response.text

with open('dates/baidu.html', 'w', encoding='utf-8') as f:
    f.write(content)
