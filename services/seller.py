from configuration.database import get_connection

class SellerService():
    db_connection = get_connection()

    def get_seller_id_by_seller_name(self, seller_name : str):
        """
            Function that get Seller Id by Seller Name

            :param
                seller_name : str

            :return
                int        
        """

        cur = self.db_connection.cursor()
        cur.execute("SELECT id FROM seller WHERE UPPER(name) =?", [seller_name.upper()])

        rows = cur.fetchall()

        if len(rows) > 0:
            return rows[0][0]
        else:
            return None