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
@programming_theory_router.callback_query(F.data == "theory_el76")
async def el76_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
        text=(
        "*El\\-76*\n\n"
        "El\\-76 is a high\\-level programming language developed in `1972\\-1973`\\. The language was created for the Elbrus computer and entirely consists of `Cyrillic` letters\\."
        ),
        reply_markup=InlineKeyboards().theory_el76(), 
        parse_mode="MarkdownV2")


@programming_theory_router.callback_query(F.data == "el76_history")
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


@programming_theory_router.callback_query(F.data == "el76_syntax")
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




@programming_theory_router.callback_query(F.data == "el76_operators")
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


@programming_theory_router.callback_query(F.data == "el76_examples")
async def el76_examples_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
        text=(
            "*Examples of code in `El\\-76`*\n\n"
            "*Example 1: Working with Loops\\. Calculating the Sum*\n"
            "```El-76\n"
            "начало\n"
            "\tконст печ = позп (ацпу);\n"
            "\tпроцедура h = функция (конст к#цел)#вещ \n"
            "\t\tначало\n"
            "\t\tперемен сум#вещ := минвещ;\n"
            "\t\tдля і от к вниздо 1\n"
            "\t\tцикл\n"
            "\t\t\tсум:= сум + 1/і\n"
            "\t\tповторить;\n"
            "\t\tсум\n"
            "\tконец;\n"
            "\tзапф (печ, h(10): \"сумма=\" g (0, 13)\n"
            "конец\n"
            "```\n"
            "This example demonstrates a function h that calculates the harmonic sum\\. The loop iterates over a range decreasing from `к` to 1, accumulating the sum of 1/і at each step\\.\n\n"
            "*Example 2: Exiting a Loop with a Value and Situation*\n"
            "```El-76\n"
            "начало\n"
            "\tконст печ = позп (ацпу);\n"
            "\tпроцедура возвстеп = функция (конст и#чис, ве#цел) #чис\n"
            "\tдо исчерпстеп\n"
            "\tцикл перемен z#чис := 1, v#чис := u, e#цел := ee;\n"
            "\t\tесли e = 0 то исчерпстеп ! (z)\n"
            "\t\tиначе\n"
            "\t\t\tдо нгчет цикл\n"
            "\t\t\t\tесли е остат 2 = 1 то нечет ! \n"
            "\t\t\t\tиначе v := v*v\n"
            "\t\t\t\tвсе;\n"
            "\t\t\t\te=: e/:2 \n"
            "\t\t\tповторить;\n"
            "\t\t\tz:= 2*v\n"
            "\t\tвсе;\n"
            "\t\te:=e- 1\n"
            "\tповторить\n"
            "\tпри исчерпстел (zz#чис) : zz % результат \n"
            "\tвсесит; \n"
            "\tзапф (печ, возвстеп (5, 3) : \"5 ** 3 \"=  g (0))\n"
            "конец\n"
            "```\n"
            "This code defines a function возвстеп that calculates exponentiation through repeated squaring\\. The loop iterates until the exponent e reaches 0, at which point the accumulated result z is returned\\.\n\n"
            "*Example 3: Working with Bit Vectors\\. Sieve of Eratosthenes*\n"
            "```El-76\n"
            "начало\n"
            "\tпроцедура решето = проц (конст п#цел)\n"
            "\t\tначало\n"
            "\t\t\tконст печ = позп (ацпу),\n"
            "\t\t\t\tреш #с8л02 = ген солог (п) иниц ( : истина); \n"
            "\t\t\tперемен к#цел := 1;\n"
            "\t\t\tзапф (печ, 1: 72d);\n"
            "\t\t\tдля і от 2 до n - 1\n"
            "\t\t\tцикл\n"
            "\t\t\t\tесли реш [i) то\n"
            "\t\t\t\t\tзапф (печ, і : 7zd);\n"
            "\t\t\t\t\tесли (к := к + 1) > 16 то % перевод строки\n"
            "\t\t\t\t\tк : = 1;\n"
            "\t\t\t\t\tзапф (печ, : 1)\n"
            "\t\t\t\t\tвсе;\n"
            "\t\t\t\t\tдо верхгран\n"
            "\t\t\t\t\tцикл перем j#цел:= і ;\n"
            "\t\t\t\t\tреш [/] := ложь ;\n"
            "\t\t\t\t\tесли (j := j + i) > (n - 1)\n"
            "\t\t\t\t\tто верхгран ! все\n"
            "\t\t\t\tповторить \n"
            "\t\t\tвсе\n"
            "\t\tповторить\n"
            "\tконец; % процедуры решето\n"
            "\tрешето (10000)\n"
            "конец\n"
            "```\n"
            "This code defines a function решето that implements the Sieve of Eratosthenes algorithm\\. It illustrates the use of arrays and loops in El\\-76\\.\n\n"
            "*Example 4: Array Sorting Using the Insertion Sort Method*\n"
            "```El-76\n"
            "начало\n"
            "\tтип тм = массив [] перем#чис;\n"
            "\tконст печ = позп (ацпу),\n"
            "\t\tb#тм = ген тм (5) иниц (0:5, 1:3, 2:3, 3:4, 4:0): \n"
            "\tпроцедура сортпр = проц (конст а#тм)\n"
            "\t\tдля і от 1 до длина а - 1\n"
            "\t\tцикл\n"
            "\t\t\tперем ai#чис;\n"
            "\t\t\tai := a[i]\n"
            "\t\t\tдо найден\n"
            "\t\t\t\t(для j от i-1 вниздо 0\n"
            "\t\t\t\tцикл\n"
            "\t\t\t\t\tесли a[j] <= ai то найден ! (j)\n"
            "\t\t\t\t\tиначе % сдвинуть j-й вправо\n"
            "\t\t\t\t\ta[j + 1] := a[j]\n"
            "\t\t\t\t\tвсе\n"
            "\t\t\t\tповторить;\n"
            "\t\t\t\tнайден ! (-1))\n"
            "\t\t\tпри\n"
            "\t\t\t\tнайден (к#цел): a[к + 1] := ai;\n"
            "\t\t\tвесит\n"
            "\t\tповторить;\n"
            "\t\tзапф(печ, : “исходный массив:”, b: 10g(10));\n"
            "\t\tсортпр(b)\n"
            "\t\tзапф(печ, :”результирующий массив: “, b:10(10))\n"
            "конец\n"
            "```\n"
            "This example showcases the use of loops, conditionals, and array manipulation in El\\-76, illustrating how a straightforward sorting algorithm is implemented in the language\\.\n"
        ),
        parse_mode="MarkdownV2",
        reply_markup=InlineKeyboards().back_to_theory_el76()
    )


