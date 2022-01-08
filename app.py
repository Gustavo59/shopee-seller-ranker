from configuration import database

from services.sales import SalesService

def main():
    print("  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n" +
          " |                                                                 |\n" +
          " |  Seller's Ranking Logic                                         |\n" +
          " |                                                                 |\n" +
          " |  The five sellers registered are:                               |\n" +
          " |  1 - Nike                                                       |\n" +
          " |  2 - Adidas                                                     |\n" +
          " |  3 - Puma                                                       |\n" +
          " |  4 - Umbro                                                      |\n" +
          " |  5 - Fila                                                       |\n" +
          " |                                                                 |\n" +
          " |  Please register the sale item under one of the sellers name    |\n" +
          " | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |\n" +
          "\n"
    )

    #Init the database with the initial tables
    database.config_database()

    sales_service = SalesService()

    #Function that keeps registering the sales
    sales_service.register_sale()
    
    
if __name__ == '__main__':
    main()