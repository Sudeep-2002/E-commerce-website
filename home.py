from flask import Blueprint,request
from classModules.productClass import objProducts
from classModules.adsClass import objAds
from classModules.visitorsClass import objVisitors
from classModules.contactClass import objContact
from classModules.productClicksClass import objProductClick


product_blueprint=Blueprint('product_blueprint',__name__)
@product_blueprint.route('/products',methods=['GET'])
def products():
    return objProducts.displayAllProducts()


@product_blueprint.route('/track-ad-click',methods=['GET'])
def logAdClick():
    return objAds.saveAdClick()
@product_blueprint.route('/track-visitors',methods=['GET'])
def logVisitors():
    return objVisitors.saveVisitor()

@product_blueprint.route('/save-contact',methods=['POST'])
def logContact():
    #Receiving the data from client/front end
    customerName=request.form['customerName']
    customerEmail=request.form['customerEmail']
    customerMobile=request.form['customerMobile']
    customerQuery=request.form['customerQuery']

    #check if name,email,mobile is empty
    if not customerName and not customerEmail and not customerMobile:
        return '["errFlag":1,"message":"Some Fields are empty"}]'
    
    return objContact.saveContact(customerName,customerEmail,customerMobile,customerQuery)

@product_blueprint.route('/track-product-click/<product_id>',methods=['GET'])  #in the browser give 127.0.0.1:8080/track-product-click/1
def trackProductClick(product_id):
   return objProductClick.saveProductClick(product_id)

