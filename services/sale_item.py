from configuration.database import get_connection
import tableprint as tp

class SaleItemService():
    db_connection = get_connection()

    def print_sales_order_by_seller_highest_amout(self):
        """
            Function that print all sales ordered by seller with the highest to the lowest amount sold

            :param

            :return            
        """

        sql = '''
            SELECT 
                s.name,
                si.customer_name,
                si.sale_date,
                si.sale_item_name,
                si.sale_value
            FROM  (
                SELECT 
                    si.id_seller,
                    SUM(si.sale_value) total
                FROM
                    sale_item si
                GROUP BY
                    si.id_seller
            ) AS amount_sales
            INNER JOIN 
                sale_item si ON si.id_seller = amount_sales.id_seller
            INNER JOIN 
                seller s ON s.id = si.id_seller
            ORDER BY
                total DESC;
        '''
        cur = self.db_connection.cursor()
        cur.execute(sql)
        sales = cur.fetchall()

        print("Here is the updated list of all registered sales ordered by the seller with the highest amount sold \n")

        headers = ['Seller Name', 'Customer Name', 'Date of Sale', 'Sale Item Name', 'Sale Value']
        
        #Library that prints table with the content
        tp.table(sales, headers)