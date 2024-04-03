import subprocess
import time

# 设置要运行的命令
command = "./ore --keypair keypair.json --rpc https://api.mainnet-beta.solana.com mine "
# 设置检查频率，每秒检查一次
check_interval = 1

def is_ore_running():
    try:
        # 使用 pgrep 检查 'ore' 进程是否存在
        subprocess.run(["pgrep", "-f", command], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        # pgrep 会在找不到进程时返回非零状态
        return False

def start_ore():
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    while True:
        if not is_ore_running():
            print("ore process not found, starting...")
            start_ore()
        else:
            print("ore process is running...")
        time.sleep(check_interval)