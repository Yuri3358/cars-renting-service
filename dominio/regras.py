class RentingRules:
    @staticmethod
    def check_renting_conflicts(new_renting, current_rentings):
        for rent in current_rentings:
            if new_renting.ending <= rent.starting:
                continue
            elif new_renting.starting >= rent.ending:
                continue
            else:
                raise ValueError("Selecione um intervalo válido!")
            
    @staticmethod
    def check_renting_period(new_renting, min_days, max_days):
        duration = (new_renting.end - new_renting.start).days

        if duration < min_days:
            raise ValueError("Duração inválida! Alugue por mais tempo!")
        elif duration > max_days:
            raise ValueError("Duração excedida!")
        
        if duration <= 0:
            raise ValueError("Data de término menor que a de início da locação.")
        
    @staticmethod
    def check_vehicle_avaliable(vehicle, rentings, desired_start, desired_end):
        for rent in rentings:
            if vehicle.license_plate == rent.license_plate:
                if not (desired_end <= rent.end or desired_start >= desired_end):
                    return False
                else:
                    return True
                
    @staticmethod  
    def renting_price_calc(renting, vehicle):
        daily_value = vehicle.daily_rent
        renting_duration = (renting.end - renting.start).days
        total_spent = daily_value*renting_duration
        
        return total_spent