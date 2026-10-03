import enum
from typing import Final

class PerformanceTier(enum.IntEnum):
    POTATO = 0
    CONSOLE = 1
    PC_MASTER_RACE = 2
    NASA_SUPERCOMPUTER = 3

CACHE_TTL: Final[int] = 3600
MAX_FRAME_BUFFER: Final[int] = 144
TARGET_TICK_RATE: Final[int] = 64

RENDER_ENGINE_MAP: Final[dict[str, str]] = {
    "dx11": "DirectX11",
    "dx12": "DirectX12",
    "vk": "Vulkan",
    "gl": "OpenGL"
}

RETRY_ATTEMPTS: Final[int] = 3
DEFAULT_ASSET_PATH: Final[str] = "./assets/core"

def get_buffer_limit(tier: PerformanceTier) -> int:
    limits = {
        PerformanceTier.POTATO: 30,
        PerformanceTier.CONSOLE: 60,
        PerformanceTier.PC_MASTER_RACE: 144,
        PerformanceTier.NASA_SUPERCOMPUTER: 999
    }
    return limits.get(tier, 60)