@programming_theory_router.callback_query(F.data == "theory_rapira")
async def rapira_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
        text=(
            "*RAPIRA*\n\n"
            "`Rapira` is a programming language designed with an educational intent, created to serve as a bridge from the educational language `Robic` to more standard programming languages\\. It was initially developed by _G\\.A\\. Zvenigorodsky_ and implemented as an interpreter within the *\"Shkolnitsa\" \\(\"Schoolgirl\"\\)* programming system on the *\"Agat\"* computer\\. The language's design is rooted in facilitating learning and ease of use, making it a suitable choice for beginners in programming\\.\n\n"
            "One of the notable aspects of `Rapira` is its _multiple regional versions_\\. This characteristic indicates that the language was adapted to meet the specific needs or preferences of different user bases, potentially including variations in keywords, syntax, or functionality to better align with regional educational standards or programming practices\\. These regional versions allow for a more localized and accessible learning experience, catering to the unique context of each user group\\.\n\n"
            "_In this particular theory resourse English version of Rapira is presented\\. However, here's a small code snippet of original Rapira:_\n"
            "```Rapira\n"
            "ПРОЦ СТАРТ();\n"
            "\tВЫВОД: “ЗДРАВСТВУЙ, МИР!”;\n"
            "КНЦ;```"
        ),
        parse_mode="MarkdownV2",
        reply_markup=InlineKeyboards().theory_rapira()
    )


