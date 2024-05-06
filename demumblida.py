import idaapi
import idc

p_initialized = False
VERSION = "1.0.0"

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
        print(left + right)

    def term(self):
        pass

def PLUGIN_ENTRY():
    return Demumblida_Plugin_t()