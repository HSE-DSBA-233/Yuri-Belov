from .start.start import start_router
from .math.math import math_router
from .programming.programming import programming_router
from .history.history import history_router
from .programming.theory import theory_router
from .math.math_books import math_books_router
from .math.math_tasks import math_tasks_router
routers = (
    start_router,
    math_router,
    math_books_router,
    math_tasks_router,
    programming_router,
    history_router,
    theory_router
)