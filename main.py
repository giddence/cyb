import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_b2_value():
    # 设置 Google Sheets API 权限
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # 打开表格（替换为你的 SHEET_ID 和工作表名称）
    sheet = client.open_by_key("1XttIKCNl3-PeZF1Y4-P4hQ-zXo0NMbmPAXQwm53ipS8").worksheet("工作表1")
    b2_value = sheet.acell("B2").value  # 读取 B2 单元格
    print(f"B2 的值: {b2_value}")
    return b2_value

if __name__ == "__main__":
    get_b2_value()
    
import os
import requests

def send_wecom_message(text):
    # 从 GitHub Secrets 获取 Webhook URL
    webhook_url = os.environ.get("WECOM_WEBHOOK_URL")  # 需在 Secrets 中配置

    headers = {"Content-Type": "application/json"}
    data = {
        "msgtype": "text",
        "text": {
            "content": text,
            # 可选：指定@的成员（通过 userid）
            "mentioned_list": ["user1", "user2"]
        }
    }

    response = requests.post(webhook_url, json=data, headers=headers)
    return response.json()

if __name__ == "__main__":
    # 示例：推送 Google Sheets 处理结果
    message = "任务执行成功！表格已更新。"
    result = send_wecom_message(message)
    print("企微机器人响应:", result)
