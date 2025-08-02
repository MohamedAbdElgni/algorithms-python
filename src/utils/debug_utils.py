"""
Debug utilities for the algorithms project.

This module provides a global debug flag and helper functions for conditional printing.
"""

DEBUG = True


def debug_print(*args, **kwargs):
    """
    Print function that only prints when DEBUG flag is True.
    
    Args:
        *args: Arguments to pass to print()
        **kwargs: Keyword arguments to pass to print()
    """
    if DEBUG:
        print(*args, **kwargs)


def set_debug(enabled: bool):
    """
    Set the global debug flag.
    
    Args:
        enabled (bool): True to enable debug prints, False to disable
    """
    global DEBUG
    DEBUG = enabled


def is_debug_enabled() -> bool:
    """
    Check if debug mode is currently enabled.
    
    Returns:
        bool: True if debug is enabled, False otherwise
    """
    return DEBUG