import sys


def stall():
    """Can be used in a loop for debugging.
    Stalls the current iteration and requires a user input to either 
    continue to the next iteration or quit the loop.

    Much poorer and infant version of python built-in function breakpoint().
    """

    inp = input("Press [q|Q] to quit OR Enter to continue... ")
    
    if inp.lower() == 'q':
        sys.exit(0)


def warning_format(msg, *args, **kwargs):
    """Used to generate warnings within code.
    Prints the warning in the following format:

    .. code:: console
        
        <script>:<n>: <type of warning>: <warning msg>
    
    ``n`` is the line number of initiated warning command within the script
    
    Sample Usage:

    .. code:: python

        import warnings
        from sap_utils import random
        warnings.formatwarning = random.warning_format
        warnings.warn("<Warning msg>")
    """
    
    return f"{args[1]}:{args[2]}: {args[0].__name__}: {str(msg)}\n"