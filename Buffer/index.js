
const http=require("http");
const fs=require("fs");
const server=http.createServer();
/*
server.on('request',(req,res)=>
{
    const fs=require("fs");
    fs.readFile('input.txt',(err,data)=>
    {
        console.log(data);
        const m=data.toString();
        console.log(m);
        res.end(data.toString());
        if (err) return console.log(err);

        
    });


   
})
server.listen(8000,"127.0.0.1");
*/

server.on('request',(req,res)=>
{


    const rstream=fs.createReadStream("input.txt");
    rstream.on('data',(chunkdata)=>
    {


        res.write(chunkdata)
    });

    rstream.on("end",()=>
    {
        res.end();
    });
    rstream.on("error",(err)=>
    {
     console.log(err);
     res.end("file bot found");
    });
})

server.listen(8000,"127.0.0.1");