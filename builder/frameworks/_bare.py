from SCons.Script import Import
from os.path import join

Import("env")

board = env.BoardConfig()

target_map = join("${BUILD_DIR}", "${PROGNAME}.map")

env.Append(
    ASFLAGS=[
        "-march=%s" % board.get("build.march"),
        "-mabi=%s" % board.get("build.mabi"),
        "-mcmodel=%s" % board.get("build.mcmodel"),
    ],

    ASPPFLAGS=[
        "-x", "assembler-with-cpp",
    ],

    CCFLAGS=[
        "-Os",
        "-Wall",
        "-march=%s" % board.get("build.march"),
        "-mabi=%s" % board.get("build.mabi"),
        "-mcmodel=%s" % board.get("build.mcmodel"),
        "-fmessage-length=0",
        "-fsigned-char",
        "-ffunction-sections",
        "-fdata-sections",
        "-fno-common"
    ],

    CFLAGS = [
        "-std=gnu11"
    ],

    CXXFLAGS = [
        "-std=gnu++17"
    ],

    CPPDEFINES = [
        "USE_STDPERIPH_DRIVER",
        ("HXTAL_VALUE", "%sU" % board.get("build.hxtal_value"))
    ],

    LINKFLAGS=[
        "-march=%s" % board.get("build.march"),
        "-mabi=%s" % board.get("build.mabi"),
        "-mcmodel=%s" % board.get("build.mcmodel"),
        "-nostartfiles",
        "-Xlinker",
        "--gc-sections",
        "--specs=nano.specs",
        "-Wl,-Map,%s" % target_map
        # "-Wl,--wrap=_exit",
        # "-Wl,--wrap=close",
        # "-Wl,--wrap=fatat",
        # "-Wl,--wrap=isatty",
        # "-Wl,--wrap=lseek",
        # "-Wl,--wrap=read",
        # "-Wl,--wrap=sbrk",
        # "-Wl,--wrap=stub",
        # "-Wl,--wrap=write_hex",
        # "-Wl,--wrap=write"
    ],

    LIBS=["c"]
)
