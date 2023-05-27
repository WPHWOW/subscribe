import time
import winsound

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"专注时钟已设置为 {minutes} 分钟.")
    time.sleep(seconds)
    frequency = 2500  # 声音频率
    duration = 2000  # 声音持续时间（毫秒）
    winsound.Beep(frequency, duration)
    print("时间到！专注时钟结束.")

# 设置专注时钟的分钟数
focus_minutes = int(input("请输入专注时钟的分钟数: "))
focus_timer(focus_minutes)
