globalvar sourceValues = [1, 2, 3]
globalvar selectedValues
globalvar mappedValues
globalvar appendedValues
globalvar loopValues = []
globalvar i

rule "Copies and mutation":
    @Event global
    selectedValues = sourceValues.filter(lambda value: value > 1)
    mappedValues = selectedValues.map(lambda value, index: value + index)
    appendedValues = sourceValues.concat(4)
    sourceValues.append(5)
    for i in range(1, 5, 2):
        loopValues.append(i)