@programming_theory_router.callback_query(F.data == "rapira_objects")
async def rapira_objects_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
        text=(
            "*Objects and Operations, supported by Rapira*\n\n"
            "*Objects:* _logical_ \\(`yes, no`\\), _integer_ and _real_ numbers, _texts_, _sequences_, the _empty object_ \\(empty\\)\\.\n"
            "_Procedures_, _functions_, _modules_, and _devices_ are also *objects*\\. "
            "For all objects, operations `\\=` and `/\\=` are defined\\.\n\n"
            "*Logical:* yes, no\n"
            "*Logical operations:* and, or, not\n\n"
            "*Numbers:* `125` \\(integer\\), `530\\.84` \\(real\\), `1\\.9e\\-8` \\(real\\)\n"
            "*Numeric operations:* `\\+` and `\\-` \\(unary and binary\\), `\\*`, `/`, `\\*\\*` \\(exponentiation\\), "
            "`//` and `/%` \\(integer division and remainder \\- for integer numbers\\), `\\>`, `\\<`, `\\>\\=`, `<\\=`\n\n"
            "_Example 1:_\n"
             "```Rapira\n"
            "fun PRIME(N)\n"
            "\tif N<2 then\n"
            "\t\treturn no\n"
            "\tfi\n"
            "\tfor M from 2 to sqrt(N)+0.5 do\n"
            "\t\tif N /% M = 0 then\n"
            "\t\t\treturn no\n"
            "\t\tfi\n"
            "\tod\n"
            "\treturn yes\n"
            "end\n"
            "output: PRIME(2003)\n"
            "```\n\n"
            "_Example 2:_\n"
            "```Rapira\n"
            "proc FRAME (N)\n"
            "\toutput: \"@\" * N\n"
            "\trepeat (N - 2) do\n"
            "\t\toutput: \"@\" + \" \" * (N - 2) + \"@\"\n"
            "\tod\n"
            "\toutput: \"@\" * N\n"
            "end\n\n"
            "call FRAME(5)\n"
            "```"
        ),
        parse_mode="MarkdownV2",
        reply_markup=InlineKeyboards().back_to_theory_rapira()
)

@programming_theory_router.callback_query(F.data == "rapira_sequences")
async def rapira_sequences_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Sequences*\n\n"
        "```\n"
        "<2,3,5,7,11>\n"
        "<“a”,“e”,“1”,“o”>\n"
        "<<1, 3, <6, 7, 9>>, 10, <44, 70, 99>>\n"
        "```\n\n"
        "*Sequence* is an _ordered set_ of objects\\. *Any* `Rapira` object may be an element of a sequence \\(including the other sequence\\)\\. The sequence construct operation `< \\>` builds a sequence\\.\n\n"
        "*Sequential operations:* `\\#` \\(length\\), `\\+` \\(concentration\\), `\\*` \\(multiplication by non\\-negative integer\\), `[]` \\(element select in the sequence\\), `[:]` \\(subsequence slice\\)\n\n"
        "_Example 1_:\n"
        "```Rapira\n"
        "fun TEXT_TO_WORDS (PHRASE)\n"
        "\tPHRASE:= PHRASE + \" \"\n"
        "\tWORDS:= <* *>\n"
        "\twhile PHRASE /= \"\" do\n"
        "\t\tK := index(\" \", PHRASE)\n"
        "\t\tif K /= 1 then\n"
        "\t\t\tWORDS:= WORDS + <* PHRASE[:K-1] *>\n"
        "\t\tfi\n"
        "\t\tPHRASE:= PHRASE[K+1:]\n"
        "\tod\n"
        "\treturn WORDS\n"
        "end\n\n"
        "WORDS_SEQUENCE:= TEXT_TO_WORDS(\"...many people nowadays Like marmelade Instead.\")\n"
        "output: WORDS_SEQUENCE\n"
        "```\n\n"
        "_Example 2_:\n"
        "```Rapira\n"
        "proc SORT ( <=NUMBERS )\n\n"
        "\tNEW:= <* *>\n"
        "\twhile NUMBERS /= <* *> do\n"
        "\t\tMIN:= NUMBERS[1]; IND:= 1\n"
        "\t\tfor K from 2 to #NUMBERS do\n"
        "\t\t\tif NUMBERS[K]<MIN then\n"
        "\t\t\t\tMIN:= NUMBERS[K]; IND:= K\n"
        "\t\t\tfi\n"
        "\t\tod\n"
        "\t\tNEW:= NEW + <* MIN *>\n"
        "\t\tNUMBERS[IND:IND]:= <* *>\n"
        "\tod\n"
        "\tNUMBERS:= NEW\n"
        "end\n"
        "DAYS:= <* *>\n"
        "repeat 10 do\n"
        "\tDAYS:= DAYS + <* int_rand(31) *>\n"
        "od\n"
        "output: DAYS\n"
        "SORT(<=DAYS)\n"
        "output: DAYS\n"
        "```"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_rapira()
)


