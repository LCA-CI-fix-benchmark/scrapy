"""Some debugging functions for working with the Scrapy engine"""
# used in global tests code
from typing import TYPE_CHECKING, Any, List, Tuple

if TYPE_CHECKING:
    from scrapy.core.engine import ExecutionEngine
def get_engine_status(engine: "ExecutionEngine") -> List[Tuple[str, Any]]:
    """Return a report of the current engine status"""
    tests = [
        "time()-engine.start_time",
        "len(engine.downloader.active)",
        "engine.scraper.is_idle()",
        "engine.spider.name",
        "engine.spider_is_idle()",
        "engine.slot.closing",
        "len(engine.slot.inprogress)",
        "len(engine.slot.scheduler.dqs or [])",
        "len(engine.slot.scheduler.mqs)",
        "len(engine.scraper.slot.queue)",
        "len(engine.scraper.slot.active)",
        "engine.scraper.slot.active_size",
        "engine.scraper.slot.itemproc_size",
        "engine.scraper.slot.needs_backout()",
    ]

    checks: List[Tuple[str, Any]] = []
    for test in tests:
        try:
            checks += [(test, eval(test))]
        except Exception as e:
            checks += [(test, f"{type(e).__name__} (exception)")]

    return checks


def format_engine_status(engine: "ExecutionEngine") -> str:
    checks = get_engine_status(engine)
    s = "Execution engine status\n\n"
    for test, result in checks:
        s += f"{test:<47} : {result}\n"
    s += "\n"

    return s


def print_engine_status(engine: "ExecutionEngine") -> None:
    print(format_engine_status(engine))
