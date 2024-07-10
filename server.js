const express = require("express");
const mongoose = require("mongoose");
const app = express();
require('dotenv').config()
const uri = process.env.MONGO_URI;


const PORT = 8000;


async function connect(){
    try{
        await mongoose.connect(uri);
        console.log("Successful connection to MongoDB")
    }catch(error){
        console.log(error)
    }
}
connect();

app.listen(PORT,()=> console.log(`Server started on ${PORT}`));