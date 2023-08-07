# esp-bin2elf written by Joel Sandin <jsandin@gmail.com>
#
# MIT licence

def get_bootrom_contents():
    return open('bootrom.bin', 'rb').read()

# boomrom symbols are listed here:
# https://github.com/espressif/ESP8266_RTOS_SDK/blob/master/ld/eagle.rom.addr.v6.ld

symbols = {
    b'SPI_sector_erase':   0x400040c0,
    b'SPI_page_program':   0x40004174,
    b'SPI_read_data':      0x400042ac,
    b'SPI_read_status':    0x400043c8,
    b'SPI_write_status':   0x40004400,
    b'SPI_write_enable':   0x4000443c,
    b'Wait_SPI_Idle':      0x4000448c,
    b'Enable_QMode':       0x400044c0,
    b'Disable_QMode':      0x40004508,

    b'Cache_Read_Enable':  0x40004678,
    b'Cache_Read_Disable': 0x400047f0,

    b'lldesc_build_chain': 0x40004f40,
    b'lldesc_num2link':    0x40005050,
    b'lldesc_set_owner':   0x4000507c,

    b'__adddf3':           0x4000c538,
    b'__addsf3':           0x4000c180,
    b'__divdf3':           0x4000cb94,
    b'__divdi3':           0x4000ce60,
    b'__divsi3':           0x4000dc88,
    b'__extendsfdf2':      0x4000cdfc,
    b'__fixdfsi':          0x4000ccb8,
    b'__fixunsdfsi':       0x4000cd00,
    b'__fixunssfsi':       0x4000c4c4,
    b'__floatsidf':        0x4000e2f0,
    b'__floatsisf':        0x4000e2ac,
    b'__floatunsidf':      0x4000e2e8,
    b'__floatunsisf':      0x4000e2a4,
    b'__muldf3':           0x4000c8f0,
    b'__muldi3':           0x40000650,
    b'__mulsf3':           0x4000c3dc,
    b'__subdf3':           0x4000c688,
    b'__subsf3':           0x4000c268,
    b'__truncdfsf2':       0x4000cd5c,
    b'__udivdi3':          0x4000d310,
    b'__udivsi3':          0x4000e21c,
    b'__umoddi3':          0x4000d770,
    b'__umodsi3':          0x4000e268,
    b'__umulsidi3':        0x4000dcf0,

    b'bzero':              0x40002ae8,
    b'memcmp':             0x400018d4,
    b'memcpy':             0x400018b4,
    b'memmove':            0x400018c4,
    b'memset':             0x400018a4,

    b'strcmp':             0x40002aa8,
    b'strcpy':             0x40002a88,
    b'strlen':             0x40002ac8,
    b'strncmp':            0x40002ab8,
    b'strncpy':            0x40002a98,
    b'strstr':             0x40002ad8,
}
