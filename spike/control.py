"""
Please don't edit this file unless you know what you are doing. Making changes \
to this file almost certaily will not do what you think it does.

This file only helps with code completion and intellisense. It does not run \
anything.
"""
class Timer():

    def __init__(self):
        """
        To use the Timer, you must first initialiZe it.

        Example

        from spike.control import Timer

        timer = Timer()

        """
        pass

    def reset(self):
        """
        Sets the Timer to "0"

        Example

        from spike.control import Timer

        timer = Timer()

        ... do some stuff

        timer.reset()
        """
        pass

    def now(self):
        """
        Retrieves the "right now" time of the Timer.
        
        Returns
        
        The current time, specified in seconds.
        
        Type: Integer (a positive or negative whole number, including 0)
        
        Values: A value greather than 0

        Example
        
        from spike.control import Timer

        timer = Timer()

        while True:
            if timer.now() > 5:
                break
        """
        pass

def wait_for_seconds(seconds):
    """
    Waits for a specified number of seconds before continuing the program.
    
    Parameters
    --------------
    seconds : The time to wait in seconds.
    
    Type : float (decimal value)
    
    Values : any value
    
    Default : no default value
    
    Errors
    ----------------
    TypeError : seconds is not a number.
    
    ValueError : seconds is not at least 0.
    """
    pass
def wait_until(get_value_function, operator_function, target_value=True):
    """
    Waits until the condition is True before continuing with the program.
    
    Parameters
    --------------
    get_value_function
    
    Type : callable function
    
    Values : A function that returns the current value to be compared to the target value.
    
    Default : no default value

    -----------------

    operator_function
    
    Type : callable function
    
    Values : A function that compares two arguments. The first argument will be the result of get_value_function() and the second argument will be target_value. The function will compare these two values and return the result.
    
    Default : no default value

    -----------------

    target_value
    
    Type : any type
    
    Values : Any object that can be compared by operator_function.
    
    Default : no default value
    
    Errors
    ----------------
    TypeError : get_value_function or operator_function is not callable or operator_function does not compare two arguments.

    Example
    ---------------
    from spike import ColorSensor

    from spike.control import wait_until

    from spike.operator import equal_to

    color_sensor = ColorSensor('A')

    wait_until(color_sensor.get_color, equal_to, 'red')

    Example
    ---------------
    from spike import ColorSensor, Motor

    from spike.control import wait_until

    color_sensor = ColorSensor('A')

    motor = Motor('B')

    def red_or_position():

        return color_sensor.get_color() == 'red' or motor.get_position() > 90

    wait_until(red_or_position)
    """
    pass
