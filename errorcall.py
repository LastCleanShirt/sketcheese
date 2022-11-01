# TODO: Catch Error

class Error:
    # Initionalization
    def __init__(self):
        self.err_type = ["InvalidArgs"]

    # Print Error
    def PrintErr(self, type, msg):
        self.type = type
        self.msg = msg
        print("sketcheese: " + self.err_type[type])
        print("     " + msg)

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__()
