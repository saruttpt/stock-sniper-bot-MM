import requests
from bs4 import BeautifulSoup
import os

# 1. URL Finviz ของคุณ
url = "https://finviz.com/screener/stocks?v=111&f=cap_smallover%2Cfa_eps3years_pos%2Cfa_pe_profitable%2Cta_rsi_os30"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def run_sniper():
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # ดึงข้อมูลหุ้น (ระบบจำลองตัวอย่างข้อมูลส่งเข้า Make)
        # ตัวอย่างโครงสร้างที่ส่งไปให้ Make.com
        payload = {
            "source": "GitHub Actions Cloud",
            "stocks": [
                {"ticker": "AMD", "price": 135.0, "sma200": 162.0, "rsi": 29.5, "mayer": 0.83},
                {"ticker": "NKE", "price": 72.0, "sma200": 90.0, "rsi": 27.8, "mayer": 0.80}
            ]
        }
        
        # 2. ยิงเข้า Make.com Webhook URL
        webhook_url = "https://hook.eu1.make.com/g71ggxv9v46il69gt6i74roomkkamo2l"
        res = requests.post(webhook_url, json=payload)
        print("Webhook Status:", res.status_code)
        
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    run_sniper()
