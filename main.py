from infra.database_connection import conn
from infra.sql_repos import VehicleRepoSQL, RentingRepoSQL
from dominio.vehicle_service import VehicleService
from dominio.renting_services import RentingService
from app.fachada import RentingFacade
from datetime import date
from uuid import uuid4

vehicle_repo = VehicleRepoSQL(conn)
renting_repo = RentingRepoSQL(conn)

vehicle_service = VehicleService(vehicle_repo)
renting_service = RentingService(renting_repo, vehicle_repo)
facade = RentingFacade(vehicle_repo, renting_repo, vehicle_service, renting_service)

def main():
    while True:
        print("\n1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Alugar veículo")
        print("4 - Sair")

        option = input("Escolha: ")

        if option == "1": #Registrar veículo
            brand = input("Marca: ")
            model = input("Modelo: ")
            license_plate = input("Placa: ")
            category = input("Categoria (SUV, Sedan, Hatch): ")
            daily_rent = float(input("Valor diário: "))

            try:
                facade.create_vehicle(brand, model, license_plate, category, daily_rent)
                print("Veículo cadastrado com sucesso!")
            except ValueError as e:
                print(e)

        elif option == "2": #listar veículos
            vehicles = facade.get_vehicles()
            for v in vehicles:
                print(v)

        elif option == "3": #alugar veículo
            renting_id = str(uuid4())
            license_plate = input("Placa do veículo: ")
            client_id = input("ID do cliente (CPF, somente números): ")
            start = date.fromisoformat(input("Data de início (YYYY-MM-DD): "))
            end = date.fromisoformat(input("Data de término (YYYY-MM-DD): "))

            try:
                total_price = facade.create_rentings(renting_id, license_plate, client_id, start, end)
                print(f"Locação realizada com sucesso! Valor total: R$ {total_price:.2f}")
            except ValueError as e:
                print("Erro:", e)

        elif option == "4": #sair
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()