import json

def filter_4_char_idioms():
    # 读取原始成语数据
    print("正在读取idiom.json文件...")
    with open('idiom.json', 'r', encoding='utf-8') as f:
        idioms = json.load(f)
    
    # 筛选四字成语
    print("正在筛选四字成语...")
    four_char_idioms = [idiom for idiom in idioms if len(idiom['word']) == 4]
    
    # 保存结果
    print(f"找到 {len(four_char_idioms)} 个四字成语，正在保存到idiom-4-char.json...")
    with open('idiom-4-char.json', 'w', encoding='utf-8') as f:
        json.dump(four_char_idioms, f, ensure_ascii=False, indent=2)
    
    print("处理完成！")

if __name__ == '__main__':
    filter_4_char_idioms() 