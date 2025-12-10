import os

def mass_replace(root_dir, old_word, new_word):
    """
    在指定目录及其所有子目录中，递归地替换文件内容、文件名和目录名中的特定字符串。

    参数:
    root_dir (str): 操作的根目录。
    old_word (str): 要被替换的旧单词（小写形式）。
    new_word (str): 用于替换的新单词（小写形式）。
    """
    # 构造大小写两种形式的替换对
    old_upper = old_word.upper()
    new_upper = new_word.upper()

    print(f"🚀 开始执行替换操作，请稍候...")
    print(f"根目录: {os.path.abspath(root_dir)}")
    print(f"规则: '{old_word}' -> '{new_word}', '{old_upper}' -> '{new_upper}'")
    print("-" * 50)

    # 使用 os.walk 进行“自下而上”的遍历 (topdown=False)
    # 这至关重要！确保我们先处理文件，再处理包含它们的目录，避免路径混乱。
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):

        # --- 第一步：处理文件内容 ---
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            # 使用 try-except 来优雅地跳过无法读取的二进制文件（如图片、程序等）
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 只有当文件内容包含目标词时才进行修改，减少不必要的文件写入
                if old_word in content or old_upper in content:
                    print(f"📝 正在修改文件内容: {file_path}")
                    new_content = content.replace(old_word, new_word)
                    new_content = new_content.replace(old_upper, new_upper)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

            except UnicodeDecodeError:
                print(f"⚠️  跳过二进制文件: {file_path}")
            except Exception as e:
                print(f"❌ 处理文件内容时发生错误 {file_path}: {e}")

        # --- 第二步：重命名文件 ---
        for filename in filenames:
            if old_word in filename or old_upper in filename:
                new_filename = filename.replace(old_word, new_word)
                new_filename = new_filename.replace(old_upper, new_upper)
                
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, new_filename)
                
                print(f"📄 正在重命名文件: {old_file_path} -> {new_file_path}")
                try:
                    os.rename(old_file_path, new_file_path)
                except Exception as e:
                    print(f"❌ 重命名文件失败 {old_file_path}: {e}")

        # --- 第三步：重命名目录 ---
        # 因为是自下而上遍历，此时 dirpath 里的文件都已处理完毕，可以安全地重命名目录
        for dirname in dirnames:
            if old_word in dirname or old_upper in dirname:
                new_dirname = dirname.replace(old_word, new_word)
                new_dirname = new_dirname.replace(old_upper, new_upper)

                old_dir_path = os.path.join(dirpath, dirname)
                new_dir_path = os.path.join(dirpath, new_dirname)

                print(f"📁 正在重命名目录: {old_dir_path} -> {new_dir_path}")
                try:
                    os.rename(old_dir_path, new_dir_path)
                except Exception as e:
                    print(f"❌ 重命名目录失败 {old_dir_path}: {e}")

    print("-" * 50)
    print("🎉 所有操作执行完毕！")


if __name__ == "__main__":
    # --- 配置区域 ---
    # 定义要操作的根目录，'.' 表示当前目录
    TARGET_DIRECTORY = '.' 
    
    # 定义要替换的单词
    OLD_WORD = "BGD_Aegis_of_the_AsiaPacific"
    NEW_WORD = "BGD_Aegis_of_the_AsiaPacific"

    # --- 执行区域 ---
    # 在执行前，给一个最终确认的机会
    print("🚨 重要提示: 此脚本将直接修改你的文件和目录名！")
    print("强烈建议在执行前备份你的数据！")
    
    # Python 3.x 使用 input
    #confirm = input("你确定要继续吗？ (输入 'yes' 继续): ")
    
    #if confirm.lower() == 'yes':
    mass_replace(TARGET_DIRECTORY, OLD_WORD, NEW_WORD)
    #else:
    #    print("操作已取消。")
