import pandas as pd
import json
from pathlib import Path

EXCEL_FILE = "resources.xlsx"
JSON_FILE = Path("data.json")

def excel_to_json():
    # 读取 Excel
    df = pd.read_excel(EXCEL_FILE)

    data = {}

    for _, row in df.iterrows():
        resource_id = str(row["id"]).strip()
        title = str(row["资源名称"]).strip()
        code = str(row["中文口令"]).strip()

        if not resource_id:
            continue

        data[resource_id] = {
            "title": title,
            "code": code
        }

    # 写入 data.json（全量覆盖，最安全）
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"已生成 {len(data)} 条资源到 data.json")

if __name__ == "__main__":
    excel_to_json()
