from flask import Blueprint,request
from classModules.visitorsClass import objVisitors
from classModules.adsClass import objAds
from classModules.productClicksClass import objProductClick

admin_dashboard_blueprint=Blueprint(__name__,'admin_dashboard_blueprint')
@admin_dashboard_blueprint.route('/today-visitors',methods=['GET'])
def tVisitors():
    return objVisitors.todayVisitors()

@admin_dashboard_blueprint.route('/today-ad-clicks',methods=['GET'])
def tAdClicks():
    return objAds.todayAdClick()     #GO HTML ADMIN DASHBOARD

@admin_dashboard_blueprint.route('/today-product-clicks',methods=['GET'])
def tPClicks():
    return objProductClick.overallProductClicks()

@admin_dashboard_blueprint.route('/visitor-trend',methods=['GET'])
def getVisitorTrend():
    return objVisitors.visitorsTrend()