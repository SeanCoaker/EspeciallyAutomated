"""A module heavily based on code from https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running to provide animated text below the progress bar during the batch upload process.

This module is executed within its own thread to provide an animated loading icon to the label below the progress bar in the upload dialog window. This code has been adapted slightly from the code at https://stackoverflow.com/questions/22029562/python-how-to-make-simple-animated-loading-while-process-is-running to provide the desired solution.

    Typical usage example:

    self.loader = Loader(self.progressBarLabel, f'Starting {_espDevices[index]} - {ip[0]}...').start()
    self.loader.stop()

"""

from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

class Loader:
    """A class to provide an animated loading icon to the label below the progress bar in the upload dialog window.
    
    This class is used to provide an animated loading icon to the label below the progress bar in the upload dialog window.
    """

    def __init__(self, outputBox, desc="Loading...", end="Cancelling...", timeout=0.1):
        """Initialise the class.

        This function initialises the class setting the text to be displayed with the animation and the text to be displayed when the animation is complete.

        Args:
            outputBox (QtWidgets.QLabel): The label to display the animation and text.
            desc (str, optional): The loading text to be displayed with the animation. Defaults to "Loading...".
            end (str, optional): The text to be displayed when the animation is complete. Defaults to "Cancelling...".
            timeout (float, optional): The time between each step of the animation. Defaults to 0.1.
        """

        self.desc = desc
        self.end = end
        self.timeout = timeout
        self.isCancelled = False

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False
        self.finished = False

        self.outputBox = outputBox

    def start(self):
        """Starts the thread.
        
        This function starts the thread and begins the animated text.

        Args:
            self: The instance of the class.
        
        Returns:
            self - The instance of the class that wa spassed into the function.
        """

        self._thread.start()
        return self

    def _animate(self):
        """Displays the animated text
        
        This function cycles through the steps of the animation and displays the text, creating a loading animation.

        Args:
            self: The instance of the class.
        """

        for c in cycle(self.steps):
            if self.done:
                if self.isCancelled:
                    self.outputBox.setText('Cancelling...')
                else:
                    self.outputBox.setText(self.end)
                break
            self.outputBox.setText(f"\r{self.desc} {c}")
            sleep(self.timeout)

        self.finished = True

    def __enter__(self):
        """Calls for the animation to start.

        This function calls for the thread and the animation to start.
        
        Args:
            self: The instance of the class.
        """

        self.start()

    def stop(self):
        """Stops the animation.
        
        This function stops the animation by setting the done flag to True.

        Args:
            self: The instance of the class.
        """

        self.done = True

    def cancel(self):
        """Cancels the animation.
        
        This function stops the animation by setting the isCancelled flag and done flag to True.
        
        Args:
            self: The instance of the class.
        """

        self.done = True
        self.isCancelled = True

    def __exit__(self, exc_type, exc_value, tb):
        """Calls for the animation to stop.

        This function calls for the thread and the animation to stop.

        Args:
            self: The instance of the class.
            exc_type: The type of exception that was raised.
            exc_value: The value of the exception that was raised.
            tb: The traceback of the exception that was raised.
        """

        self.stop()

    def getFinished(self):
        """Returns the finished flag.

        This function returns the finished flag.

        Args:
            self: The instance of the class.

        Returns:
            self.finished - The finished flag.
        """

        return self.finished