from fastapi import FastAPI 
app =FastAPI()
 #https://ominous-enigma-6w7645wqq44f4gw4-8000.app.github.dev/ 
@app.get('/intro') 
def index(): 
   return 'FASTAPI'