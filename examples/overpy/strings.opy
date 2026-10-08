playervar points = 0

rule "Format per-player text":
    @Event eachPlayer
    @Condition eventPlayer.hasSpawned()
    hudHeader(eventPlayer, f"Points: {eventPlayer.points}", color=Color.YELLOW)
