

# I need a enum with all possible combinations of the following:
# 1 - Wrong comma
# 2 - Abbreveation used
# 3 - Wrong Length

enum = {
    0: "NO_ERROR",
    1: "COMMA", # 1
    2: "ABBREVIATION", #2
    3: "LENGTH" #3
    4: "COMMA_LENGTH",#1 and 3
    5: "ABBREVIATION_LENGTH", #2 and 3
    6: "COMMA_ABBREVIATION", #1 and 2
    7: "COMMA_ABBREVIATION_LENGTH" #1, 2 and 3
}