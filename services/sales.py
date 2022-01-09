from datetime import date, datetime

from services.seller import SellerService
from services.sale_item import SaleItemService
from configuration.database import create_sale_item, get_connection

class SalesService():
    def __validate_required_field(self, input_value : str):
        """
            Validate if a required field has value

            :param
                input_value : str
            
            :return
                bool
        """
        if (input_value != ""):
            return True
        else:
            return False
    
    def __validate_input_type(self, input_value : str, input_type : type):
        """
            Validate if a input value is from a certain type

            :param
                input_value : str
                input_type : type
            
            :return
                bool
        """
        if(input_type == str):
            try:
                if type(input_value) == str:
                    return True
                else:
                    return False
            except:
                return False
        
        elif (input_type == date):
            try:
                datetime.strptime(input_value, '%Y-%m-%d')
                return True
            except:
                return False
        
        elif (input_type == float):
            try:
                float(input_value)

                if float(input_value) > 0:
                    return True
                else:
                    return False
            except:
                return False


    def receive_input(self, input_text : str, input_type : type, required : bool = True):
        """
            Function for receiving user's input

            :params
                input_text : str
                input_type : type
                required : bool

            :return
                str
        """
        try:
            user_input = input(input_text)

            if (required):
                # Function validating if input required has value
                valid = self.__validate_required_field(user_input)
                while not valid:
                    print("This field is required!\n")

                    user_input = input(input_text)

                    valid = self.__validate_required_field(user_input)
                
                # Function validating input type
                type_valid = self.__validate_input_type(user_input, input_type)
                while not type_valid:
                    print("Value inserted is invalid, please type an accordingly value!\n")

                    user_input = input(input_text)

                    type_valid = self.__validate_input_type(user_input, input_type)

            return user_input

        except Exception as e:
            print(e)
    
    def receive_seller_name(self):
        """
            Function for receiving user's input for the Seller Name

            :params

            :return
                int
        """
        seller_service = SellerService()

        #Getting the user input
        seller_name = self.receive_input(input_text= "Please enter the Seller Name: ", input_type= str)

        #Searching seller by the user input
        seller_id = seller_service.get_seller_id_by_seller_name(seller_name= seller_name)

        #Validating
        while not seller_id:
            print("Seller name not registered, please choose one of the existent sellers!\n")

            seller_name = self.receive_input(input_text= "Please enter the Seller Name: ", input_type= str)

            seller_id = seller_service.get_seller_id_by_seller_name(seller_name= seller_name)
        
        return seller_id

    
    def register_sale(self):
        """
            Function that request the inputs and register the sales

            :param

            :return
        """
        still_registering = True

        #Get the database connection
        db_connection = get_connection()
        sale_item_service = SaleItemService()

        #Loop to keep registering the sales
        while still_registering:
            
            #Show table with the sales ordered by seller with the highest to lowest amount sold
            sale_item_service.print_sales_order_by_seller_highest_amout()

            print("Let's register another sale!\n")

            #Getting the inputs values from answer
            seller_id : int = self.receive_seller_name()
            customer_name : str = self.receive_input(input_text= "Please enter the Customer Name: ", input_type= str)
            sale_date : str = self.receive_input(input_text= "Please enter the Date of the Sale (YYYY-MM-DD): ", input_type= date)
            sale_item_name : str = self.receive_input(input_text= "Please enter the Sale Item Name: ", input_type= str)
            sale_value : float = self.receive_input(input_text= "Please enter the Sale Value: ", input_type= float)
            
            #Inserting the sale item into the database
            create_sale_item(db_connection, seller_id, customer_name, sale_date, sale_item_name, float(sale_value))

            print("\nSale registered!\n")


