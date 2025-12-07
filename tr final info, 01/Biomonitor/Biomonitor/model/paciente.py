"""
Modelo de Paciente para BioMonitor
Clase que representa a un paciente con sus signos vitales y cálculo de riesgo
"""

class Paciente:
    def __init__(self, nombre, id_paciente, edad, bpm=0, spo2=0, temperatura=0):
        """
        Constructor de la clase Paciente
        
        Args:
            nombre (str): Nombre del paciente
            id_paciente (str): Identificador único del paciente
            edad (int): Edad del paciente
            bpm (int): Frecuencia cardíaca en latidos por minuto
            spo2 (float): Saturación de oxígeno en porcentaje
            temperatura (float): Temperatura corporal en grados Celsius
        """
        self._nombre = nombre
        self._id_paciente = id_paciente
        self._edad = edad
        self._bpm = bpm
        self._spo2 = spo2
        self._temperatura = temperatura
    
    # ==================== GETTERS ====================
    
    def get_nombre(self):
        return self._nombre
    
    def get_id(self):
        return self._id_paciente
    
    def get_edad(self):
        return self._edad
    
    def get_bpm(self):
        return self._bpm
    
    def get_spo2(self):
        return self._spo2
    
    def get_temperatura(self):
        return self._temperatura
    
    # ==================== SETTERS ====================
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def set_id(self, id_paciente):
        self._id_paciente = id_paciente
    
    def set_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = edad
    
    def set_bpm(self, bpm):
        if bpm < 0:
            raise ValueError("Los BPM no pueden ser negativos")
        self._bpm = bpm
    
    def set_spo2(self, spo2):
        if spo2 < 0 or spo2 > 100:
            raise ValueError("SpO2 debe estar entre 0 y 100")
        self._spo2 = spo2
    
    def set_temperatura(self, temperatura):
        if temperatura < 30 or temperatura > 45:
            raise ValueError("Temperatura fuera de rango válido")
        self._temperatura = temperatura
    
    # ==================== LÓGICA BIOMÉDICA ====================
    
    def calcular_riesgo(self):
        """
        Calcula el nivel de riesgo del paciente según sus signos vitales
        
        Reglas biomédicas:
        - CRÍTICO: SpO2 < 90% OR BPM < 50 OR BPM > 120 OR Temp > 39°C OR Temp < 35°C
        - ALERTA: SpO2 < 95% OR BPM < 60 OR BPM > 100 OR Temp > 38°C OR Temp < 36°C
        - NORMAL: Resto de casos
        
        Returns:
            str: "Crítico", "Alerta" o "Normal"
        """
        # Condiciones CRÍTICAS
        if self._spo2 < 90:
            return "Crítico"
        if self._bpm < 50 or self._bpm > 120:
            return "Crítico"
        if self._temperatura > 39 or self._temperatura < 35:
            return "Crítico"
        
        # Condiciones de ALERTA
        if self._spo2 < 95:
            return "Alerta"
        if self._bpm < 60 or self._bpm > 100:
            return "Alerta"
        if self._temperatura > 38 or self._temperatura < 36:
            return "Alerta"
        
        # NORMAL
        return "Normal"
    
    def get_color_riesgo(self):
        """
        Retorna el color asociado al nivel de riesgo
        
        Returns:
            str: Color en formato hex o nombre
        """
        riesgo = self.calcular_riesgo()
        if riesgo == "Crítico":
            return "#FF4444"  # Rojo
        elif riesgo == "Alerta":
            return "#FFA500"  # Naranja
        else:
            return "#4CAF50"  # Verde
    
    def to_dict(self):
        """
        Convierte el paciente a un diccionario para facilitar el manejo de datos
        
        Returns:
            dict: Diccionario con todos los datos del paciente
        """
        return {
            "nombre": self._nombre,
            "id": self._id_paciente,
            "edad": self._edad,
            "bpm": self._bpm,
            "spo2": self._spo2,
            "temperatura": self._temperatura,
            "riesgo": self.calcular_riesgo()
        }
    
    def __str__(self):
        """Representación en string del paciente"""
        return f"Paciente: {self._nombre} (ID: {self._id_paciente}) - Riesgo: {self.calcular_riesgo()}"