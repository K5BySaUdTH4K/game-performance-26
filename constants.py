from enum import Enum, unique

@unique
class PerformanceTier(Enum):
    POTATO = 0
    CONSOLE = 1
    PC_MASTER_RACE = 2

CACHE_LIMIT_MB = 1024
FRAME_TARGETS = {PerformanceTier.POTATO: 30, PerformanceTier.CONSOLE: 60, PerformanceTier.PC_MASTER_RACE: 144}

SHADERS_DIR = "./assets/shaders"
TEXTURE_COMPRESSION_LEVEL = 9

BUFFER_SIZES = (1024, 2048, 4096)

def get_frame_budget(tier: PerformanceTier) -> float:
    """Calculates ms per frame budget based on tier."""
    return 1000.0 / FRAME_TARGETS.get(tier, 30)

GLOBAL_TIMEOUT_SECONDS = 5.5
MAX_CONCURRENT_THREADS = 8

DEBUG_LOG_PATH = "/var/log/game_perf.log"