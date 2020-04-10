import psutil
import time
import datetime


def close_pid_by_process_name(process_name_list, over_hour):
    ps_list = psutil.pids()
    for ps_pid in ps_list:
        try:
            ps_info = psutil.Process(ps_pid)
            ps_name = ps_info.name().lower()
            ps_create_time = ps_info.create_time()
            if ps_name in process_name_list:
                print("======================start======================")
                over_time = (datetime.datetime.now() - datetime.timedelta(hours=over_hour)).timestamp()
                ps_time_info = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ps_create_time))
                over_time_info = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(over_time))
                print("process id is: [ " + str(ps_pid) + " ]")
                print("process name is: [ " + ps_name + " ]")
                print("create time is: [ " + ps_time_info + " ]")
                print("over time is: [ " + over_time_info + " ]")
                if over_time > ps_create_time:
                    ps_info.terminate()
                    ps_info.wait(timeout=3)
                    print("process kill is successful...")
                print("====================== end ======================\n")
        except Exception as e:
            print("process kill is failed, ", e)
            print("====================== end ======================\n")


if __name__ == "__main__":
    print("程序执行开始")
    print("==========================================================================================================")
    print("温馨提示： 进程名称列表以\"|\"分隔(例如： winword.exe|excel.exe|powerpnt.exe), 超时时间以小时为单位(例如： 1)")
    print("==========================================================================================================")
    process_list_input = input("请输入需要监控的进程名称列表： ")
    over_time_input = int(input("请输入进程超时的时间： "))
    process_list = process_list_input.split("|")
    while True:
        close_pid_by_process_name(process_list, over_time_input)
        time.sleep(5)
