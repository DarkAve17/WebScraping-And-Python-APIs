#uvicorn routes:app --reload

from fastapi import FastAPI, HTTPException, Depends,UploadFile, File, status
from pydantic import BaseModel
from typing import List, Annotated
from models import TeamsData
from models import Base
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models
import io
import pandas as pd

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency= Annotated[Session, Depends(get_db)]



@app.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)):
    try:
        
        #contents = await file.read()  
        #decoded_contents = contents.decode()
       # df = pd.read_csv(io.StringIO(decoded_contents))
        
        #code to upload that file into a new table in a PostgreSql Database
        
        #df = pd.read_csv(contents)  
        #print(df)
        name_of_file= "List of Teams.CSV"
        
        df = pd.read_csv(f"C:\\Users\\mridu\\OneDrive\\Desktop\\VS Code\\Post CSV File to DB\\{name_of_file}")
        
        
        data = df.to_dict(orient='records')
        print(data[:5])
    
        with engine.connect() as conn:
            conn.execute(TeamsData.__table__.insert(), data)
            conn.commit()
        
        return {"Thankyou": "Data uploaded successfully."}
    
    except Exception as e:
        return status.HTTP_500_INTERNAL_SERVER_ERROR


@app.get("/Teams/{ID}")
async def team_by_id(ID:int, db:db_dependency):
    result = db.query(models.TeamsData).filter(models.TeamsData.ID == ID).first()
    if not result:
        raise HTTPException(status_code=404, detail='Data not found')
    return result