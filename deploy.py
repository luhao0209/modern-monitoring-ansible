import subprocess
import getpass

print("========================================")
print(" 🚀 欢迎使用自动化部署脚手架 (密码模式)")
print("========================================")

# 1. 捕获用户输入
ip = input("👉 请输入新服务器 IP: ").strip()
# getpass 可以让密码在输入时不显示在屏幕上，防偷窥
password = getpass.getpass("👉 请输入 root 密码: ").strip()

if not ip or not password:
    print("❌ IP 或密码不能为空！")
    exit(1)

# 2. 生成带有明文密码的 inventory.ini
inventory_content = f"""[monitoring_servers]
server_1 ansible_host={ip} ansible_user=root ansible_ssh_pass={password}
"""

with open("inventory.ini", "w") as f:
    f.write(inventory_content)

print(f"✅ 配置已生成，目标: {ip}")
print("⏳ 正在推送至 GitHub 触发自动化流水线...")

try:
    # 3. 自动提交并推送到 GitHub
    subprocess.run(["git", "add", "inventory.ini"], check=True)
    subprocess.run(["git", "commit", "-m", f"Auto deploy to {ip} via password"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    
    print("\n🎉 部署指令已发送！流水线正在执行...")
except Exception as e:
    print(f"\n❌ 推送失败: {e}")
