from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.theory import InlineKeyboards
from filters.chat_type import ChatTypeFilter

programming_theory_router = Router(name='theory')
programming_theory_router.message.filter(ChatTypeFilter(chat_type=["private"]))

# Theory menu
@programming_theory_router.callback_query(F.data == "programming_theory")
async def programming_theory_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
        text= (
        "*Theory*\n\n"
        "In the following section you can choose one of three Soviet programming languages to study\\!"
        ),
        reply_markup=InlineKeyboards().programming_theory(), 
        parse_mode="MarkdownV2")


@programming_theory_router.callback_query(F.data == "theory_refal")
async def refal_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
        text=(
        "*REFAL\\-5*\n\n"
        "REFAL\\-5 \\(Recursive Functions Algorithmic Language\\), 5th iteration of REFAL `\\(1966\\)`, is a functional programming language designed primarily for symbolic data processing\\. It excels in pattern matching, symbolic computation, and string processing, making it a powerful tool for tasks in these domains\\."
        ),
        reply_markup=InlineKeyboards().theory_refal(), 
        parse_mode="MarkdownV2")
    
@programming_theory_router.callback_query(F.data == "refal_intro")
async def refal_intro_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Basic Syntax and Constructs*\n\n"
        "*Expressions:* The basic building blocks in REFAL are expressions, which can be constants, variables, or function applications\.\n\n"
        "*Functions:* Functions in REFAL are defined by specifying patterns for their arguments and corresponding actions\. This pattern matching is what allows for the expressive power of REFAL\.\n\n"
        "*Sequences:* Data in REFAL is often represented as sequences, which can be thought of as lists\. These sequences are manipulated using pattern matching in function definitions\.\n\n"
        "```REFAL-5\n"
        "$ENTRY Go {\n"
        "  = <HelloWorld\\>;\n"
        "}\n\n"
        "HelloWorld {\n"
        "  = 'Hello, World!';\n"
        "}```\n\n"
        "Since REFAL\\-5 is a functional language, naturally, it supports function definition, which can be seen in the code snippet above\."
    ),
    reply_markup=InlineKeyboards().back_to_theory_refal(),
    parse_mode="MarkdownV2"
)

@programming_theory_router.callback_query(F.data == "refal_operators")
async def refal_operators_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Basic operations*\n\n"
        "REFAL\\-5 supports basic arithmetic operations and comparisons\\. For example, \\+, \\-, \\*, \\/, \\>, \\<, \\=, and so on\\."
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_refal()
)
    

@programming_theory_router.callback_query(F.data == "refal_lists")
async def refal_lists_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Lists*\n\n"
        "Creating a list in REFAL\\-5 involves using parentheses `\\(\\)`to denote the list and using a dot \\. to separate the elements\. Lists in REFAL are similar to linked lists, where each element points to the next\. Here's how you can create lists of various lengths and complexities:\n\n"
        "*Empty List:* An empty list is just `\\(\\)`\.\n\n"
        "*Single Element List:* A list with one element, say `a`, is written as:\n"
        "```REFAL-5\n"
        "\\(a \\. \\(\\)\\)\n"
        "```\n"
        "The dot separates the element a from the rest of the list, which is empty in this case\.\n\n"
        "*Two Element List:* A list with elements `a` and `b` looks like:\n"
        "```REFAL-5\n"
        "\\(a \\. \\(b \\. \\(\\)\\)\\)\n"
        "```\n"
        "Here, a is followed by another list containing b\.\n\n"
        "*Multiple Element List:* For more elements, you continue this pattern\. A list with `a`, `b`, and `c` is:\n"
        "```REFAL-5\n"
        "\\(a \\. \\(b \\. \\(c \\. \\(\\)\\)\\)\\)\n"
        "```\n\n"
        "*Nested Lists:* You can also create nested lists\. A list where the first element is `a` and the second element is another list\n"
        "`\\(b \\. \\(c \\. \\(\\)\\)\\)` would be:\n"
        "```REFAL-5\n"
        "\\(a \\. \\(\\(b \\. \\(c \\. \\(\\)\\)\\) \\. \\(\\)\\)\\)\n"
        "```\n"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_refal()
)
    

