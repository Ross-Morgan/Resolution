from typing import NamedTuple

_4_3 = (4, 3)
_5_4 = (5, 4)
_16_9 = (16, 9)
_16_10 = (16, 10)
_17_9 = (17, 9)
_21_9 = (21, 9)
_100_171 = (100, 171)


class Size(NamedTuple):
    """Representation of width, height and aspect-ratio of a resolution standard"""
    width: int
    height: int
    aspect_ratio: tuple[int, int]


class Resolution:
    # 4:3 resolutions
    QVGA =      Size(320,  240,  _4_3)
    VGA =       Size(640,  480,  _4_3)
    NTSC_4_3 =  Size(720,  480,  _4_3)
    PAL =       Size(768,  576,  _4_3)
    SVGA =      Size(800,  600,  _4_3)
    XGA =       Size(1024, 768,  _4_3)
    SXGA_plus = Size(1400, 1050, _4_3)
    UXGA =      Size(1600, 1200, _4_3)
    QXGA =      Size(2048, 1536, _4_3)

    # 5:4 resolutions
    SXGA =  Size(1280, 1024, _5_4)
    QSXGA = Size(2560, 2048, _5_4)

    # 16:9 resolutions
    WVGA_16_9 = Size(854,  480,  _16_9)
    HD =        Size(1280, 720,  _16_9)
    FHD =       Size(1920, 1080, _16_9)
    QHD =       Size(2560, 1440, _16_9)
    UHD =       Size(3840, 2160, _16_9)

    # 16:10 resolutions
    CGA =        Size(320,  200,  _16_10)
    WXGA_16_10 = Size(1280, 800,  _16_10)
    WSXGA_plus = Size(1680, 1050, _16_10)
    WUXGA =      Size(1920, 1200, _16_10)
    WQXGA =      Size(2560, 1600, _16_10)

    # 17:9 resolutions
    WVGA_17_9 = Size(800,  480,  _17_9)
    WXGA_17_9 = Size(1280, 768,  _17_9)
    twoK =      Size(2048, 1080, _17_9)

    # 21:9 resolutions
    UWFHD = Size(2560, 1080, _21_9)
    UWQHD = Size(3440, 1440, _21_9)

    # 100:171 resolutions
        # Seriously, why does this exist?
        # I spent an entire 15 seconds on a calculator to find the aspect ratio of this
        # I know why it exists, I just don't want it to
        # But it will never be as awful as 1366 x 786 *insert violent shuddering*
    WSVGA = Size(1024, 600, _100_171)