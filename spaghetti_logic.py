"""Data processing module with clean code principles."""

# Constants
PRICE_ADJUSTMENT_RATE = 1.15
LOG_FILE_PATH = "log.txt"


def apply_price_adjustment(data: list[float], adjustment_rate: float) -> list[float]:
    """Apply price adjustment to a list of values.
    
    Args:
        data: List of numeric values to adjust
        adjustment_rate: Rate to multiply each value by (e.g., 1.15 for 15% increase)
    
    Returns:
        List of adjusted values
    """
    return [item * adjustment_rate for item in data]


def format_for_display(value: float) -> str:
    """Format a single value for display output.
    
    Args:
        value: Numeric value to format
    
    Returns:
        Formatted string suitable for printing
    """
    return f"Total: {value:.2f}"


def log_results(results: list[float], filepath: str = LOG_FILE_PATH) -> None:
    """Persist results to a log file.
    
    Args:
        results: List of values to log
        filepath: Path to the log file (default: LOG_FILE_PATH)
    """
    with open(filepath, "a") as log_file:
        log_file.write(str(results) + "\n")


def display_results(adjusted_values: list[float]) -> None:
    """Display all adjusted values to console.
    
    Args:
        adjusted_values: List of values to display
    """
    for value in adjusted_values:
        formatted_output = format_for_display(value)
        print(formatted_output)


def process_data(data: list[float]) -> list[float]:
    """Process data by applying adjustment, displaying, and logging results.
    
    This orchestrator function coordinates:
    1. Applying price adjustment to input data
    2. Displaying results to console
    3. Logging results to file
    
    Args:
        data: List of numeric values to process
    
    Returns:
        List of adjusted values
    """
    adjusted_values = apply_price_adjustment(data, PRICE_ADJUSTMENT_RATE)
    display_results(adjusted_values)
    log_results(adjusted_values)
    return adjusted_values
