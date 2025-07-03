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
