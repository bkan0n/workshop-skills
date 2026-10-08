rule "Deliberately invalid API":
    @Event global
    thisApiDoesNotExist()