@programming_theory_router.callback_query(F.data == "rapira_variables")
async def rapira_variables_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Variables*\n\n"
        "_Any object may act as the value of a variable\._\n\n"
        "*Example:*\n"
        "_Game:_ a person thinks of an animal; the computer tries to guess it by asking questions, for `‘yes’` and `‘no’` answer only\. If the animal is unknown, the computer asks for help thus enriching its `knowledge`\.\n\n"
        "The computer asks if this animal is thought of it\. If not, the computer gives up, asks for that animal, and a question to distinguish them both\. As a result, the leaf is replaced by the new subtree\.\n\n"
        "*Implementation:*\n"
        "The tree is represented by the sequence KNOWLEDGE:\n"
        "`<question, subtree for ‘yes’, subtree for ‘no’\\>`\n"
        "Each subtree is a similar _sequence_ or a text \(animal’s name\)\. When a subtree is chosen, the attempt variable value is a sequence or a text, depending upon the descend depth\.\n\n"
        "```Rapira\n"
        "proc ANIMALS ( <=KNOWLEDGE )\n\n"
        "\toutput: KNOWLEDGE[1], \"(yes,no)\"\n"
        "\tinput: ANSWER\n"
        "\tif ANSWER then\n"
        "\t\tN := 2\n"
        "\telse\n"
        "\t\tN := 3\n"
        "\tfi\n"
        "\tATTEMPT:= KNOWLEDGE[N]\n"
        "\tif is_seq(ATTEMPT) then\n"
        "\t\tANIMALS(<=ATTEMPT)\n"
        "\telse\n"
        "\t\toutput: \"Is it a \", ATTEMPT, \"?(yes,no)\"\n"
        "\t\tinput: ANSWER\n"
        "\t\tif ANSWER then\n"
        "\t\t\toutput: \"I've guessed!\"\n"
        "\t\telse\n\n"
        "\t\t\toutput: \"I give up\. What animal are you thinking of?\"\n"
        "\t\t\tinput text: BEAST\n"
        "\t\t\toutput: \"Type in a question to distinguish\"\n"
        "\t\t\toutput: \"a \", BEAST, \" and a \", ATTEMPT, \":\"\n"
        "\t\t\tinput text: QUESTION\n"
        "\t\t\toutput: \"What will be an answer for a \", BEAST, \"?\"\n"
        "\t\t\tinput: ANSWER\n"
        "\t\t\tif ANSWER then\n"
        "\t\t\t\tATTEMPT := <* QUESTION, BEAST, ATTEMPT *>\n"
        "\t\t\telse\n"
        "\t\t\t\tATTEMPT := <* QUESTION, ATTEMPT, BEAST *>\n"
        "\t\t\tfi\n"
        "\t\tfi\n"
        "\tfi\n"
        "\tKNOWLEDGE[N]:= ATTEMPT\n"
        "end\n\n"
        "ALL_ANIMALS:= <* \"Does it live in water?\", \"fish\", \"ostrich\" *>\n"
        "do\n"
        "\tANIMALS(<=ALL_ANIMALS)\n"
        "od\n"
        "```\n\n"
        "*How it works:*\n"
        "```Game\n"
        "- Does it live in water?(yes, no)\n"
        "  no\n"
        "- Is it an ostrich?(yes, no)\n"
        "  no\n"
        "- I give up\. What animal are you thinking of?\n"
        "  turtle\n"
        "- Type in a question to distinguish a turtle and an ostrich:\n"
        "  Has it wings?\n"
        "- What will be an answer for a turtle?\n"
        "  no\n"
        "- Does it live in water?(yes, no)\n"
        "  no\n"
        "- Has it wings?(yes, no)\n"
        "  yes\n"
        "- Is it an ostrich?(yes, no)\n"
        "  no\n"
        "- I give up\. What animal are you thinking of?\n"
        "  parrot\n"
        "- Type in a question to distinguish a parrot and an ostrich:\n"
        "  Can it fly?\n"
        "- What will be an answer for a parrot?\n"
        "  yes\n"
        "- Does it live in water?(yes, no)\n"
        "  yes\n"
        "- Is it a fish?(yes, no)\n"
        "  yes\n"
        "- I’ve guessed!```"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_rapira()
)


