globalvar mode = 1
globalvar multiplier
globalvar selectedValue

enum Mode:
    NORMAL = 1
    DOUBLE

rule "Explicit selection":
    @Event global
    switch mode:
        case Mode.NORMAL:
            multiplier = 1
            break
        case Mode.DOUBLE:
            multiplier = 2
            break
        default:
            multiplier = 0
    selectedValue = {1: 10, 2: 20, default: -1}[mode]