@programming_theory_router.callback_query(F.data == "refal_patterns")
async def refal_patterns_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Patterns*\n\n"
        "*Simple Patterns:* Match single values or variables\\. For example, `x` in a pattern matches any single value and assigns it to x\\.\n\n"
        "*Compound Patterns:* Involve more complex structures, like sequences or nested patterns\\. For instance, `\\(x \\. y\\)` matches a two\\-element sequence, binding the first element to `x` and the second to `y`\\.\n\n"
        "*Conditional Patterns:* Use conditions to make more sophisticated pattern matches\\. They can include arithmetic operations, comparisons, and more\\.\n\n"
        "*Recursive Patterns:* Allow patterns to include calls to other functions, enabling complex, recursive data processing\\."
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_refal()
)
    
@programming_theory_router.callback_query(F.data == "refal_recursion")
async def refal_recursion_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Recursion*\n\n"
        "Recursion is the fundamental concept of REFAL\\-5, since it's incapable of iteration due to the nature of its functional paradigm\. However, REFAL\\-5 is indeed capable of handling not only simple iterative processes but also complex, nested, or conditional data processing that might be cumbersome with loops\.\n\n"
        "The following code snippet uses a recursive function to compute the factorial of a number:\n"
        "```REFAL-5\n"
        "Factorial {\n"
        "  0 = 1;\n"
        "  n = n \\*<Factorial n \\- 1\\>;\n"
        "}\n"
        "```\n"
        "And this one recursively sums elements of a list:\n"
        "```REFAL-5\n"
        "Sum {\n"
        "  \\(\\) = 0;\n"
        "  \\(e . s\\) = e + <Sum s\\>;\n"
        "}\n"
        "```\n"
        "Doubles a number:\n"
        "```REFAL-5\n"
        "Double {\n"
        "  x = x + x;\n"
        "}\n"
        "```\n"
        "Checks evenness:\n"
        "```REFAL-5\n"
        "IsEven {\n"
        "  0 = true;\n"
        "  \\(1 + x\\) = <IsOdd x\\>;\n"
        "}\n"
        "```\n"
        "Returns list length:\n"
        "```REFAL-5\n"
        "LengthList {\n"
        "  \\(\\) = 0;\n"
        "  \\(x . l\\) = 1 + <LengthList l\\>;\n"
        "}\n"
        "```\n\n"
        "Notice that conditions are widely used\\. For example \\: `if the list is empty, the program returns 0\. Otherwise, it adds the first element of the list to the sum of the rest of the list \\(<Sum s\\>\\)\.`"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_refal()  # Assuming you want to include the back button
)

# el-76 theory begins here
@theory_router.callback_query(F.data == "theory_el76")
async def el76_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
        text=(
        "*El\\-76*\n\n"
        "El\\-76 is a high\\-level programming language developed in `1972\\-1973`\\. The language was created for the Elbrus computer and entirely consists of `Cyrillic` letters\\."
        ),
        reply_markup=InlineKeyboards().theory_el76(), 
        parse_mode="MarkdownV2")


@theory_router.callback_query(F.data == "el76_history")
async def el76_history_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=( 
            "*History of `El\\-76`*\n\n"
            "`El\\-76` is a programming language developed at the _Lebedev Institute of Precision Mechanics and Computer Engineering_ in the `USSR`\\. It was designed by *Boris Babayan* and his team in the early `1970s` for use on the *Elbrus\\-1* computer, one of the earliest Soviet mainframe computers\\. The language's development was part of a larger initiative to create a software ecosystem for *Elbrus* computers, which were among the most powerful computing systems in the `USSR` at the time\\.\n\n"
            "The choice to use _Cyrillic_ characters in `El\\-76's` syntax was driven by the desire to make the language more accessible to programmers in the Soviet Union, where _Cyrillic_ is the standard script\\. This decision reflects a broader trend in Soviet computing to develop technology that catered specifically to the needs and contexts of its users\\.\n\n"
            "Over the years, `El\\-76` was used for various applications, including system programming, scientific computing, and educational purposes\\. Despite its innovative aspects, the language remained relatively unknown outside the Soviet Union and its direct sphere of influence\\.\n\n"
            "Today, `El\\-76` stands as a testament to the rich history of computing in the `USSR` and offers valuable insights into the unique challenges and solutions encountered in the development of computer technology during that era\\."
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_el76(),
)