@programming_theory_router.callback_query(F.data == "rapira_slices")
async def rapira_slices_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Slices and selections*\n\n"
        "_Writing a variable you may use slices and selections:_\n"
        "```Rapira\n"
        "KNOWLEDGE[N] := ATTEMPT\n"
        "```\n\n"
        "_Example:_"
        "```Rapira\n"
        "proc REPLACE ( <=WHERE, =>WHAT, =>BY_WHAT )\n"
        "\tN:= 1\n"
        "\tdo\n"
        "\t\tK:= index (WHAT, WHERE [N:])\n"
        "\n"
        "\t\tif K = 0 then\n"
        "\t\t\texit\n"
        "\t\tfi\n"
        "\t\tK:= N+K-1\n"
        "\t\tWHERE[K:K+#WHAT-1]:= BY_WHAT\n"
        "\n"
        "\t\tN:= K + #BY_WHAT\n"
        "\tod\n"
        "end\n\n"
        "FAIRYTAIL:= \"Somebody said,\" + lf + \"\"\"Bother!\"\"\" + lf + \"And then he said,\" + lf + \"\"\"Oh, deary me!\"\"\" + lf + \"Somebody sobbed, \"\"Oh, deary me!\"\"\" + lf + \"And went back to bed.\"\n"
        "REPLACE (<=FAIRYTAIL, =>\"Somebody\", =>\"The King\")\n"
        "output: FAIRYTAIL\n"
        "```\n\n"
        "_So, the output would be:\n_"
        "`The King said,\n"
        "\"Bother\"!\n"
        "And then he said,\n"
        "\"Oh, deary me!\"\n"
        "The King sobbed, \"Oh, deary me!\"\n"
        "And went back to the bad\\.`"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_rapira()
)


