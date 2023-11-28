from flask import Flask,request,render_template
import pickle
from datetime import datetime

app=Flask(__name__)
#loading the model

with open('random_forest.pkl', 'rb') as file: 
    random_forest_model = pickle.load(file)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    try:
         '''
        Required input for machine learning model
        1. bedrooms
        2. bathrooms
        3. sqft_living
        4. sqft_lot
        5. floors
        6. yr_built
        7. yr_renovated
        '''
         #syntax-->  var_name=request.form['<name which in present in html form(index.html)>']
         query_bedrooms = float(request.form['bedrooms'])
         query_bathrooms = float(request.form['bathrooms'])
         query_sqft_living = float(request.form['sqft_living'])
         query_sqft_lot = float(request.form['sqft_lot'])
         query_floors = float(request.form['floors'])
         query_yr_built = float(request.form['yr_built'])
         query_yr_renovated = float(request.form['yr_renovated'])

         #For Bedroom condition
         #For Bedroom condition
         if query_bedrooms=="numberofbedrooms":
            numberofbedrooms = 1
            numberofbedrooms_1=0
            numberofbedrooms_2=0
            numberofbedrooms_3=0
            umberofbedrooms_4=0
            numberofbedrooms_5=0
            numberofbedrooms_6=0
            numberofbedrooms_7=0
            numberofbedrooms_8=0
            numberofbedrooms_9=0
         elif query_bedrooms=="numberofbedrooms_1":
            numberofbedrooms=0
            numberofbedrooms_1=1
            numberofbedrooms_2=0
            numberofbedrooms_3=0
            umberofbedrooms_4=0
            numberofbedrooms_5=0
            numberofbedrooms_6=0
            numberofbedrooms_7=0
            numberofbedrooms_8=0
            numberofbedrooms_9=0
         elif query_bedrooms=="numberofbedrooms_2":
            numberofbedrooms=0
            numberofbedrooms_1=0
            numberofbedrooms_2=1
            numberofbedrooms_3=0
            umberofbedrooms_4=0
            numberofbedrooms_5=0
            numberofbedrooms_6=0
            numberofbedrooms_7=0
            numberofbedrooms_8=0
            numberofbedrooms_9=0
         elif query_bedrooms=="numberofbedrooms_3":
            numberofbedrooms=0
            numberofbedrooms_1=0
            numberofbedrooms_2=0
            numberofbedrooms_3=1
            umberofbedrooms_4=0
            numberofbedrooms_5=0
            numberofbedrooms_6=0
            numberofbedrooms_7=0
            numberofbedrooms_8=0
            numberofbedrooms_9=0
         elif query_bedrooms=="numberofbedrooms_4":
            numberofbedrooms=0
            numberofbedrooms_1=0
            numberofbedrooms_2=0
            numberofbedrooms_3=0
            numberofbedrooms_4=1
            numberofbedrooms_5=0
            numberofbedrooms_6=0
            numberofbedrooms_7=0
            numberofbedrooms_8=0
            numberofbedrooms_9=0
         elif query_bedrooms=="numberofbedrooms_5":
            numberofbedrooms=0
            numberofbedrooms_1=0
            numberofbedrooms_2=0
            numberofbedrooms_3=0
            numberofbedrooms_4=0
            numberofbedrooms_5=1
            numberofbedrooms_6=0
            numberofbedrooms_7=0
            numberofbedrooms_8=0
            numberofbedrooms_9=0
         elif query_bedrooms=="numberofbedrooms_6":
            numberofbedrooms=0
            numberofbedrooms_1=0
            numberofbedrooms_2=0
            numberofbedrooms_3=0
            numberofbedrooms_4=0
            numberofbedrooms_5=0
            numberofbedrooms_6=1
            numberofbedrooms_7=0
            numberofbedrooms_8=0
            numberofbedrooms_9=0
         elif query_bedrooms=="numberofbedrooms_7":
            numberofbedrooms=0
            numberofbedrooms_1=0
            numberofbedrooms_2=0
            numberofbedrooms_3=0
            numberofbedrooms_4=0
            numberofbedrooms_5=0
            numberofbedrooms_6=0
            numberofbedrooms_7=1
            numberofbedrooms_8=0
            numberofbedrooms_9=0
         elif query_bedrooms=="numberofbedrooms_8":
            numberofbedrooms=0
            numberofbedrooms_1=0
            numberofbedrooms_2=0
            numberofbedrooms_3=0
            numberofbedrooms_4=0
            numberofbedrooms_5=0
            numberofbedrooms_6=0
            numberofbedrooms_7=0
            numberofbedrooms_8=1
            numberofbedrooms_9=0
         else:
            numberofbedrooms=0
            numberofbedrooms_1=0
            numberofbedrooms_2=0
            numberofbedrooms_3=0
            numberofbedrooms_4=0
            numberofbedrooms_5=0
            numberofbedrooms_6=0
            numberofbedrooms_7=0
            numberofbedrooms_8=0
            numberofbedrooms_9=1

        # For Bathroom condition
         if query_bathrooms=="numberofbathrooms":
            numberofbathrooms=1
            numberofbathrooms_1=0
            numberofbathrooms_125=0
            numberofbathrooms_150=0
            numberofbathrooms_175=0
            numberofbathrooms_2=0
            numberofbathrooms_225= 0
            numberofbathrooms_250= 0
            numberofbathrooms_275= 0
            numberofbathrooms_3= 0
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0

         elif query_bathrooms==" numberofbathrooms_1":
            numberofbathrooms=0
            numberofbathrooms_1=1
            numberofbathrooms_125=0
            numberofbathrooms_150=0
            numberofbathrooms_175=0
            numberofbathrooms_2=0
            numberofbathrooms_225= 0
            numberofbathrooms_250= 0
            numberofbathrooms_275= 0
            numberofbathrooms_3= 0
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0
         elif query_bathrooms=="numberofbathrooms_125":
            numberofbathrooms=0
            numberofbathrooms_1=0
            numberofbathrooms_125=1
            numberofbathrooms_150=0
            numberofbathrooms_175=0
            numberofbathrooms_2=0
            numberofbathrooms_225= 0
            numberofbathrooms_250= 0
            numberofbathrooms_275= 0
            numberofbathrooms_3= 0
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0

         elif query_bathrooms==" numberofbathrooms_150":
            numberofbathrooms=0
            numberofbathrooms_1=0
            numberofbathrooms_125=0
            numberofbathrooms_150=1
            numberofbathrooms_175=0
            numberofbathrooms_2=0
            numberofbathrooms_225= 0
            numberofbathrooms_250= 0
            numberofbathrooms_275= 0
            numberofbathrooms_3= 0
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0
         elif query_bathrooms==" numberofbathrooms_175":
            numberofbathrooms=0
            numberofbathrooms_1=0
            numberofbathrooms_125=0
            numberofbathrooms_150=0
            numberofbathrooms_175=1
            numberofbathrooms_2=0
            numberofbathrooms_225= 0
            numberofbathrooms_250= 0
            numberofbathrooms_275= 0
            numberofbathrooms_3= 0
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0

         elif query_bathrooms==" numberofbathrooms_2":
            numberofbathrooms=0
            numberofbathrooms_1=0
            numberofbathrooms_125=0
            numberofbathrooms_150=0
            numberofbathrooms_175=0
            numberofbathrooms_2=1
            numberofbathrooms_225= 0
            numberofbathrooms_250= 0
            numberofbathrooms_275= 0
            numberofbathrooms_3= 0
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0

         elif query_bathrooms==" numberofbathrooms_225":
            numberofbathrooms=0
            numberofbathrooms_1=0
            numberofbathrooms_125=0
            numberofbathrooms_150=0
            numberofbathrooms_175=0
            numberofbathrooms_2=0
            numberofbathrooms_225= 1
            numberofbathrooms_250= 0
            numberofbathrooms_275= 0
            numberofbathrooms_3= 0
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0

         elif query_bathrooms==" numberofbathrooms_250":
            numberofbathrooms=0
            numberofbathrooms_1=0
            numberofbathrooms_125=0
            numberofbathrooms_150=0
            numberofbathrooms_175=0
            numberofbathrooms_2=0
            numberofbathrooms_225= 0
            numberofbathrooms_250= 1
            numberofbathrooms_275= 0
            numberofbathrooms_3= 0
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0

         elif query_bathrooms==" numberofbathrooms_275":
            numberofbathrooms=0
            numberofbathrooms_1=0
            numberofbathrooms_125=0
            numberofbathrooms_150=0
            numberofbathrooms_175=0
            numberofbathrooms_2=0
            numberofbathrooms_225= 0
            numberofbathrooms_250= 0
            numberofbathrooms_275= 1
            numberofbathrooms_3= 0
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0
            
         elif query_bathrooms==" numberofbathrooms_3":
            numberofbathrooms=0
            numberofbathrooms_1=0
            numberofbathrooms_125=0
            numberofbathrooms_150=0
            numberofbathrooms_175=0
            numberofbathrooms_2=0
            numberofbathrooms_225= 0
            numberofbathrooms_250= 0
            numberofbathrooms_275= 0
            numberofbathrooms_3= 1
            numberofbathrooms_325=0
            numberofbathrooms_350= 0
            numberofbathrooms_375= 0
            numberofbathrooms_4= 0
            numberofbathrooms_425= 0
            numberofbathrooms_450= 0
            numberofbathrooms_475= 0
            numberofbathrooms_5= 0
            numberofbathrooms_520= 0
            numberofbathrooms_550= 0
         
         model_data = [[query_bedrooms, query_bathrooms, 
                        query_sqft_living, query_sqft_lot, 
                        query_floors, query_yr_built, query_yr_renovated]]
         result=random_forest_model.predict(model_data)
         predicted_price = float(result[0])
         formatted_price = "{: .3f}".format(predicted_price)

         return render_template('index.html',results= formatted_price)
    except ValueError:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)