const EventEmitter=require("events");
const event=new EventEmitter();
/*
event.on("saymyname",()=>
{
    console.log("Your name is rahul");
})
event.emit("saymyname");
*/

event.on("checkpage",(sc,msg)=>
{
    console.log(`status code is ${sc} and page is ${msg}`);
})

event.emit("checkpage",200,"ok");