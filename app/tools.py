class ResistanceCalculating:
    """
    A class to calculate electrical resistance using voltage and current.
    """


    def ResistanceCalculatorSingle(self,Voltage: float, Current: float) -> float:
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
    

    def total_resistance_parallel(self,resistors) -> float:
        """
        Calculates the total resistance for components in parallel.

        Parameters:
        resistors (list): A list of resistors in ohms (Ω).

        Returns:
        float: The total resistance in ohms (Ω).
        
        Formula:
        Resistance = 1/(1 / R1 / R2 / R3 + Rn)
        """
        # Calculate the total resistance using the formula: 1 / Resistance = 1 / R1 + 1 / R2 + 1 / R3 + ...
        total_resistance = 1 / sum([1 / resistor for resistor in resistors])

        # Return the calculated total resistance
        return total_resistance
    

    def total_resistance_series(self, resistors: list) -> float:
        """
        Calculates the total resistance for components in series.

        Parameters:
        resistors (list): A list of resistors in ohms (Ω).

        Returns:
        float: The total resistance in ohms (Ω).
        
        Formula:
        Resistance = R1 + R2 + R3 + Rn
        """
        # Calculate the total resistance using the formula: Resistance = R1 + R2 + R3 + ...
        total_resistance = sum(resistors)

        # Return the calculated total resistance
        return total_resistance