@programming_theory_router.callback_query(F.data == "rapira_statements")
async def rapira_statements_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Statements*\n\n"
        "Statements: _assignment, procedure call, conditional, cases, loops, output, input, loop exit, return from procedure or function\\._\n"
        "Almost all statements were used in the examples before this section\\.\n\n"
        "`It is time for the largest example yet`\n\n"
        "_Example:_\n\n"
        "```Rapira\n"
        "proc GAME ()\n"
        "\textern: GAME_START, YOUR_TURN, MY_TURN, WRONG\n"
        "\tintern: RIDDLE, MIN, MAX, YOU_GUESSED, I_GUESSED\n"
        "\toutput: \"Who'll guess first?\"\n"
        "\tGAME_START()\n"
        "\tdo\n"
        "\t\toutput: \"Your turn:\"; YOUR_TURN()\n"
        "\t\toutput: \"My turn.\"; MY_TURN()\n"
        "\t\tcase\n"
        "\t\t\twhen YOU_GUESSED and I_GUESSED:\n"
        "\t\t\t\toutput: \"Nobody won!\"\n"
        "\t\t\twhen YOU_GUESSED:\n"
        "\t\t\t\toutput: \"You won!\"\n"
        "\t\t\twhen I_GUESSED:\n"
        "\t\t\t\toutput: \"I won!\"\n"
        "\t\tesac\n"
        "\t\tif YOU_GUESSED or I_GUESSED then\n"
        "\t\t\treturn\n"
        "\t\tfi\n"
        "\tuntil WRONG()\n\n"
        "\toutput: \"You've missed somewhere!\"\n"
        "\toutput: \"I don't want to play anymore.\"\n"
        "end\n\n"
        "proc GAME_START ()\n"
        "\textern: RIDDLE, MIN, MAX, YOU_GUESSED, I_GUESSED\n"
        "\toutput: \"Think of a number from 1 to 1000\"\n"
        "\toutput: \"and try to guess mine\"\n"
        "\tRIDDLE      := int_rand(1000)\n"
        "\tMIN         := 0\n"
        "\tMAX         := 1001\n"
        "\tYOU_GUESSED := no\n"
        "\tI_GUESSED   := no\n"
        "end\n\n"
        "proc YOUR_TURN ()\n"
        "\textern: RIDDLE, YOU_GUESSED\n"
        "\tintern: ATTEMPT\n"
        "\tinput: ATTEMPT\n"
        "\tcase\n"
        "\t\twhen ATTEMPT>RIDDLE:\n"
        "\t\t\toutput: \"My number is less!\"\n"
        "\t\twhen ATTEMPT<RIDDLE:\n"
        "\t\t\toutput: \"My number is greater!\"\n"
        "\tesac\n"
        "\tYOU_GUESSED:= (ATTEMPT = RIDDLE)\n"
        "end\n\n"
        "proc MY_TURN ()\n"
        "\textern: MIN, MAX, I_GUESSED\n"
        "\tintern: ATTEMPT, ANSWER, ANSWER_CORRECT\n"
        "\tATTEMPT:= (MIN+MAX) // 2\n"
        "\toutput: \"Is it \", ATTEMPT, \"?\"\n"
        "\tdo\n"
        "\t\toutput: \"Answers: =, > (riddle>\", ATTEMPT, \"), < (riddle<\", ATTEMPT, \")\"\n"
        "\t\tinput text: ANSWER\n"
        "\t\tANSWER_CORRECT:= yes\n"
        "\t\tcase ANSWER\n"
        "\t\t\twhen \">\":   MIN         := ATTEMPT\n"
        "\t\t\twhen \"<\":   MAX         := ATTEMPT\n"
        "\t\t\twhen \"=\":   I_GUESSED   := yes\n"
        "\t\t\telse        ANSWER_CORRECT:= no\n"
        "\t\t\t\t\t\t\toutput:\"You did a mistake\"\n"
        "\t\tesac\n"
        "\tuntil ANSWER_CORRECT\n"
        "end\n\n"
        "fun WRONG ()\n"
        "\textern: MAX, MIN\n"
        "\treturn MIN+1=MAX\n"
        "end\n\n"
        "GAME()\n"
        "```\n"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_rapira_statements()
)


@programming_theory_router.callback_query(F.data == "rapira_statements_game")
async def rapira_statements_game_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "_This is an example of how the game would be commenced:_\n\n"
        "```Game\n"
        "- Who'll guess first?\n"
        "- Think of a number from 1 to 1000 and try to guess mine\n"
        "- Your turn:\n"
        "  512\n"
        "- My number is less!\n"
        "- My turn.\n"
        "- Is it 500?\n"
        "- Answers: =, > (riddle> 500), < (riddle< 500)\n"
        "  <\n"
        "- Your turn:\n"
        "  256\n"
        "- My number is greater!\n"
        "- My turn.\n"
        "- Is it 250?\n"
        "- Answers: =, > (riddle> 250), < (riddle< 250)\n"
        "  <\n"
        "- Your turn:\n"
        "  384\n"
        "- My turn.\n"
        "- Is it 125?\n"
        "- Answers: =, > (riddle> 125), < (riddle< 125)\n"
        "  >\n"
        "- You won!```"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_rapira_statements_game()
)

@programming_theory_router.callback_query(F.data == "rapira_modules")
async def rapira_modules_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Modules and Devices*\n\n"
        "Means of modules and devices planned:\n"
        "\\- connecting a module enlarges the list of standard names _\\(including standard procedures and functions names\\)_\\.\n\n"
        "\\- connecting a module *enlarges the set* of simple statements\\.\n\n"
        "\\- a device is a special form of module\\. A device may be communicated with by means of input and output:\n"
        "\t\toutput \\>\\>printer:\n"
        "\t\t\t\t“This text \\- to printer”\n\n"
        "Input/output statements may contain mode specifications:\n"
        "\t\tinput text: QUESTION\t\t\t\\\ see example 9\n"
        "\"text\" is a keyword for the KEYBOARD device\\."
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_rapira()
)


