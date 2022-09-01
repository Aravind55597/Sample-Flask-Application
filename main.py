from website import create_app 



app=create_app(); 

if __name__ =="__main__": 
    #debug true allows for hot-reload
    #0.0.0.0 makes the server publicly available
    app.run(debug=True,host='0.0.0.0', port=5000)

    
    