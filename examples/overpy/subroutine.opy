playervar uses = 0

macro Player.showUses():
    smallMessage(self, "Uses: {}".format(self.uses))

def recordUse():
    eventPlayer.uses += 1
    eventPlayer.showUses()

rule "Call in the player's context":
    @Event eachPlayer
    @Condition eventPlayer.isHoldingButton(Button.INTERACT)
    recordUse()
