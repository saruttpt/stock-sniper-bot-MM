import requests

def run_sniper():
    try:
        # ส่งข้อมูลชุดทดสอบตรงไปที่ Make.com ทันทีเพื่อเช็กการเชื่อมต่อ
        payload = {
            "source": "GitHub Test Connection",
            "stocks": [
                {"ticker": "TEST1"},
                {"ticker": "TEST2"}
            ]
        }

        # ใส่ Webhook URL ปัจจุบันของคุณตรงนี้ให้ถูกต้อง
        webhook_url = "https://hook.eu1.make.com/g71ggxv9v46il69gt6i74roomkkamo2l"
        res = requests.post(webhook_url, json=payload)
        print("Webhook Status:", res.status_code)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    run_sniper()
