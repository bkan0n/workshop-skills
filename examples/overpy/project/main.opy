#!include "constants.opy"
settings "mode.opy.json"

globalvar multiplier = MULTIPLIER

rule "Project entry point":
    @Event global
    setMatchTime(MATCH_SECONDS)
