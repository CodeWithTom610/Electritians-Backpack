class ResistanceCalculating:
    """
    A class to calculate electrical resistance using voltage and current.
    """

    @staticmethod
    def ResistanceCalculatorSingle(Voltage: float, Current: float) -> float:
        """
        Calculates the resistance using Ohm's Law.

        Parameters:
        Voltage (float): The voltage in volts (V).
        Current (float): The current in amperes (A).

        Returns:
        float: The calculated resistance in ohms (Ω).
        
        Formula:
        Resistance = Voltage / Current
        """
        # Calculate resistance using the formula: Resistance = Voltage / Current
        Resistance = Voltage / Current

        # Return the calculated resistance
        return Resistance
