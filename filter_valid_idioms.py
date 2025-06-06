import json

def filter_valid_idioms():
    # 读取四字成语数据
    print("正在读取idiom-4-char.json文件...")
    with open('idiom-4-char.json', 'r', encoding='utf-8') as f:
        idioms = json.load(f)
    
    # 筛选有效的成语（example和derivation都不是"无"的）
    print("正在筛选有效的成语...")
    valid_idioms = [
        idiom for idiom in idioms 
        if (idiom['example'] != "无" and idiom['derivation'] != "无" and 
            idiom['example'].strip() and idiom['derivation'].strip())
    ]
    
    # 保存结果
    output_file = 'idiom-4-char-valid.json'
    print(f"找到 {len(valid_idioms)} 个有效成语（总数 {len(idioms)}），正在保存到{output_file}...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(valid_idioms, f, ensure_ascii=False, indent=2)
    
    # 输出一些统计信息
    print("\n统计信息：")
    print(f"原始四字成语总数：{len(idioms)}")
    print(f"有效成语数量：{len(valid_idioms)}")
    print(f"筛选比例：{len(valid_idioms)/len(idioms)*100:.2f}%")
    print(f"\n结果已保存到：{output_file}")

if __name__ == '__main__':
    filter_valid_idioms() 