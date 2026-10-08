playervar presses = 0

rule "Count an interact press":
    @Event eachPlayer
    @Condition eventPlayer.hasSpawned()
    @Condition eventPlayer.isHoldingButton(Button.INTERACT)
    eventPlayer.presses += 1
    smallMessage(eventPlayer, "Presses: {}".format(eventPlayer.presses))
