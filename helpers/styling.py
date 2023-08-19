class Style:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    @staticmethod
    def bold(text):
        return f"{Style.BOLD}{text}{Style.ENDC}"

    @staticmethod
    def blue(text):
        return f"{Style.OKBLUE}{text}{Style.ENDC}"

    @staticmethod
    def yellow(text):
        return f"{Style.WARNING}{text}{Style.ENDC}"

    @staticmethod
    def green(text):
        return f"{Style.OKGREEN}{text}{Style.ENDC}"

    @staticmethod
    def red(text):
        return f"{Style.FAIL}{text}{Style.ENDC}"
