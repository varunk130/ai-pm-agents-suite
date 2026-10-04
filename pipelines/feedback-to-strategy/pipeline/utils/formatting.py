"""
Formatting utilities for Rich console output and data presentation.

Built by Varun Kulkarni.
"""

from __future__ import annotations


def format_currency(amount: int | float, decimals: int = 0) -> str:
    """Format a number as USD currency. E.g. 2500000 → '$2,500,000'."""
    if decimals > 0:
        return f"${amount:,.{decimals}f}"
    return f"${int(amount):,}"


def format_percentage(value: float, decimals: int = 1) -> str:
    """Format a number as a percentage. E.g. 3.8 → '3.8%'."""
    return f"{value:.{decimals}f}%"


def format_duration(seconds: float) -> str:
    """
    Format a duration in seconds to a human-readable string.

    Examples:
        0.045  → '45ms'
        1.234  → '1.23s'
        65.0   → '1m 5s'
        3661.0 → '1h 1m 1s'
    """
    if seconds < 0:
        return "0ms"
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    if seconds < 60:
        return f"{seconds:.2f}s"
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    if minutes < 60:
        return f"{minutes}m {secs}s"
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h {mins}m {secs}s"
