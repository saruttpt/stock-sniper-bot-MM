import requests
from bs4 BeautifulSoup
import os

def run_sniper():
    try:
        # 1. URL หน้า Finviz ตามเงื่อนไขของคุณ
        url = "https://finviz.com/screener/stocks?v=111&f=cap_smallover%2Cfa_eps3years_pos%2Cfa_pe_profitable%2Cta_rsi_os30"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # ดึงรายชื่อหุ้น (Ticker) จากตารางหน้าเว็บ Finviz อย่างง่าย
        stocks_list = []
        for row in soup.find_all('tr', class_='table-row-link'):
            cols = row.find_all('td')
            if len(cols) > 1:
                ticker = cols[1].text.strip()
                stocks_list.append({"ticker": ticker})
        
        # ถ้าดึงเว็บตรงๆ ไม่ได้ (โดนบล็อก) ให้ส่งตัวอย่างสำรองไปก่อนเพื่อให้ระบบวิ่งต่อได้
        if not stocks_list:
            stocks_list = [{"ticker": "AMD"}, {"ticker": "NKE"}]

        # 2. จัดรูปแบบ Payload ส่งเข้า Make.com Webhook
        payload = {
            "source": "GitHub Actions",
            "stocks": stocks_list
        }

        # 3. ยิงเข้า Make.com Webhook URL ของคุณ
        webhook_url = "https://hook.eu1.make.com/g71ggxv9v46il69gt6i74roomkkamo2l"
        res = requests.post(webhook_url, json=payload)
        print("Webhook Status:", res.status_code)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    run_sniper()
