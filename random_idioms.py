import json
import random

def create_tiny_idioms(input_file, output_file, sample_size=500):
    # 读取原始JSON文件
    with open(input_file, 'r', encoding='utf-8') as f:
        idioms = json.load(f)
    
    # 确保sample_size不超过原始数据的长度
    sample_size = min(sample_size, len(idioms))
    
    # 随机抽取指定数量的成语
    sampled_idioms = random.sample(idioms, sample_size)
    
    # 将抽取的成语写入新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sampled_idioms, f, ensure_ascii=False, indent=2)
    
    print(f'成功从{len(idioms)}个四字成语中随机抽取{sample_size}个成语')
    print(f'新文件已保存为: {output_file}')

if __name__ == '__main__':
    input_file = 'idiom-4-char.json'
    output_file = 'idiom-4-char-tiny.json'
    create_tiny_idioms(input_file, output_file) 