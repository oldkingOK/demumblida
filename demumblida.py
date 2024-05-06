import idaapi
import idc
import subprocess
import os
import ida_diskio
import shutil

p_initialized = False
VERSION = "1.0.0"
RES_EXE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "demumblida_util", 'demumble.exe')
TARGET_EXE = os.path.join(ida_diskio.get_user_idadir(), "plugins", "demumblida_util", 'demumble.exe')

def run_exe(s: str):
    return subprocess.run([TARGET_EXE, s], capture_output=True, text=True, shell=True).stdout.replace("\n", "")

def trans(s: str):
    # user_dir = ida_diskio.get_user_idadir()
    # ida_diskio.getsysfile()
    result = run_exe(s)
    if result == s:
        print(f"<<< {s[:-2]}")
        result = run_exe(s[:-2])
    return result

class Demumblida_Plugin_t(idaapi.plugin_t):
    flags = idaapi.PLUGIN_KEEP
    comment = "Use demumble in IDA Pro"
    help = "This is help"
    wanted_name = "Demumblida"
    wanted_hotkey = "Ctrl-Alt-D"

    def init(self):
        global p_initialized

        if p_initialized is False:
            p_initialized = True
            print("=" * 80)
            print("Demumblida v{0} by oldkingOK, 2024".format(VERSION))
            print("=" * 80)
            # 复制可执行文件到用户目录
            if not os.path.exists(RES_EXE):
                raise Exception("demumble.exe not found")
            os.makedirs(os.path.dirname(TARGET_EXE), exist_ok=True)
            shutil.copy(RES_EXE, TARGET_EXE)

        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        # print("Demumblida plugin is running...")
        s = idc.generate_disasm_line(idc.here(),0)
        loc = idaapi.get_cursor()[1] # 拿到坐标
        # 提取光标左右两边的字符串——函数名
        left_loc = s.rfind(" ", 0, loc)
        left = s[left_loc+1:loc]
        if (right_loc := s.find(";", loc)) != -1:
            pass
        elif (right_loc := s.find(" ", loc)) != -1:
            pass
        else:
            right_loc = len(s)
        right = s[loc:right_loc]
        s = left + right
        print(f"<<< {s}")
        print(f">>> {trans(s)}")

    def term(self):
        pass

def PLUGIN_ENTRY():
    return Demumblida_Plugin_t()