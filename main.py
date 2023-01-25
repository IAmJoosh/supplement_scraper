from bs4 import BeautifulSoup
import requests


class Scrape_My_Supplement:
    def __init__(self):
        self.get_pages()
        self.get_input()
        self.scrape()

    def scrape(self):
        soup = BeautifulSoup(self.supplement_selection, "lxml")
        products = soup.find_all(
            "div", class_="box-text box-text-products text-center grid-style-2"
        )
        print(f"{self.supplement_selection.upper()}\n")
        for product in products:
            product_name = product.find(
                "a",
                class_="woocommerce-LoopProduct-link woocommerce-loop-product__link",
            ).text
            product_special_price = product.find("ins")
            if product_special_price != None:
                product_price = product_special_price.text
                sale = "Yes"
            else:
                product_price = product.find(
                    "span", class_="woocommerce-Price-amount amount"
                ).text
                sale = "No"

            print(
                f"Product Name: {product_name}\nPrice: {product_price}\nOn Sale: {sale}",
                end="\n\n",
            )

    def get_pages(self):
        self.html_protein = requests.get(
            "https://xtremenutrition.co.za/product-category/protein/?orderby=popularity"
        ).text
        self.html_preworkout = requests.get(
            "https://xtremenutrition.co.za/product-category/pre-workout/?orderby=popularity"
        ).text
        self.html_creatine = requests.get(
            "https://xtremenutrition.co.za/product-category/creatine/?orderby=popularity"
        ).text

    def get_input(self):
        self.supplement_selection = input("Which product?:")
        if self.supplement_selection == "creatine":
            self.supplement = self.html_creatine
        elif self.supplement_selection == "preworkout":
            self.supplement = self.html_preworkout
        elif self.supplement_selection == "protein":
            self.supplement = self.html_protein
        else:
            print("Invalid supplement")
            return


Scrape_My_Supplement()
