def get_product_details(prd_id,name,quantity,price):
   return(
      f"Product ID: {prd_id}\n"
      f"Product name: {name}\n"
      f"Quantity: {quantity}\n"
      f"Price: {price}" 
  )

#Example usage (optional)
if __name__=="__main__":
    print(get_product_details("P101","Wireless Mouse",2,550))