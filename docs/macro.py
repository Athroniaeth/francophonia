def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    @env.macro
    def hello_world(name: str = "World"):
        """ A simple macro that returns a greeting. """
        return f"Hello {name}!"