@theory_router.callback_query(F.data == "el76_syntax")
async def el76_syntax_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Syntax Overview of `El\\-76`*\n\n"
        "`El\\-76`, like any programming language, has its unique syntax that defines how programs are written and structured\\. Here are some peculiarities and key aspects of El\\-76 syntax:\n\n\n"
        "*1\\. Cyrillic Keywords:*\n"
        "`El\\-76` utilizes Cyrillic keywords for its syntax, which is aligned with its development in a Russian\\-speaking context\\. This approach makes the language more intuitive for Cyrillic\\-based language speakers\\. However, latin letters are still allowed for denoting variables\\.\n\n"
        "_Example:_ начало, конец, если, цикл, перемен, процедура\n\n"
        "*2\\. Variable Declaration and Initialization:*\n"
        "`El\\-76` uses specific keywords for declaring variables with a type or changing their values\\.\n\n"
        "_Example 1:_ `перемен ai#чис;`\n"
        "_Example 2:_ `ai := a[I]`\n\n"
        "*3\\. Loops and Conditions:*\n"
        "`El\\-76` supports loop constructs and conditional statements, allowing for complex data processing\\.\n\n"
        "_Example 1:_\n`для і от 1 до длина а \\- 1 цикл ...`\n"
        "_Example 2:_ `если a[j] \\<= ai то ...`\n\n"
        "*4\\. Functions and Procedures:*\n"
        "`El\\-76` allows the definition of functions and procedures for modular and reusable code\\.\n\n"
        "_Example:_\n`процедура сортпр = проц (конст а#тм)`\n\n"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_el76()
)




@theory_router.callback_query(F.data == "el76_operators")
async def el76_operators_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Basic Operators in `El\\-76`*\n\n"
        "`El\\-76` includes several basic operators similar to those found in other programming languages\\.\n\n"
        "*Assignment* `\\(:=\\)`*:*\n"
        "```El-76\n"
        "ai := a[i]\n\n"
        "```\n\n"
        "*Arithmetic Operators:*\n"
        "*Addition* `\\(+\\)`*:*\n"
        "```El-76\n"
        "r := r + 1;\n"
        "```\n"
        "*Subtraction* `\\(\\-\\)`*:*"
        "```El-76\n"
        "r := r - 1;\n"
        "```\n"
        "*Multiplication* `\\(*\\)`*:*\n"
        "```El-76\n"
        "r := r * 10;\n"
        "```\n\n"
        "*Division* `\\(/\\)`*:*"
        "```El-76\n"
        "m[i] := измтип (r/:2, циф);\n"
        "```\n\n"
        "*Comparison Operators:*\n"
        "*Less than or equal to* `\\(<=\\)`*:*"
        "```El-76\n"
        "если a[j] <= ai то найден ! (j)\n\n"
        "```\n\n"
        "*Concatenation* `\\(+\\)`*:*"
        "```El-76\n"
        "s[l] := измтип (\"0\" + m[l], лит);\n\n"
        "```\n\n"
        "*Comment* `\\(%\\)`*:*"
        "```El-76\n"
        "цикл % слева от i-го элемента ищется меньший\n"
        "```\n\n"
        "These examples illustrate how various operators are utilized in `El\\-76` to perform assignments, arithmetic operations, comparisons, concatenations, and comments\\."
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_el76()
)
