playervar offset
playervar effectId

rule "Capture offset, keep player position live":
    @Event eachPlayer
    @Condition eventPlayer.hasSpawned()
    @Condition eventPlayer.isHoldingButton(Button.INTERACT)
    eventPlayer.offset = vect(2, 0, 0)
    createEffect(eventPlayer, Effect.SPHERE, Color.BLUE,
        eventPlayer.getPosition() + evalOnce(eventPlayer.offset), 0.5,
        EffectReeval.VISIBILITY_POSITION_RADIUS_AND_COLOR)
    eventPlayer.effectId = getLastCreatedEntity()
    eventPlayer.offset = vect(5, 0, 0)
    wait(1, Wait.IGNORE_CONDITION)
    destroyEffect(eventPlayer.effectId)
    eventPlayer.effectId = null
