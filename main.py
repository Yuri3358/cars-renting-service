from infra.database_connection import conn
from infra.sql_repos import VehicleRepoSQL, RentingRepoSQL
from dominio.vehicle_service import VehicleService
from app.fachada import RentingFacade

vehicle_repo = VehicleRepoSQL(conn)
renting_repo = RentingRepoSQL(conn)

vehicle_service = VehicleService(vehicle_repo)
facade = RentingFacade(vehicle_repo, renting_repo, vehicle_service)

def main():
    while True:
        print("\n1 - Cadastrar veículo")
        print("2 - Listar veículos")
        print("3 - Sair")

        option = input("Escolha: ")

        if option == "1":
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

        elif option == "2":
            vehicles = facade.get_vehicles()
            for v in vehicles:
                print(v)

        elif option == "3":
            break

        else:
            print("Opção inválida.")