@programming_theory_router.callback_query(F.data == "rapira_equivalents")
async def rapira_equivalents_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Russian equivalents of functions*\n\n"
        "_In this section, a table of simple functions in both English and Russian is presented:_\n\n"
        "```Rapira\n"
        "keyword::=    \\\ in the Russian variant\n"
        "and           \\\ и\n"
        "call          \\\ вызов\n"
        "case          \\\ выбор\n"
        "do            \\\ цикл\n"
        "else          \\\ иначе\n"
        "end           \\\ конец\n"
        "esac          \\\ все\n"
        "exit          \\\ выход\n"
        "extern        \\\ чужие\n"
        "fi            \\\ все\n"
        "for           \\\ для\n"
        "from          \\\ от\n"
        "fun           \\\ функ\n"
        "if            \\\ если\n"
        "input         \\\ ввод\n"
        "intern        \\\ свои\n"
        "nlf           \\\ бпс\n"
        "not           \\\ не\n"
        "od            \\\ кц\n"
        "or            \\\ или\n"
        "output        \\\ вывод\n"
        "proc          \\\ проц\n"
        "repeat        \\\ повтор\n"
        "return        \\\ возврат\n"
        "step          \\\ шаг\n"
        "text          \\\ текста\n"
        "then          \\\ то\n"
        "to            \\\ до\n"
        "until         \\\ кц по\n"
        "when          \\\ при\n"
        "while         \\\ пока\n"
        "```"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_rapira()
)

@programming_theory_router.callback_query(F.data == "rapira_others")
async def rapira_others_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
    text=(
        "*Other examples*\n\n"
        "_In this section, you can examine code which didn’t make it to the previous sections\\._\n\n"
        "```Rapira\n"
        "proc VICE_VERSA ()\n"
        "\toutput: \"Enter a text \"\n"
        "\tinput text: PHRASE\n"
        "\tREVERSED:= \"\"\n"
        "\tfor K to #PHRASE do\n"
        "\t\tREVERSED:= PHRASE[K] + REVERSED\n"
        "\tod\n"
        "\toutput: REVERSED\n"
        "end\n"
        "call VICE_VERSA()\n"
        "```\n\n"
        "```Rapira\n"
        "proc TEXT_BY_WORDS (PHRASE)\n"
        "\tPHRASE:= PHRASE + \" \"\n"
        "\twhile PHRASE /= \"\" do\n"
        "\t\tK:= index(\" \", PHRASE)\n"
        "\t\tif K /= 1 then\n"
        "\t\t\toutput: PHRASE[:K-1]\n"
        "\t\tfi\n"
        "\t\tPHRASE:= PHRASE[K+1:]\n"
        "\tod\n"
        "end\n"
        "TEXT_BY_WORDS(\"...I'll go and tell The cow Now Before she goes to bed.\")\n"
        "```\n\n"
        "```Rapira\n"
        "fun SIEVE (N)\n"
        "\tPRIME:= <* yes *> * N\n"
        "\tfor K from 2 to sqrt(N)+0.5 do\n"
        "\t\tif PRIME[K] then\n"
        "\t\t\tfor J from K+K to N step K do\n"
        "\t\t\t\tPRIME[J]:= no\n"
        "\t\t\tod\n"
        "\t\tfi\n"
        "\tod\n"
        "\tPRIME_NUMBERS:= <* *>\n"
        "\tfor K from 2 to N do\n"
        "\t\tif PRIME[K] then\n"
        "\t\t\tPRIME_NUMBERS:= PRIME_NUMBERS + <* K *>\n"
        "\t\tfi\n"
        "\tod\n"
        "\treturn PRIME_NUMBERS\n"
        "end\n"
        "output: SIEVE(5)\n"
        "output: SIEVE(200)\n"
        "```"
    ),
    parse_mode="MarkdownV2",
    reply_markup=InlineKeyboards().back_to_theory_rapira()
)

