class RentingRules:
    @staticmethod
    def check_renting_conflicts(new_renting, current_rentings):
        for rent in current_rentings:
            if not (new_renting.end <= rent.start or new_renting.start <= rent.start):
                raise ValueError("Conflito detectado!")
    @staticmethod
    def check_renting_period(new_renting, min_days, max_days):
        duration = (new_renting.end - new_renting.start).days

        if duration < min_days:
            raise ValueError("Duração inválida! Alugue por mais tempo!")
        elif duration > max_days:
            raise ValueError("Duração excedida!")
        
        if duration <= 0:
            raise ValueError("Data de término menor que a de início da locação.")
        
    def renting_price_calc(renting, vehicle):
        daily_value = vehicle.daily_renting
        renting_duration = (renting.end - renting.start).days
        total_spent = daily_value*renting_duration
        
        return total_spent