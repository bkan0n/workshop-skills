globalvar flag = 0

rule "Deliberate numeric wait-until condition":
    @Event global
    waitUntil(flag, 1)
