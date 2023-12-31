class Option:
    """
    A class for options shown on the screens.
    """

    def __init__(self, *args, description, func=None, **kwargs):
        """
        A constructor of option class.
        :param description: The description of the option shown on the screen,
        such as "Show all titles" or "Add a title".
        :param func: The function of the option, which defines its behaviour.
        :param args: The arguments that the function may need.
        :param kwargs: The dictionary of keyword arguments that the function may need.
        """
        self.description = description
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        """
        It runs the pre-defined function of the option.
        :return: The return of the function.
        """
        if self.func is not None:
            return self.func(*self.args, **self.kwargs)
        return None
