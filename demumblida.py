import idaapi

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
        print("Demumblida plugin is running...")

    def term(self):
        pass

def PLUGIN_ENTRY():
    return Demumblida_Plugin_t()