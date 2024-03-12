from .start.start import start_router
from .math.math import math_router
from .math.math_books import math_books_router
from .math.math_tasks import math_tasks_router
from .programming.programming import programming_router
from .programming.theory import programming_theory_router
from .programming.tasks import programming_tasks_router
from .programming.translator import programming_translator_router
from .history.history import history_router

routers = (
    start_router,
    math_router,
    math_books_router,
    math_tasks_router,
    programming_router,
    programming_tasks_router,
    programming_theory_router,
    programming_translator_router,
    history_router,
)
